from utils.db import db

class Favorite_vehicle(db.Model):
    __tablename__ = 'favorites_vehicles'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vehicles_uid = db.Column(db.Integer, db.ForeignKey('vehicles.uid'))

    def __repr__(self):
        return f'<Favorites_vehicles {self.id}>'