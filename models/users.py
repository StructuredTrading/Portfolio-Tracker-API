from init import db,ma

class User(db.Model):
    __tablename__ = "users"

    userID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    portfolio = db.relationship("Portfolio", back_populates="user", uselist=False, cascade="all, delete")

class UserSchema(ma.Schema):

    class Meta:
        fields = ("userID", "email", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)