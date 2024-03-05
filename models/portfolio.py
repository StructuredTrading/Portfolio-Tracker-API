from init import db, ma 

class Portfolio(db.Model):
    __tablename__ = "portfolio"

    PortfolioID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    Holdings = db.Column(db.Integer)
    DateCreated = db.Column(db.Date) # Date the portfolio was created.

    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False) # Foreign key 'user.UserID' tablename = 'user', key = 'UserID'