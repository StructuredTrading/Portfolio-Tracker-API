from flask import Blueprint

from init import db
from models.ownedAssets import OwnedAsset, ownedAssets_schema
# from models.transactions import Transaction

ownedAssets_bp = Blueprint("ownedAssets", __name__, url_prefix="/assets/owned")

# def refresh_owned_assets():
#     stmt = db.select(Transaction)
#     transactions = db.session.scalars(stmt).all()
#     portfolio_ids = [id.portfolioID for id in portfolio_ids]
#     for transaction in
    # *** UP TO HERE ***

    # need add or subtract owned assets every time a asset is traded in transactions table

    # for asset in ownedAssets:
    #     stmt2 = db.select(transactions)

@ownedAssets_bp.route("/")
def retrieve_owned_assetts():
    stmt = db.select(OwnedAsset)
    assets = db.session.execute(stmt).scalars().all()
    return ownedAssets_schema.dump(assets)