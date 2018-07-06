import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    """
    Create table for admin users
    """
    __table__name = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(258))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")

        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def as_dict(self):
        return dict(id=self.id, email=self.email)

    def __repr__(self):
        return "<Users: {}>".format(self.email)
