from flask import Blueprint

from init import db
from models.ownedAssets import OwnedAsset, ownedAssets_schema

ownedAssets_bp = Blueprint("ownedAssets", __name__, url_prefix="/assets/owned")


@ownedAssets_bp.route("/")
def retrieve_owned_assetts():
    stmt = db.select(OwnedAsset)
    assets = db.session.execute(stmt).scalars().all()
    return ownedAssets_schema.dump(assets)