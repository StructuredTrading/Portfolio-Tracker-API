from init import db

class Asset(db.Model):
    __tablename__ = "asset"

    assetID = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date = db.Column(db.Date)

    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolio.PortfolioID"))