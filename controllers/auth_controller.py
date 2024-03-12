from datetime import timedelta
import functools

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import db, bcrypt
from models.users import User, user_schema


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def authorise_as_admin(custom_error_message=None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            stmt = db.select(User).filter_by(userID=current_user)
            user = db.session.scalar(stmt)
            # If the user is an admin
            if user.is_admin:
                # We will continue and run the decorated function
                return fn(*args, **kwargs)
            # else (if the user is NOT an admin)
            else:
                # set the error_message to be returned
                error_message = custom_error_message or "Not authorised to perform this action"
                # return an error
                return {"error": error_message}, 403
        return wrapper
    return decorator


def authorised_user(custom_error_message=None, user_id=None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            stmt = db.select(User).filter_by(userID=current_user)
            user = db.session.scalar(stmt)
            # If the currently logged in user is the same user as the user_id in the API call
            if user.userID == user_id:
                # We will continue and run the decorated function
                return fn (*args, **kwargs)
            # else (if the user is not the same user as being requested in the API call)
            else:
                # set the error_message to be returned
                error_message = custom_error_message or "Not authorised to perform this action"
                # return an error
                return {"error": error_message}, 403
        return wrapper
    return decorator
            

# Register a new user
@auth_bp.route("/register", methods=["POST"]) # /auth/register
def auth_register():
    # Retrieve data from the body of the request
    data = request.get_json()
    # Retrieve the password field from json request
    password = data.get("password")
    hashed_password = ""
    # If password exists, hash the password
    if password:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # Create the user instance
    user = User(
        email=data.get("email"),
        password=hashed_password
    )

    # Add and commiit the user to the database
    db.session.add(user)
    db.session.commit()
    # Respond back to the client
    return user_schema.dump(user), 201


# Login a registered user
@auth_bp.route("/login", methods=["POST"]) # /auth/login
def auth_login():
    # Retrieve data from the body of the request
    data=request.get_json()
    # Find the user with matching email address
    stmt = db.select(User).filter_by(email=data.get("email"))
    user = db.session.scalar(stmt)
    # If email and password is correct
    if user and bcrypt.check_password_hash(user.password, data.get("password")):
        # Create JWT access token
        token = create_access_token(identity=str(user.userID), expires_delta=timedelta(days=1))
        return {"email": user.email, "token": token, "is_admin": user.is_admin}
    # Else
    else:
        # Return error
        return {"error": "Invalid email or password"}, 401
    

# Delete a user
@auth_bp.route("/delete/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    stmt = db.select(User).filter_by(userID=user_id)
    user = db.session.scalar(stmt)
    if user:
        if str(user.userID) == get_jwt_identity():
            db.session.delete(user)
            db.session.commit()
            return {"message": f"User '{user.userID}' succesfully deleted."}
        else:
            return {"error": f"Only the user can delete there account."}
    else:
        return {"error": f"User with userID '{user_id}' does not exist."}