import datetime
from app import db


class Clients(db.Model):
    """
    Create clients table
    """

    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Clients: {}>".format(self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


