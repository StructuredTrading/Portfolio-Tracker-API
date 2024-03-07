from flask import Blueprint, request

from init import db
from models.portfolios import Portfolio, portfolios_schema


portfolios_bp = Blueprint("portfolios", __name__, url_prefix="/portfolios")

# Retrieve all portfolios table from database
@portfolios_bp.route("/")
def get_all_portfolios():
    # SQL select statement to retrieve all entries from 'portfolios' table,
    # ordering them by 'portfolioID'
    stmt = db.select(Portfolio).order_by(Portfolio.portfolioID)
    # Execute SQL statement 'stmt' against database, and retrieve the result.
    portfolios = db.session.execute(stmt).scalars().all() 
    return portfolios_schema.dump(portfolios), 200