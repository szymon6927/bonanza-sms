import datetime
from app import db


class Content(db.Model):
    """
    Create content table
    """

    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    chef_desc = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Content: {}>".format(self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
