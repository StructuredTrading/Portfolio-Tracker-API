from flask import Blueprint

from init import db, bcrypt
from models.user import User

db_commands = Blueprint('db', __name__)

# Create the tables in the database
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created successfully.")

# Drops all tables from the database
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables deleted successfully.")