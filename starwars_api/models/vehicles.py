from utils.db import db
import uuid

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    uid = db.Column(db.Integer,primary_key=True)
    id = db.Column(db.String(80), unique=True)
    model = db.Column(db.String(50), nullable=False)
    max_speed = db.Column(db.Integer, nullable=False)
    length = db.Column(db.String(50), nullable=False)
    cargo_capacity = db.Column(db.String(50), nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.String(50), nullable=False)
    description = db. Column(db.String(320), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    

    def __init__(self, model, max_speed, length, cargo_capacity, crew, cost, description, image):
        self.id = str(uuid.uuid4())
        self.model = model
        self.max_speed = max_speed
        self.length = length
        self.cargo_capacity = cargo_capacity
        self.crew = crew
        self.cost = cost
        self.description = description
        self.image = image

    def __repr__(self):
        return f'<Vehicle {self.model}>'
    
    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
    
    def serialize_with_users(self):
        return {
            "uid": self.uid,
            "id": self.id,
            "model": self.model,
            "max_speed": self.max_speed,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity,
            "crew": self.crew,
            "cost": self.cost,
            "description": self.description,
            "image": self.image,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "users": [user.serialize() for user in self.users]
        }