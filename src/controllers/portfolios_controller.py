from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.users import User
from models.portfolios import Portfolio, portfolio_schema, portfolios_schema
from models.transactions import Transaction
from models.ownedAssets import OwnedAsset
from controllers.auth_controller import authorise_as_admin
from controllers.transactions_controller import update_owned_assets


portfolios_bp = Blueprint("portfolios", __name__, url_prefix="/portfolios")

def refresh_portfolio():
    """
    Functionality: This function updates the holdings information for all portfolios based on the latest transactions. It iterates through each portfolio in the database, calculates the total cost of all transactions associated with that portfolio, and updates the portfolio's holdings to reflect the current total cost. This ensures that the holdings information for each portfolio is up-to-date with the latest financial transactions.

    Input: None. This function does not require any input parameters.
    Output: None. This function does not return any value but updates the database records for portfolios.
        
    Errors: 
    - This function does not explicitly return error messages or status codes since it is intended to run internally within the application. However, errors during database operations (such as committing changes) could raise exceptions that are to be handled by the application's global error handlers.

    Requires:
    - Access to the database session to execute queries and commit changes.

    The function starts by selecting all portfolios from the database. For each portfolio, it retrieves all transactions and owned assets associated with that portfolio ID. It then calculates the total cost of all transactions. If the calculated total cost differs from the portfolio's recorded holdings, the portfolio's holdings are updated to match the calculated total cost. This process ensures the holdings data reflects the actual value based on transactions.

    This function is typically called before performing operations that require up-to-date portfolio information, such as displaying portfolio data to the user or calculating performance metrics. It does not directly interact with users or return data to them but plays a critical role in maintaining data integrity within the application.
    """

    # Attempts to retrieve all portfolios from the database
    stmt = db.select(Portfolio)
    portfolios = db.session.scalars(stmt).all()

    # If portfolios exist
    if portfolios:
        # For each portfolio in portfolios
        for portfolio in portfolios:
            # stmt2 retrieves all transactions that belond to the current portfolio and assigns it to transactions variable
            stmt2 = db.select(Transaction).filter_by(portfolioID=portfolio.portfolioID)
            transactions = db.session.scalars(stmt2).all()

            # stmt 3 retrieves all owned assets that belond to the current portfolio and assigns it to ownedAssets variable
            stmt3 = db.select(OwnedAsset).filter_by(portfolioID=portfolio.portfolioID)
            ownedAssets = db.session.scalars(stmt3).all()

            # Total_cost variable is to the sum of the total cost all transactions belonging to that portfolio
            total_cost = sum(transaction.totalCost for transaction in transactions)

            # If total_cost variable differs from portfolio holdings
            if portfolio.holdings != total_cost:
                # Update portfolio holdings to correct value of total_cost
                portfolio.holdings=total_cost
                db.session.commit()


# Retrieve all portfolios from portfolios table in database
@portfolios_bp.route("/") # /portfolios
@jwt_required()
@authorise_as_admin()
def get_all_portfolios():
    """
    Endpoint: GET /portfolios

    Functionality: Retrieves a list of all portfolios from the portfolios table in the database, after updating the portfolios based on the latest transactions and asset ownership. This endpoint is protected by JWT authentication and further restricted to users with administrative privileges through the @authorise_as_admin() decorator. It ensures that sensitive portfolio data is only accessible by authorized personnel.

    Input: None. The request does not require any input data, but it does require an authenticated user with administrative rights.
    Output: A JSON array containing details of all portfolios in the system, ordered by 'portfolioID', or a message indicating no portfolios were found.
        
    Errors: 
    - Returns a 403 Forbidden error message and status code if the JWT token is missing, invalid, or does not belong to an administrative user, preventing access to portfolio data.
    - Returns a 404 Not Found error message and status code if no portfolios are found in the database.

    Requires:
    - A valid JWT token in the Authorization header, indicating that the requester is logged in.
    - Administrative privileges verified by the @authorise_as_admin() decorator to ensure that only users with the appropriate level of access can retrieve the list of all portfolios.

    The function first invokes the refresh_portfolio() method to update portfolios based on the latest transactions and asset ownership. It then initiates a database query to select all entries from the 'portfolios' table, ordering them by 'portfolioID' for organized retrieval. The results are serialized into JSON format and returned to the requester, providing a comprehensive view of all investment portfolios managed within the system. If no portfolios are found, a message is returned to indicate this.
    """

    # Check for changes in owned assets and transactions and update the portfolio
    refresh_portfolio()

    # Retrieve all portfolios in the db and order by portfolioID
    stmt = db.select(Portfolio).order_by(Portfolio.portfolioID)
    portfolios = db.session.execute(stmt).scalars().all() 

    if portfolios:
        # Return the portfolios
        return portfolios_schema.dump(portfolios), 200
    else:
        # Return error no portfolios found
        return {"error": "No portfolios found"}, 404


# Retrieve portfolio by portfolioID
@portfolios_bp.route("/search/<int:portfolio_id>", methods=["GET"]) #   /portfolios/search/<portfolio_id>
@jwt_required()
def search_for_portfolio(portfolio_id):
    """
    Endpoint: GET /portfolios/search/<int:portfolio_id>

    Functionality: Retrieves the details of a specific portfolio identified by portfolio_id. This endpoint requires JWT authentication and ensures that only the portfolio's owner or an administrative user can access the portfolio details, maintaining privacy and security.

    Input: Portfolio ID as part of the URL path.
    Output: JSON object containing the details of the requested portfolio with 200 success response.
    
    Errors: 
    - Returns a 403 Forbidden error message and status code if the requester is neither the owner of the portfolio nor an admin, indicating unauthorized access attempt.
    - Returns a 404 Not Found error message and status code if the specified portfolio does not exist, indicating the portfolio ID provided does not match any portfolio in the database.

    Requires:
    - JWT token in the Authorization header to authenticate the request.
    - `portfolio_id` parameter in the URL path specifying which portfolio's details are being requested.
    """

    # Check for changes in owned assets and transactions and update the portfolio
    refresh_portfolio()

    # Attempt to retrieve the portfolio ID in db by ID given
    stmt = db.select(Portfolio).filter_by(portfolioID=portfolio_id)
    portfolio = db.session.scalar(stmt)

    # find the currently logged in User
    current_user = User.query.filter_by(userID=get_jwt_identity()).first()

    # If portfolio exists
    if portfolio:
        # Verify if the current user is authorized to retrieve the portfolio (either owns it or is an admin)
        if portfolio.userID != current_user.userID and not current_user.is_admin:
            # Unauthorized action - return error response
            return {"error": "Not authorised to perform this action"}, 403
        # Else if user owns portfolio or is an admin
        else:
            # Return portfolio
            return portfolio_schema.dump(portfolio), 200
    # Else if portfolio does not exists
    else:
        # Return error response
        return {"error" : f"Portfolio with id '{portfolio_id}' not found"}, 404


# Create new portfolio in portfolios table
@portfolios_bp.route("/create", methods=["POST"]) # /portfolios/create
@jwt_required()
def create_portfolio():
    """
    Endpoint: POST /portfolios/create

    Functionality: This endpoint facilitates the creation of a new portfolio in the portfolios table. It first checks if the currently logged-in user already has a portfolio and restricts users to having only one portfolio. If no existing portfolio is found for the user, it proceeds to create a new portfolio using the provided details and associates it with the user's account.

    Input: JSON object containing 'name' and 'description' for the new portfolio. The 'date' is automatically set to the current date, and 'userID' is derived from the JWT token of the authenticated request.
    Output: JSON object of the newly created portfolio, including the portfolio's ID, name, description, creation date, and the user ID, and HTTP status code 201 (Created).

    Errors: 
    - Returns a 403 Forbidden error message and status code if the user already has a portfolio, indicating that each user is only allowed one portfolio.
    - Utilizes the `portfolio_schema` for validating the input data, which may return errors for missing or invalid fields.

    Requires:
    - JWT token in the Authorization header to authenticate the request and identify the user.
    """

    # Check the db to see if the currently logged in user allready has a portfolio
    stmt = db.select(Portfolio).filter_by(userID=get_jwt_identity())
    existing_portfolio = db.session.scalar(stmt)

    # If portfolio exists
    if existing_portfolio:
        # Return error
        return {"error": f"User '{existing_portfolio.userID}' is not allowed to create more than one portfolio, user '{existing_portfolio.userID}' allready has a portfolio called '{existing_portfolio.name}'."}, 403
    # Retrieve body data from JSON in portfolio_schema format
    data = portfolio_schema.load(request.get_json())
    # Create new portfolio model instance
    portfolio = Portfolio(
        name=data.get("name"),
        description=data.get("description"),
        date=date.today(),
        userID=get_jwt_identity()
    )
    # Add portfolio instance to the session and commit
    db.session.add(portfolio)
    db.session.commit()
    # Return newly created portfolio
    return portfolio_schema.dump(portfolio), 201


# Update a portfolio in portfolios table
@portfolios_bp.route("/update/<int:portfolio_id>", methods=["PUT","PATCH"]) #   /portfolios/update/<portfolio_id>
@jwt_required()
def update_portfolio(portfolio_id):
    """
    Endpoint: PUT/PATCH /portfolios/update/int:portfolio_id

    Functionality: This endpoint handles the updating of specific fields within a portfolio in the database. It ensures that the request comes from an authorized user (either the owner of the portfolio or an administrator) before proceeding with the update. Upon successful update, it returns the updated portfolio data.

    Input: Portfolio ID as part of the URL path and JSON object containing the fields to be updated ('name', 'description').
    Output: JSON object of the updated portfolio data, reflecting the changes made.
    
    Errors: 
    - Returns a 403 Forbidden error message and status code if the user attempting the update is neither the portfolio owner nor an administrator.
    - Returns a 404 Not Found error message and status code if the specified portfolio does not exist.

    Requires:
    - JWT token in the Authorization header to authenticate the request.
    - `portfolio_id` parameter in the URL path specifying the portfolio to be updated.
    - Optional JSON fields in the request body for 'name' and 'description', where provided values will overwrite existing ones.

    Notes:
    - This endpoint uses both PUT and PATCH methods to support full and partial updates respectively.
    """

    # Retrieve body data from JSON
    data = portfolio_schema.load(request.get_json())

    # Attmept to retrieve the portfolio from database whose fields need to be updated
    stmt = db.select(Portfolio).filter_by(portfolioID=portfolio_id)
    portfolio = db.session.scalar(stmt)

    # Retrieve the currently logged in user
    current_user = User.query.filter_by(userID=get_jwt_identity()).first()

    # Ensure the portfolio exists
    if portfolio:
        # Verify if the current user is authorized to delete the portfolio (either owns it or is an admin)
        if portfolio.userID != current_user.userID and not current_user.is_admin:
            # Unauthorized action - return error response
            return {"error": "Only the portfolio owner or an admin can edit the requested portfolio"}, 403
        # Else if current user owns the portfolio or is an admin
        else:
            # Update the fields
            portfolio.name=data.get("name") or portfolio.name,
            portfolio.description=data.get("description") or portfolio.description
            # commit the changes
            db.session.commit()
            # Return the updated portfolio back
            return portfolio_schema.dump(portfolio), 200
    # Else
    else:
        # Return error msg
        return {"error": f"Portfolio with id '{portfolio_id}' not found"}, 404
    

# Delete a portfolio from portfolios table
@portfolios_bp.route("/delete/<int:portfolio_id>", methods=["DELETE"]) #    /portfolios/delete/<portfolio_id>
@jwt_required()
def delete_portfolio(portfolio_id):
    """
    Endpoint: DELETE /portfolios/delete/int:portfolio_id

    Functionality: This endpoint handles the deletion of a specific portfolio from the database. It checks the current user's authorization to ensure they are the owner of the portfolio or an administrator before proceeding with the deletion. Upon successful deletion, it returns a confirmation message.

    Input: Portfolio ID as part of the URL path.
    Output: JSON object with a message confirming the deletion of the portfolio, and HTTP status code 200 (OK) for successful deletion or 403 (Forbidden) and 404 (Not Found) for errors.
    
    Errors: 
    - Returns a 403 Forbidden error message and status code if the user attempting the deletion is neither the portfolio owner nor an administrator.
    - Returns a 404 Not Found error message and status code if the specified portfolio does not exist.

    Requires:
    - JWT token in the Authorization header to authenticate the request.
    - `portfolio_id` parameter in the URL path specifying the portfolio to be deleted.
    """

    # Attempt to retrieve the portfolio to be deleted
    stmt = db.select(Portfolio).filter_by(portfolioID=portfolio_id)
    portfolio = db.session.scalar(stmt)

    # Retrieve the currently logged in user
    current_user = User.query.filter_by(userID=get_jwt_identity()).first()

    # Ensure the portfolio exists
    if portfolio:
        # Verify if the current user is authorized to delete the portfolio (either owns it or is an admin)
        if (portfolio.userID != current_user.userID and not current_user.is_admin):
            # Unauthorized action - return error response
            return {"error": "Only the portfolio owner or an admin can delete the requested portfolio"}, 403
        # Else if current user owns the portfolio or is an admin
        else:
            # Delete portfolio, save changes to database
            db.session.delete(portfolio)
            db.session.commit()
            # Return success response
            return {"message": f"Portfolio '{portfolio.name}' with portfolio ID '{portfolio.portfolioID}' has successfully been deleted."}, 200
    # Else if portfolio does not exist
    else:
        # Return error response
        return {"error": f"Portfolio with ID '{portfolio_id}' not found."}, 404