from init import db

class User(db.Model):
    __tablename__ = "Users"

    UserID = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String, nullable=False, unique=True)
    Password = db.Column(db.String, nullable=False)
