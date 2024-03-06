from init import db

class Asset(db.Model):
    __tablename__ = "assets"

    assetID = db.Column(db.String, primary_key=True)
    symbol = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)