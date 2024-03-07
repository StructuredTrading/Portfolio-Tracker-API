from marshmallow import fields

from init import db, ma

class Asset(db.Model):
    __tablename__ = "assets"

    assetID = db.Column(db.String, primary_key=True)
    symbol = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)

    transaction = db.relationship("Transaction", back_populates="asset", cascade="all, delete")
    ownedasset = db.relationship("OwnedAsset", back_populates="asset", cascade="all,delete")


class Asset_Schema(ma.Schema):

    class Meta:
        fields = ('assetID', 'symbol', 'name', 'price')
        ordered=True

asset_schema = Asset_Schema()
assets_schema = Asset_Schema(many=True)