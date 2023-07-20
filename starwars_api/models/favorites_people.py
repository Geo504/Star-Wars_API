from utils.db import db

class Favorite_people(db.Model):
    __tablename__ = 'favorites_peoples'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    people_uid = db.Column(db.Integer, db.ForeignKey('peoples.uid'))

    def __repr__(self):
        return f'<Favorites_peoples {self.id}>'