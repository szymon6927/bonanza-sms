import datetime
from app import db


class Reviews(db.Model):
    """
    Create reviews table
    """

    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    opinion = db.Column(db.Text)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Clients: {}>".format(self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


