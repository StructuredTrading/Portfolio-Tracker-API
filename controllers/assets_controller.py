from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db, cg
from models.assets import Asset, assets_schema, asset_schema

assets_bp = Blueprint("assets", __name__, url_prefix="/assets")
 

def get_all_assets():
        """
        Functionality: Fetches and returns a list of cryptocurrency assets with their market data including symbol, name, and current price in USD. This function makes an external API call to CoinGecko to retrieve the market data for up to 250 cryptocurrencies, ensuring a comprehensive dataset is obtained.

        Input: None. This function does not require any input parameters as it retrieves data based on predefined settings such as 'vs_currency' set to 'usd'.

        Output: A list of Asset instances, each populated with the 'assetID', 'marketCapPos', 'symbol', 'name', and 'price' of a cryptocurrency. These Asset instances are ready to be processed further, such as being added to a database.

        Errors:
        - Returns a JSON object with an error message and HTTP status code 501 (Not Implemented) if an exception occurs during the fetch process, indicating a problem with the external API call or data processing.
        """
        try:
            # Fetch market data for cryptocurrencies in USD
            coins_market = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
            print("trying to fetch assets")
            assets = []
            # Extract symbol, name, and price in USD for each cryptocurrency
            unique_coins = []  # Use a set to track unique coin IDs
            for coin in coins_market:
                # Check if coin ID is already processed to ensure uniqueness
                if coin not in unique_coins:
                    unique_coins.append(coin['id'])
                    assets.append(
                        Asset(
                            assetID= coin['id'],
                            marketCapPos= coin['market_cap_rank'],
                            symbol= coin['symbol'].upper(),
                            name= coin['name'],
                            price= coin['current_price']
                        ) 
                    )
                else:
                    print(f"Coin id '{coin['id']}' allready added.") 
            
            return assets
        except Exception as e:
            # Handle exceptions by returning an error message and a 501 status code
            return jsonify({"error": str(e)}), 501
        

def update_asset_prices():
    """
    Functionality: Updates the prices and market capitalization positions of all assets listed in the database by fetching the latest market data from CoinGecko. This operation ensures that the asset information in the database reflects the current market conditions accurately.

    Input: None. This operation does not require any input as it affects all assets stored in the database.

    Output: None. While this operation does not return any direct output to the caller, it updates asset records in the database with the latest pricing and market capitalization data.

    Errors: 
    - Potential errors during the process, such as issues with fetching data from CoinGecko or database update failures, are not directly handled by this function. These errors are to be caught and managed by the application's global error handlers.

    Requires:
    - Proper configuration and access to the CoinGecko API, as well as write access to the database where asset records are stored.
    """
    # Retrieve all assets from the database ordered by market cap position
    stmt = db.select(Asset).order_by(Asset.marketCapPos)
    assets = db.session.execute(stmt).scalars().all()

    # Compile asset IDs for data fetch
    asset_ids = [asset.assetID for asset in assets]

    # Fetch updated market data from CoinGecko
    market_data = cg.get_coins_markets(vs_currency='usd', ids=','.join(asset_ids))

    # Map CoinGecko IDs to their market data
    market_data_map = {data['id']: data for data in market_data}

    # Update database records with fetched data
    for asset in assets:
        # Use the mapping to access the market data for each asset
        data = market_data_map.get(asset.assetID)
        if data:
            asset.price = data.get('current_price', asset.price)  # Update price
            asset.marketCapPos = data.get('market_cap_rank', asset.marketCapPos)  # Update market cap position
    # Commit updates to the database
    db.session.commit()
    return


# Retrieve all available assets
@assets_bp.route("/")
def retrieve_all_assets():
    """
    Endpoint: GET /assets

    Functionality: Retrieves a comprehensive list of all available assets from the database, including their symbols, names, current prices, and market capitalization positions. Prior to retrieval, this endpoint updates the price and market cap ranking of each asset to ensure the most current data is provided.

    Input: None. This request does not require any input parameters, making it accessible to anyone seeking information on available assets.

    Output: 
    - A JSON array containing the details of all assets, ordered by their market capitalization position. 
    - HTTP status code 200 (OK) is returned alongside the assets list upon successful retrieval.

    Errors:
    - If no assets are found within the database, the endpoint returns a JSON object with an error message and a 404 Not Found status code.

    Requires:
    - No authentication or specific permissions are required for accessing this endpoint, allowing public access for querying all assets.
    """

    # Call function to update asset prices and market cap positions
    update_asset_prices()

    # Construct query to retrieve all assets, ordered by market cap position
    stmt = db.select(Asset).order_by(Asset.marketCapPos)
    assets = db.session.execute(stmt).scalars().all() 

    # If assets exist in the database
    if assets:
        # Serialize and return the list of assets as JSON
        return assets_schema.dump(assets), 200
    # If no assets are found
    else:
        # Return an error message indicating no assets were found
        return {"error": "No assets found"}, 404


# Retrieve asset by assetID
@assets_bp.route("/search/<asset_id>")
def search_assets(asset_id):
    """
    Endpoint: GET /assets/search/<asset_id>

    Functionality: Searches and retrieves details of a specific asset by its unique assetID from the database. This endpoint provides users with the ability to access detailed information about an individual asset, including its symbol, name, current price, and market capitalization position.

    Input: 
    - `asset_id`: The unique identifier for the asset, passed as part of the URL path. It specifies the asset whose details are to be retrieved.

    Output: 
    - Returns a JSON object containing the detailed information of the requested asset if found.
    - HTTP status code 200 (OK) is returned alongside the asset information upon successful retrieval.

    Errors:
    - If no asset matching the provided `asset_id` exists within the database, the endpoint returns a JSON object with an error message and a 404 Not Found status code.

    Requires:
    - No authentication or specific permissions are required to access this endpoint, making it publicly accessible for querying asset details.
    """

    # Call function to update asset prices and market cap positions
    update_asset_prices()

    # Attempt to find the asset by 'asset_id' in the database
    stmt = db.select(Asset).filter_by(assetID = asset_id)
    asset = db.session.scalar(stmt)
    # If the asset is found
    if asset:
        # Serialize and return the asset's details
        return asset_schema.dump(asset), 200
    # If the asset is not found
    else:
        # Return an error message indicating the asset was not found
        return {"error": "Asset with asset id '{asset_id}' not found"}, 404