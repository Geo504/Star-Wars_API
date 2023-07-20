from utils.db import db

class Favorite_planet(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    people_uid = db.Column(db.Integer, db.ForeignKey('planets.uid'))

    def __repr__(self):
        return f'<Favorites_planets {self.id}>'