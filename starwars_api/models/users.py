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
    favorites = db.relationship('People',
                                secondary='users_favorites',
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
            "favorites": [favorite.as_dict() for favorite in self.favorites]
        }