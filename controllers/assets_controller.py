from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.assets import Asset, assets_schema, asset_schema

assets_bp = Blueprint("assets", __name__, url_prefix="/assets")

# Retrieve all available assets
@assets_bp.route("/")
def retrieve_all_assets():
    # Retrieve all assets from the database
    stmt = db.select(Asset)
    assets = db.session.execute(stmt).scalars().all() 
    return assets_schema.dump(assets)