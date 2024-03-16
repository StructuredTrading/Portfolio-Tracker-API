from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.ownedAssets import OwnedAsset, ownedAssets_schema
from models.portfolios import Portfolio
from models.users import User

ownedAssets_bp = Blueprint("ownedAssets", __name__, url_prefix="/assets/owned")


@ownedAssets_bp.route("/")
def retrieve_owned_assets():
    stmt = db.select(OwnedAsset)
    assets = db.session.execute(stmt).scalars().all()
    return ownedAssets_schema.dump(assets)

@ownedAssets_bp.route("/<int:portfolio_id>")
@jwt_required()
def retrieve_portfolio_assets(portfolio_id):

    # Attempt to retrieve a list of assets owned by portfolio_id
    owned_assets = OwnedAsset.query.filter_by(portfolioID=portfolio_id).all()

    # If owned_assets exists
    if owned_assets:
        # attempt to retrieve the portfio of the currently logged in user
        current_user = Portfolio.query.filter_by(userID=get_jwt_identity()).first()
        # Attempt to retrieve the User profile of the currently logged in user
        current_user_ID = User.query.filter_by(userID=get_jwt_identity()).first()

        # If current user is an admin or owns the portfolio containing the assets
        if current_user_ID.is_admin or current_user and current_user.portfolioID == portfolio_id:
            # Return owned assets list
            return ownedAssets_schema.dump(owned_assets), 200
        # Else if current user is not authorised
        else:
            return {"error": "Not Authorised"}, 403
    else:
        return {"error": f"Assets with portfolioID '{portfolio_id}' not found"}