from init import db, ma 

class Portfolio(db.Model):
    __tablename__ = "portfolios"

    portfolioID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    holdings = db.Column(db.Float, default=0, nullable=False)
    date = db.Column(db.Date, nullable=False) # Date the portfolio was created.

    userID = db.Column(db.Integer, db.ForeignKey("users.userID"), nullable=False) # Foreign key 'user.UserID' tablename = 'user', key = 'UserID'

    # Relationship of tables setup 
    # name of relational attribute = user | function used to define a relationship = db.relationship() | name of related class = "User" | "portfolio" = the relationship attribute in the related class 'User'
    user = db.relationship("User", back_populates="portfolio")
    transaction = db.relationship("Transaction", back_populates="portfolio", cascade="all, delete")
    ownedasset = db.relationship("OwnedAsset", back_populates="portfolio", cascade="all, delete")