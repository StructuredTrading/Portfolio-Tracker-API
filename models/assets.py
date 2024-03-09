from marshmallow import fields

from init import db, ma

class Asset(db.Model):
    __tablename__ = "assets"

    assetID = db.Column(db.String, primary_key=True)
    marketCapPos = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    transaction = db.relationship("Transaction", back_populates="asset", cascade="all, delete")
    ownedAssets = db.relationship("OwnedAsset", back_populates="asset", cascade="all,delete")


class Asset_Schema(ma.Schema):

    class Meta:
        fields = ('assetID', 'marketCapPos', 'symbol', 'name', 'price')
        ordered=True

asset_schema = Asset_Schema()
assets_schema = Asset_Schema(many=True)