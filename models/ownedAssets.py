from init import db

class OwnedAsset(db.Model):
    __tablename__ = "ownedAssets"

    ID = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"))
    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"))