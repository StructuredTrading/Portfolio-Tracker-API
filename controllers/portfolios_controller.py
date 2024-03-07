from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.portfolios import Portfolio, portfolio_schema, portfolios_schema


portfolios_bp = Blueprint("portfolios", __name__, url_prefix="/portfolios")

# Retrieve all portfolios from portfolios table in database
@portfolios_bp.route("/")
def get_all_portfolios():
    # SQL select statement to retrieve all entries from 'portfolios' table,
    # ordering them by 'portfolioID'
    stmt = db.select(Portfolio).order_by(Portfolio.portfolioID)
    # Execute SQL statement 'stmt' against database, and retrieve the result.
    portfolios = db.session.execute(stmt).scalars().all() 
    return portfolios_schema.dump(portfolios), 200


# Create new portfolio in portfolios table
@portfolios_bp.route("/create", methods=["POST"])
@jwt_required()
def create_portfolio():
    # Retrieve body data from JSON
    data = portfolio_schema.load(request.get_json())
    # Create new portfolio model instance
    portfolio = Portfolio(
        name=data.get("name"),
        description=data.get("description"),
        date=date.today(),
        userID=get_jwt_identity()
    )
    # Add portfolio instance tro the session and commit
    db.session.add(portfolio)
    db.session.commit()
    # Return newly created portfolio
    return portfolio_schema.dump(portfolio), 201