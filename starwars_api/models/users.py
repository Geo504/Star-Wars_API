from utils.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    user_name = db.Column(db.String(25))
    created_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    favorites_people = db.relationship('People',
                                secondary='favorites_peoples',
                                backref='users',
                                lazy=True)
    favorites_planets = db.relationship('Planets',
                                secondary='favorites_planets',
                                backref='users',
                                lazy=True)
    favorites_vehicles = db.relationship('Vehicles',
                                secondary='favorites_vehicles',
                                backref='users',
                                lazy=True)

    
    def __repr__(self):
        return f'<User {self.email}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def serialize_with_favorites(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "favorites_people": [favorite.as_dict() for favorite in self.favorites_people],
            "favorites_planets": [favorite.as_dict() for favorite in self.favorites_planets],
            "favorites_vehicles": [favorite.as_dict() for favorite in self.favorites_vehicles]
        }