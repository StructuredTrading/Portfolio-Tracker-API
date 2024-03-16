from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.transactions import Transaction, transactions_schema, transaction_schema
from models.assets import Asset
from models.ownedAssets import OwnedAsset
from models.portfolios import Portfolio
from models.users import User
from controllers.assets_controller import update_asset_prices
from controllers.auth_controller import authorise_as_admin


transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


def update_owned_assets(transaction):
    """
    Functionality: Updates or adds an owned asset in a portfolio following a transaction. This function checks if the asset involved in the transaction already exists in the user's portfolio. If it does, it updates the quantity and recalculates the average price. If not, it creates a new OwnedAsset record.

    Input: A Transaction object that contains the details of the recent transaction, including the assetID, portfolioID, quantity, and price.
    Output: None. This function updates or creates entries in the OwnedAsset table of the database but does not return any direct output.

    Errors:
    - This function does not directly return error messages or status codes since it operates within the context of a larger operation (creating or updating a transaction). However, database operation failures (such as integrity constraints violations) would raise exceptions that would be caught and handled by the global error handlers.
    """

    # Retrieve ownedAsset instance that matches asset in transaction and portfolioID
    stmt = db.select(OwnedAsset).filter_by(portfolioID=transaction.portfolioID).filter_by(assetID=transaction.assetID)
    ownedAsset = db.session.scalar(stmt)

    # If ownedAsset exists, update the new quantity and AvgPrice
    if ownedAsset:
        new_quantity = ownedAsset.quantity + transaction.quantity
        ownedAsset.price=(ownedAsset.price + transaction.price / new_quantity),
        ownedAsset.quantity=new_quantity

    # else add new asset to ownedAssets belonging to portfolioID
    else:
        # Retrieve Asset instance that matches assetID in transaction
        stmt = db.select(Asset).filter_by(assetID=transaction.assetID)
        asset = db.session.scalar(stmt)
        # Retrieve Portfolio instance that matches portfolioID in transaction
        stmt = db.select(Portfolio).filter_by(portfolioID=transaction.portfolioID)
        portfolio = db.session.scalar(stmt)

        # Create new instance of OwnedAsset with transaction, Asset and Portfolio details 
        new_owned_asset = OwnedAsset(
            symbol=asset.symbol,
            name=asset.name,
            quantity=transaction.quantity,
            price=transaction.price,
            asset=asset,
            portfolio=portfolio
        )
        # Add new instance to database
        db.session.add(new_owned_asset)
    # Commit changes to database
    db.session.commit()


@transactions_bp.route("/")
@authorise_as_admin()
def retrieve_all_transactions():
    """
    Endpoint: GET /transactions

    Functionality: Retrieves a comprehensive list of all transactions across all portfolios, accessible exclusively to users with administrative privileges. This endpoint offers a detailed overview of transaction activities, including transaction types, quantities, prices, and associations with specific assets and portfolios.

    Input: None. No input parameters are required for this request.
    Output: A JSON array containing the details of all transactions, provided transactions exist within the database.

    Errors:
    - Returns a 403 Forbidden error if the requester does not have administrative privileges, ensuring sensitive transaction data is safeguarded.
    - Returns a 404 Not Found error if no transactions are present within the database.

    Requires:
    - A valid JWT token in the Authorization header to authenticate the request, ensuring that the requester possesses administrative privileges. The @authorise_as_admin() decorator enforces this requirement, restricting access to this sensitive endpoint to authorized administrative users only.
    """

    # Execute query to retrieve all transactions from the database
    stmt = db.select(Transaction)
    transactions = db.session.execute(stmt).scalars().all()

    # If transactions are found in the database
    if transactions:
        # Serialize and return the list of transactions as JSON
        return transactions_schema.dump(transactions), 200
    # If no transactions are found
    else:
        # Return an error message indicating no transactions were found
        return  {"error": "No transactions found"}, 404


@transactions_bp.route("/search/<int:transaction_id>")
@jwt_required()
def search_transactions_by_id(transaction_id):
    """
    Endpoint: GET /transactions/search/<int:transaction_id>

    Functionality: Retrieves details of a specific transaction by its ID. This endpoint ensures that transactions can only be viewed by their owners or an administrative user. It requires JWT authentication to verify the user's identity and authorization to access the transaction details.

    Input: Transaction ID as part of the URL path.
    Output: JSON object containing the details of the requested transaction and HTTP status code 200 (OK) for successful retrieval.

    Errors:
    - Returns a 403 Forbidden error message and status code if the user attempting to access the transaction details is neither the owner of the transaction nor an administrative user.
    - Returns a 404 Not Found error message and status code if the specified transaction ID does not exist in the database.

    Requires:
    - A valid JWT token in the Authorization header to authenticate the request.
    - The transaction ID in the URL path to specify which transaction's details are to be retrieved.
     """

    # Attempt to find transaction by transaction ID
    transaction = Transaction.query.filter_by(transactionID=transaction_id).first()

    # If transaction exists
    if transaction:
        # Currently logged in user
        current_user = User.query.filter_by(userID=get_jwt_identity()).first()

        # attempt to find the currently logged in user's portfolio
        current_user_portfolioID = Portfolio.query.filter_by(userID=get_jwt_identity()).first()

        # If current user is an admin or the current user is the owner of the transaction
        if current_user.is_admin or current_user_portfolioID and transaction.portfolioID == current_user_portfolioID.portfolioID:
            # Return the transaction
            return transaction_schema.dump(transaction), 200
        # Else if the user is not authorised to view the transaction
        else:
            # Return error
            return {"error": "Not Authorised to view transaction"}, 403
    
    # Else if transaction does not exist
    else:
        # Return error response
        return {"error": "Transaction not found"}, 404


@transactions_bp.route("/trade", methods=["POST"])
@jwt_required()
def create_trade():
    """
    Endpoint: POST /transactions/trade

    Functionality: This endpoint facilitates the creation of a new transaction for the current user's portfolio. It verifies the user's portfolio existence, checks the specified asset's existence, and records the transaction with details such as type, quantity, price, and total cost.

    Input: JSON object containing 'transactionType', 'quantity', 'assetID'. The 'transactionType' should be a string (e.g., "buy" or "sell"), 'quantity' an integer representing the number of assets transacted, and 'assetID' a string identifier for the asset involved in the transaction.

    Output: JSON object of the created transaction, including transaction details, and HTTP status code 201 (Created) for successful transactions.

    Errors: 
    - Returns a 404 Not Found error message and status code if the specified asset ID does not exist.
    - Returns a 403 Forbidden error message and status code if the current user does not have an associated portfolio, indicating that the user must create a portfolio before creating transactions.

    Requires:
    - A valid JWT token in the Authorization header, indicating that the requester is logged in and authorized to create transactions.
    """

    # sets current user variable to currently logged in user
    current_user = get_jwt_identity()

    # Attempts to find a portfolio for the current user
    stmt = db.select(Portfolio).filter_by(userID=current_user)
    portfolio = db.session.scalar(stmt)

    # If the current user has a portfolio
    if portfolio:
        # load data from json body
        data = transaction_schema.load(request.get_json())

        # Attempt to retrieve asset from list of assets
        stmt = db.select(Asset).filter_by(assetID=data.get("assetID"))
        asset = db.session.scalar(stmt)

        # If asset exists
        if asset:
            # Update asset prices
            update_asset_prices()

            # Create a new transaction
            new_transaction = Transaction(
                transactionType=data.get("transactionType"),
                quantity=data.get("quantity"),
                price=asset.price,
                totalCost=asset.price * int(data.get("quantity")),
                date=date.today(),
                assetID=data.get("assetID"),
                portfolioID=portfolio.portfolioID
            )

            # Add the new transaction to the database and commit
            db.session.add(new_transaction)
            db.session.commit()

            # Update owned assets to reflect new changes
            update_owned_assets(new_transaction)

            # Return the new transaction details
            return transaction_schema.dump(new_transaction), 201

        # Else if asset does not exist
        else:
            # Return error response for asset not found
            return {"error": "Asset id not found."}, 404
    else:
        return {"error": "You must create a portfolio first"}, 403