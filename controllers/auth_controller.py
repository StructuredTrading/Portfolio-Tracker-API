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


# def authorised_user(custom_error_message=None):
#     def decorator(fn):
#         @functools.wraps(fn)
#         def wrapper(*args, **kwargs):
#             data = request.get_json()
#             current_user = get_jwt_identity()
#             stmt = db.select(User).filter_by(userID=current_user)
#             user = db.session.scalar(stmt)
#             # If the currently logged in user is the same user as the user_id in the API call
#             if user.userID == data.get("userID"):
#                 # We will continue and run the decorated function
#                 return fn (*args, **kwargs)
#             # else (if the user is not the same user as being requested in the API call)
#             else:
#                 # set the error_message to be returned
#                 error_message = custom_error_message or "Not authorised to perform this action"
#                 # return an error
#                 return {"error": error_message}, 403
#         return wrapper
#     return decorator


# 
@auth_bp.route("/register", methods=["POST"])
def auth_register():
    """
    Endpoint: POST /auth/register
    Functionality: This endpoint handles user registration. It validates the input data,
    hashes the user's password for security, and creates a new user record in the database.
    Upon successful registration, it returns the newly created user data.
    
    Input: JSON object containing 'email' and 'password'.
    Output: JSON object of the registered user excluding the password, and HTTP status code 201 (Created).
    Errors: Returns appropriate error messages and HTTP status codes for invalid inputs or failed operations.
    """
    # Validate and deserialize json input
    data = user_schema.load(request.get_json())

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8') if data.get('password') else None

    # Create and save the user
    user = User(
        email=data.get("email"), 
        password=hashed_password
        )
    db.session.add(user)
    db.session.commit()

    # Return the created user
    return user_schema.dump(user), 201


# Login a registered user
@auth_bp.route("/login", methods=["POST"]) # /auth/login
def auth_login():
    """
    Endpoint: POST /auth/login
    Functionality: This endpoint handles the login process for registered users. It validates the input data against the user schema,
    checks for a user with the matching email, and verifies the password. Upon successful authentication,
    it generates a JWT access token with a specified expiration time and returns the user's email, access token,
    and admin status. If the email or password does not match, it returns an error.
    Input: JSON object containing 'email' and 'password'.
    Output: On successful authentication, returns a JSON object with the user's email, a JWT access token, 
    and a boolean indicating whether the user is an admin, along with HTTP status code 200 (OK).
    Errors: Returns an error message and HTTP status code 401 (Unauthorized) for incorrect email or password.
    """
    # Validate and deserialize json input
    data = user_schema.load(request.get_json())

    # Find the user with matching email address
    stmt = db.select(User).filter_by(email=data.get("email"))
    user = db.session.scalar(stmt)
    
    # If email and password is correct
    if user and data.get("password") and bcrypt.check_password_hash(user.password, data.get("password")):

        # Create JWT access token and return login information
        token = create_access_token(identity=str(user.userID), expires_delta=timedelta(days=1))
        return {"email": user.email, "token": token, "is_admin": user.is_admin}, 200
    
    # Else return error
    else:
        return {"error": "Invalid email or password"}, 401
    

# Delete a user
@auth_bp.route("/delete/<int:user_id>", methods=["DELETE"])
@jwt_required()
# @authorised_user()
def delete_user(user_id):
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    stmt = db.select(User).filter_by(userID=user_id)
    user_to_delete = db.session.scalar(stmt)

    # If user to delete exists
    if user_to_delete:
        # Check if the current user is the user to be deleted OR if the current user is an admin
        if (str(user_to_delete.userID) == current_user_id) or (current_user.is_admin):
            db.session.delete(user_to_delete)
            db.session.commit()
            return {"message": f"User with userID '{user_to_delete.userID}' successfully deleted."}, 200
        else:
            return {"error": "Unauthorized. You do not have permission to perform this action."}, 403
    else:
        return {"error": f"User with 'userID' '{user_id}' does not exist."}, 404