from init import db,ma
from marshmallow import fields, validate

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
    email = fields.Email()
    password = ma.String(validate=validate.Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)