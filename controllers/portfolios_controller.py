from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.portfolios import Portfolio, portfolio_schema, portfolios_schema


portfolios_bp = Blueprint("portfolios", __name__, url_prefix="/portfolios")

# Retrieve all portfolios from portfolios table in database
@portfolios_bp.route("/") # /portfolios
def get_all_portfolios():
    # SQL select statement to retrieve all entries from 'portfolios' table,
    # ordering them by 'portfolioID'
    stmt = db.select(Portfolio).order_by(Portfolio.portfolioID)
    # Execute SQL statement 'stmt' against database, and retrieve the result.
    portfolios = db.session.execute(stmt).scalars().all() 
    return portfolios_schema.dump(portfolios), 200


# Create new portfolio in portfolios table
@portfolios_bp.route("/create", methods=["POST"]) # /portfolios/create
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


# Update a portfolio in portfolios table
@portfolios_bp.route("/update/<int:portfolio_id>", methods=["PUT","PATCH"])
@jwt_required()
def update_portfolio(portfolio_id):
    # Retrieve body data from JSON
    data = portfolio_schema.load(request.get_json())
    # Retrieve the portfolio from database whose fields need to be updated
    stmt = db.select(Portfolio).filter_by(portfolioID=portfolio_id)
    portfolio = db.session.scalar(stmt)
    # If portfolio exists
    if portfolio:
        if str(portfolio.userID) != get_jwt_identity():
            return {"error": "Only the owner can edit this portfolio"}, 403
        # Update the fields
        portfolio.name=data.get("name") or portfolio.name,
        portfolio.description=data.get("description") or portfolio.description
        # commit the changes
        db.session.commit()
        # Return the updated portfolio back
        return portfolio_schema.dump(portfolio)
    # Else
    else:
        # Return error msg
        return {"error": f"Portfolio with id '{portfolio_id}' not found"}, 404