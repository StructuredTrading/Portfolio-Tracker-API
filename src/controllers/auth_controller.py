from datetime import timedelta
import functools

from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import db, bcrypt
from models.users import User, user_schema


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def authorise_as_admin(custom_error_message=None):
    """
    Decorator: authorise_as_admin

    Functionality: This decorator is used to restrict access to certain endpoints to only users with administrative privileges. It checks the role of the user making the request and allows the request to proceed if the user is an admin. Otherwise, it returns an error response.

    Input: Optionally takes a custom error message to be returned if the user is not authorized.
    Output: The decorated function's output if the user is an admin, or a JSON error message and HTTP status code 403 (Forbidden) if not.

    Errors:
    - Returns a 403 Forbidden error message and status code if the user attempting to access the function is not an admin. The error message can be customized.

    Requires:
    - A valid JWT token in the Authorization header to authenticate the request and verify the user's identity and administrative status.
    """

    def decorator(fn):
        """
        Decorator function that checks if the currently logged-in user has administrative privileges.
        
        :param custom_error_message: Optional string parameter for specifying a custom error message.
        """

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # Retrieve the currently logged-in user's ID from JWT token
            current_user = get_jwt_identity()
             # Query the database for the user with the retrieved ID
            stmt = db.select(User).filter_by(userID=current_user)
            user = db.session.scalar(stmt)
            # Check if the user is marked as an admin
            if user and user.is_admin:
                # Allow the request to proceed and execute the decorated function
                return fn(*args, **kwargs)
            # else (if the user is NOT an admin)
            else:
                # User is not an admin, prepare custom or default error message
                error_message = custom_error_message or "Not authorised to perform this action"
                # Return an error response indicating the user is not authorized
                return {"error": error_message}, 403
        return wrapper
    return decorator


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
def delete_user(user_id):
    """
    Endpoint: DELETE /auth/delete/<int:user_id>

    Functionality: This endpoint handles the deletion of a user record from the database. It checks if the user making the request has the right authorization to delete the specified user account. The endpoint requires JWT authentication, and the user must be the account owner or an admin to proceed with deletion. Upon successful deletion, it returns a confirmation message.

    Input: User ID as part of the URL path.
    Output: JSON object with a message indicating successful deletion, and HTTP status code 200 (OK).

    Errors: 
    - Returns a 401 Unauthorized error message and status code if the user is not the account owner or an admin.
    - Returns a 404 Not Found error message and status code if the user account does not exist.

    Requires:
    - JWT token in the Authorization header to authenticate the request.
    - `user_id` parameter in the URL path specifying the user account to be deleted.
    """
    # Get the current user's ID from the JWT token
    current_user_id = get_jwt_identity()

    # Fetch the current user's record from the database
    current_user = User.query.get(current_user_id)

    # Prepare a statement to find the user to delete by their user ID
    stmt = db.select(User).filter_by(userID=user_id)
    user_to_delete = db.session.scalar(stmt)

    # If the user to delete is found in the database
    if user_to_delete:
        # Check if the current user is either the user to be deleted or an admin
        if (str(user_to_delete.userID) == current_user_id) or (current_user.is_admin):
            # Delete the user record from the database and commit the changes
            db.session.delete(user_to_delete)
            db.session.commit()
            # Return a success message
            return {"message": f"User with userID '{user_to_delete.userID}' successfully deleted."}, 200
        # Return an error if the current user is neither the user to be deleted nor an admin
        else:
            return {"error": "Unauthorized. You do not have permission to perform this action."}, 401
    # Return an error if the user to be deleted was not found
    else:
        return {"error": f"User with 'userID' '{user_id}' does not exist."}, 404