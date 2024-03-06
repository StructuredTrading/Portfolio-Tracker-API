from datetime import date

from flask import Blueprint, jsonify

from init import db, bcrypt, cg
from models.users import User
from models.portfolios import Portfolio
from models.assets import Asset
from models.ownedAssets import OwnedAsset
from models.transactions import Transaction


db_commands = Blueprint('db', __name__)

# Create the tables in the database
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created successfully.")

# Drops all tables from the database
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables deleted successfully.")

# Populate the tables in the database
@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
        User(
            email="test@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8")
        )
    ]

    db.session.add_all(users)
    print("Seeding users table.")

    def get_all_assets():
        try:
            # Fetch market data for cryptocurrencies in USD
            # The 'vs_currency' is set to 'usd', and you could adjust the 'per_page' and 'page' parameters as needed
            coins_market = cg.get_coins_markets(vs_currency='usd', per_page=250, page=1)
            print("trying to fetch assets")
            assets = []
            # Extract symbol, name, and price in USD for each cryptocurrency
            unique_coins = ['dYdX']
            for coin in coins_market:
                if 'dydx' not in coin['id'].lower():
                    unique_coins.append(coin['id'])
                    assets.append(
                        {
                            "id": coin['id'],
                            "symbol": coin['symbol'].upper(),
                            "name": coin['name'],
                            "price": coin['current_price']
                        } 
                    )
                else:
                    print(f"Coin id '{coin['id']}' allready added.") 
            
            return assets
        
        except Exception as e:
            return jsonify({"error": str(e)}), 501


    assets = []
    available_assets = get_all_assets()

    for current_asset in available_assets:
        # print(current_asset)
        assets.append(
            Asset(
                assetID=current_asset["id"],
                symbol=current_asset["symbol"],
                name=current_asset["name"],
                price=current_asset["price"]
            )
        )
    
    db.session.add_all(assets)

    portfolio = [
        Portfolio(
            name="Admin Portfolio",
            description="A Portfolio that is owned by Admin.",
            holdings=50000,
            date=date.today(),
            user=users[0] # Foreign Key from users table
        ),
        Portfolio(
            name="Test Portfolio",
            description="A Portfolio that is owned by test account.",
            holdings=1000,
            date=date.today(),
            user=users[1] # Foreign Key from users table
        )
    ]
    db.session.add_all(portfolio)
    print("Seeding portfolio table.")
    db.session.commit()
    print("Successfully seeded all tables in the database.")