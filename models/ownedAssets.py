from init import db, ma

class OwnedAsset(db.Model):
    __tablename__ = "ownedAssets"

    ID = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    # Foreign keys
    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"), nullable=False)
    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"), nullable=False)

    # Relationship of table setup
    asset = db.relationship("Asset", back_populates="ownedAssets")
    portfolio = db.relationship("Portfolio", back_populates="ownedAssets")


class OwnedAssetSchema(ma.Schema):

    class Meta:
        fields = ('ID', 'symbol', 'name', 'quantity', 'price', 'totalCost', 'assetID', 'portfolioID')

ownedAsset_schema = OwnedAssetSchema()
ownedAssets_schema = OwnedAssetSchema(many=True)