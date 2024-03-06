from init import db

class Transaction(db.Model):
    __tablename__ = "transactions"

    transactionID = db.Column(db.Integer, primary_key=True)
    transactionType = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"))
    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"))