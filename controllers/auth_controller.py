from flask import Blueprint, request

from init import db, bcrypt
from models.users import User, user_schema


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register a new user
@auth_bp.route("/register", methods=["POST"]) # /auth/register
def auth_register():
    # Retrieve data from the body of the request
    data = request.get_json()
    # retrieve the password field from json request
    password = data.get("password")
    hashed_password = ""
    # If password exists, hash the password
    if password:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # create the user instance
    user = User(
        email=data.get("email"),
        password=hashed_password
    )

    # Add and commiit the user to the database
    db.session.add(user)
    db.session.commit()
    # Respond back to the client
    return user_schema.dump(user), 201