from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db, cg
from models.assets import Asset, assets_schema, asset_schema

assets_bp = Blueprint("assets", __name__, url_prefix="/assets")
 

@assets_bp.route("/update")    
def update_asset_prices():

    stmt = db.select(Asset).order_by(Asset.marketCapPos)
    assets = db.session.execute(stmt).scalars().all()

    asset_ids = [asset.assetID for asset in assets]

    # # Fetch current prices for all assets in one go, replace 'usd'

    # Use /coins/markets endpoint to fetch market data including market cap rank
    market_data = cg.get_coins_markets(vs_currency='usd', ids=','.join(asset_ids))

    # Create a dictionary mapping CoinGecko IDs to their market data for easier access
    market_data_map = {data['id']: data for data in market_data}

    for asset in assets:
        # Use the mapping to access the market data for each asset
        data = market_data_map.get(asset.assetID)
        if data:
            asset.price = data.get('current_price', asset.price)  # Update price
            asset.marketCapPos = data.get('market_cap_rank', asset.marketCapPos)  # Update market cap position
            # asset.price = prices.get(asset.assetID, {}).get('usd', asset.price)
            # asset.marketCapPos = prices.get('market_cap_rank') 
    # Commit the updated prices to the database
    db.session.commit()
   
    return assets_schema.dump(assets) #jsonify(updated_assets_info)


# Retrieve all available assets
@assets_bp.route("/")
def retrieve_all_assets():
    # Update asset prices and marketCapPos before retrieving
    update_asset_prices()
    # Retrieve all assets from the database
    stmt = db.select(Asset).order_by(Asset.marketCapPos)
    assets = db.session.execute(stmt).scalars().all() 
    return assets_schema.dump(assets)


# Retrieve asset by assetID
@assets_bp.route("/search/<asset_id>")
def search_assets(asset_id):
    # retrieve asset with 'asset_id' from the database
    stmt = db.select(Asset).filter_by(assetID = asset_id)
    assets = db.session.scalar(stmt)
    return asset_schema.dump(assets)