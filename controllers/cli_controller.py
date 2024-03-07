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
    print("Seeding assets table.")

    portfolios = [
        Portfolio(
            name="Admin Portfolio",
            description="A Portfolio that is owned by Admin.",
            date=date.today(),
            user=users[0] # set relational attribute "user" in Portfolio instance to relate to the first instance of class 'User' using the variable 'users'
        ),
        Portfolio(
            name="Test Portfolio",
            description="A Portfolio that is owned by test account.",
            date=date.today(),
            user=users[1] # set relational attribute "user" in Portfolio instance to relate to the second instance of class 'User' using the variable 'users'
        )
    ]

    transactions = [
        Transaction(
            transactionType="buy",
            quantity=10,
            price=assets[0].price,
            date=date.today(),
            # assetID=assets[0],
            asset=assets[0],
            # portfolioID=portfolio[0]
            portfolio=portfolios[0]
        ),
        Transaction(
            transactionType="buy",
            quantity=5,
            price=assets[1].price,
            date=date.today(),
            asset=assets[1],
            portfolio=portfolios[0]
        ),
        Transaction(
            transactionType="buy",
            quantity=30,
            price=assets[21].price,
            date=date.today(),
            asset=assets[21],
            portfolio=portfolios[0]
        ),
        Transaction(
            transactionType="buy",
            quantity=1000,
            price=assets[9].price,
            date=date.today(),
            asset=assets[9],
            portfolio=portfolios[0]
        )
    ]

    # adjusting portfolio holdings according to transactions
    portfolios[0].holdings=transactions[0].quantity * transactions[0].price + transactions[1].quantity * transactions[1].price + transactions[2].quantity * transactions[2].price + transactions[3].quantity * transactions[3].price

    db.session.add_all(portfolios)
    print("Seeding portfolios table.")
    db.session.add_all(transactions)
    print("Seeding transactions table.")

    owned_asset = [
        OwnedAsset(
            symbol=assets[0].symbol,
            name=assets[0].name,
            quantity=transactions[0].quantity,
            price=transactions[0].price,
            asset=assets[0],
            portfolio=portfolios[0]
        ),
        OwnedAsset(
            symbol=assets[1].symbol,
            name=assets[1].name,
            quantity=transactions[1].quantity,
            price=transactions[1].price,
            asset=assets[1],
            portfolio=portfolios[0]
        ),
        OwnedAsset(
            symbol=assets[21].symbol,
            name=assets[21].name,
            quantity=transactions[2].quantity,
            price=transactions[2].price,
            asset=assets[21],
            portfolio=portfolios[0]
        ),
        OwnedAsset(
            symbol=assets[9].symbol,
            name=assets[9].name,
            quantity=transactions[3].quantity,
            price=transactions[3].price,
            asset=assets[9],
            portfolio=portfolios[0]
        )
    ]

    db.session.add_all(owned_asset)
    print("Seeding ownedAssets table.")
    db.session.commit()
    print("Successfully seeded all tables in the database.")