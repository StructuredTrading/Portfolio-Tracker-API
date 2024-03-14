from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.transactions import Transaction, transactions_schema, transaction_schema
from models.assets import Asset
from models.ownedAssets import OwnedAsset
from models.portfolios import Portfolio
from controllers.assets_controller import update_asset_prices
# from controllers.auth_controller import authorised_user


transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


def update_owned_assets(transaction):
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
def retrieve_all_transactions():
    stmt = db.select(Transaction)
    transactions = db.session.execute(stmt).scalars().all()
    return transactions_schema.dump(transactions)


@transactions_bp.route("/search/<int:transaction_id>")
def search_transactions_by_id(transaction_id):
    stmt = db.select(Transaction).filter_by(transactionID=transaction_id)
    transaction = db.session.execute(stmt).scalars().all()
    return transactions_schema.dump(transaction)


@transactions_bp.route("/trade", methods=["POST"])
@jwt_required()
def create_trade():
    current_user = get_jwt_identity()
    stmt = db.select(Portfolio).filter_by(userID=current_user)
    portfolio = db.session.scalar(stmt)
    # If currently logged in user has a portfolio
    if portfolio:
        # Retrieve data from json body
        data = transaction_schema.load(request.get_json())
        # Attempt to retrieve asset from list of assets
        stmt = db.select(Asset).filter_by(assetID=data.get("assetID"))
        asset = db.session.scalar(stmt)
        # assets = db.session.execute(stmt).scalars().all()
        if asset:
            update_asset_prices()
            new_transaction = Transaction(
                transactionType=data.get("transactionType"),
                quantity=data.get("quantity"),
                price=asset.price,
                totalCost=asset.price * int(data.get("quantity")),
                date=date.today(),
                assetID=data.get("assetID"),
                portfolioID=portfolio.portfolioID # this will get the user identity NOT the portfolio identity
            )
            db.session.add(new_transaction)
            db.session.commit()
            update_owned_assets(new_transaction)
            return transaction_schema.dump(new_transaction)#{"message": "Asset found."}

        else:
            return {"error": "Asset id not found."}