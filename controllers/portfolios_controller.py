from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.portfolios import Portfolio, portfolio_schema, portfolios_schema
from models.transactions import Transaction
from models.ownedAssets import OwnedAsset
from controllers.auth_controller import authorise_as_admin


portfolios_bp = Blueprint("portfolios", __name__, url_prefix="/portfolios")

def refresh_portfolio():
    stmt = db.select(Portfolio)
    portfolios = db.session.scalars(stmt).all()
    if portfolios:
        for portfolio in portfolios:
            stmt2 = db.select(Transaction).filter_by(portfolioID=portfolio.portfolioID)
            stmt3 = db.select(OwnedAsset).filter_by(portfolioID=portfolio.portfolioID)
            transactions = db.session.scalars(stmt2).all()
            ownedAssets = db.session.scalars(stmt3).all()
            print(f"owned Assets:{ownedAssets}")
            total_cost = sum(transaction.totalCost for transaction in transactions)
            if portfolio.holdings != total_cost:
                portfolio.holdings=total_cost
            # if portfolio.ownedAssets != ownedAssets:
            # print(f"porfolio contains: {portfolio.ownedAssets}")
            # print(f"portfolio doesnt contain {ownedAssets}")
        db.session.commit()

# Retrieve all portfolios from portfolios table in database
@portfolios_bp.route("/") # /portfolios
@jwt_required()
@authorise_as_admin(custom_error_message="Only user Admin can retrieve all available portfolio's. Try using '/portfolios/search/<portfolio_id>' to search.")
def get_all_portfolios():
    # SQL select statement to retrieve all entries from 'portfolios' table,
    # ordering them by 'portfolioID'
    refresh_portfolio()
    stmt = db.select(Portfolio).order_by(Portfolio.portfolioID)
    # Execute SQL statement 'stmt' against database, and retrieve the result.
    portfolios = db.session.execute(stmt).scalars().all() 
    return portfolios_schema.dump(portfolios), 200


# Retrieve portfolio by portfolioID
@portfolios_bp.route("/search/<int:portfolio_id>", methods=["GET"]) #   /portfolios/search/<portfolio_id>
@jwt_required()
def search_for_portfolio(portfolio_id):
    refresh_portfolio()
    # Retrieve boy data from JSON
        # SQL select statement to retrieve to retrieve portfolio entry in 'portfolios' table,
    # that matches 'portfolio_id'
    stmt = db.select(Portfolio).filter_by(portfolioID=portfolio_id)
    portfolio = db.session.scalar(stmt)
    # If portfolio exists
    if portfolio:
        if str(portfolio.userID) != get_jwt_identity():
            return {"error": "Only the owner can retrieve this portfolio"}, 403
        # Return portfolio
        return portfolio_schema.dump(portfolio)
    else:
        return {"error" : f"Portfolio with id '{portfolio_id}' not found"}, 404


# Create new portfolio in portfolios table
@portfolios_bp.route("/create", methods=["POST"]) # /portfolios/create
@jwt_required()
def create_portfolio():
    stmt = db.select(Portfolio).filter_by(userID=get_jwt_identity())
    existing_portfolio = db.session.scalar(stmt)
    if existing_portfolio:
        return {"error": f"User '{existing_portfolio.userID}' allready has a portfolio called '{existing_portfolio.name}'."}
    # Retrieve body data from JSON in portfolio_schema format
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
@portfolios_bp.route("/update/<int:portfolio_id>", methods=["PUT","PATCH"]) #   /portfolios/update/<portfolio_id>
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
    

# Delete a portfolio from portfolios table
@portfolios_bp.route("/delete/<int:portfolio_id>", methods=["DELETE"]) #    /portfolios/delete/<portfolio_id>
@jwt_required()
def delete_portfolio(portfolio_id):
    stmt = db.select(Portfolio).filter_by(portfolioID=portfolio_id)
    portfolio = db.session.scalar(stmt)
    if portfolio:
        if str(portfolio.userID) != get_jwt_identity():
            return {"error": f"Only the owner can delete the portfolio '{portfolio.name}' portfolio"}, 403
        else:
            db.session.delete(portfolio)
            db.session.commit()
            return {"message": f"Portfolio '{portfolio.name}' with portfolio ID '{portfolio.portfolioID}' has successfully been deleted."}, 200
    else:
        return {"error": f"Portfolio with ID '{portfolio_id}' not found."}, 404