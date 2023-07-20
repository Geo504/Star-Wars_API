from utils.db import db
import uuid

class Planets(db.Model):
    __tablename__ = 'planets'
    uid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.String(30), nullable=False)
    population = db.Column(db.String(30), nullable=False)
    terrain = db.Column(db.String(80), nullable=False)
    climate = db.Column(db.String(80), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    description = db. Column(db.String(320), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    

    def __init__(self, name, diameter, population, terrain, climate, surface_water, description, image):
        self.id = str(uuid.uuid4())
        self.name = name
        self.diameter = diameter
        self.population = population
        self.terrain = terrain
        self.climate = climate
        self.surface_water = surface_water
        self.description = description
        self.image = image

    def __repr__(self):
        return f'<Planet {self.name}>'
    
    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
    
    def serialize_with_users(self):
        return {
            "uid": self.uid,
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "surface_water": self.surface_water,
            "description": self.description,
            "image": self.image,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "users": [user.serialize() for user in self.users]
        }