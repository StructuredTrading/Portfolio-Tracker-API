from init import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    transactionID = db.Column(db.Integer, primary_key=True)
    transactionType = db.Column(db.String(100), nullable=False, default="buy")
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"))
    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"))

    portfolio = db.relationship("Portfolio", back_populates="transaction")
    asset = db.relationship("Asset", back_populates="transaction")