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
    """
    Endpoint: GET /assets/owned/<int:portfolio_id>

    Functionality: Retrieves all assets owned by a specific portfolio. It ensures that the request comes from an authorized user who either owns the portfolio or has administrative rights. This endpoint requires JWT authentication.

    Input: Portfolio ID as part of the URL path, used to identify the specific portfolio whose assets are to be retrieved.
    Output: A JSON list of owned assets belonging to the specified portfolio, and HTTP status code 200 (OK) if successful.

    Errors:
    - Returns a 403 Forbidden error message and status code if the user attempting to access the data is neither the portfolio owner nor an admin.
    - Returns a 404 Not Found error message and status code if no assets are found for the specified portfolio ID.

    Requires:
    - A valid JWT token in the Authorization header to authenticate the request and verify the user's identity and permissions.
    """
    # Attempt to retrieve a list of assets owned by portfolio_id
    owned_assets = OwnedAsset.query.filter_by(portfolioID=portfolio_id).all()

    # If owned_assets exists
    if owned_assets:
        # Attempt to retrieve the portfio of the currently logged in user
        current_user = Portfolio.query.filter_by(userID=get_jwt_identity()).first()
        # Attempt to retrieve the User profile of the currently logged in user
        current_user_ID = User.query.filter_by(userID=get_jwt_identity()).first()

        # If current user is an admin or owns the portfolio containing the assets
        if current_user_ID.is_admin or current_user and current_user.portfolioID == portfolio_id:
            # Return owned assets list
            return ownedAssets_schema.dump(owned_assets), 200
        # Else if current user is not authorised
        else:
            # Return error response
            return {"error": "Not Authorised"}, 403
    # Else if owned_assets does not exist
    else:
        # Return error response
        return {"error": f"Assets with portfolioID '{portfolio_id}' not found"}, 404