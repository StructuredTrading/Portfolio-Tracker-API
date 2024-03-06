from init import db, ma 

class Portfolio(db.Model):
    __tablename__ = "portfolios"

    portfolioID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    holdings = db.Column(db.Integer)
    date = db.Column(db.Date) # Date the portfolio was created.

    userID = db.Column(db.Integer, db.ForeignKey("users.userID"), nullable=False) # Foreign key 'user.UserID' tablename = 'user', key = 'UserID'

    user = db.relationship("User", back_populates="portfolio")