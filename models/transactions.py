from init import db, ma
from marshmallow import fields
from marshmallow.validate import OneOf, Range

VALID_TRANSACTIONS = ("buy", "sell")

class Transaction(db.Model):
    __tablename__ = "transactions"

    transactionID = db.Column(db.Integer, primary_key=True)
    transactionType = db.Column(db.String(100), nullable=False, default="buy")
    quantity = db.Column(db.Integer, nullable=False)
    # price = db.Column(Numeric(precision=18, scale=8), nullable=False)
    price = db.Column(db.Float, nullable=False)
    totalCost = db.Column(db.Float, nullable=False)
    # cost = db.Column(Numeric(precision=12, scale=2), nullable=False)
    date = db.Column(db.Date, nullable=False)

    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"))
    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"))

    portfolio = db.relationship("Portfolio", back_populates="transaction")
    asset = db.relationship("Asset", back_populates="transaction")



class Transaction_Schema(ma.Schema):

    class Meta:

        fields = ("transactionID", "transactionType", "quantity", "price", "totalCost", "date", "portfolioID", "assetID")

    transactionType = fields.String(validate=OneOf(VALID_TRANSACTIONS))
    quantity = fields.Integer(validate=Range(min=1))
    assetID = fields.String()

    # email = fields.Email()
    # password = ma.String(validate=validate.Length(min=6))

transaction_schema = Transaction_Schema()
transactions_schema = Transaction_Schema(many=True)