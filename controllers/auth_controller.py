from datetime import timedelta

from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from init import db, bcrypt
from models.users import User, user_schema


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

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