import os

from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from init import db, ma, bcrypt, jwt


def create_app():
    app = Flask(__name__)
    
    # configs
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # Connect libraries with flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # global error handling
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": str(err)}, 400
    
    @app.errorhandler(404)
    def not_found(err):
        return {"error": str(err)}, 404

    @app.errorhandler(IntegrityError)
    def integrity_error(err):
        # Handle NOT NULL violations, such as missing fields in the request
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            # Return a 400 Bad Request with a message specifying the missing field
            return {"error": f"The '{err.orig.diag.column_name}' field is required"}, 400
        
        # Handle UNIQUE violations, such as trying to use an email that already exists
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            # Return a 409 Conflict error indicating the email is already in use
            return {"error": f"Email address already in use"}, 409
        

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.portfolios_controller import portfolios_bp
    app.register_blueprint(portfolios_bp)

    from controllers.assets_controller import assets_bp
    app.register_blueprint(assets_bp)

    from controllers.ownedAssets_controller import ownedAssets_bp
    app.register_blueprint(ownedAssets_bp)

    from controllers.transactions_controller import transactions_bp
    app.register_blueprint(transactions_bp)

    return app