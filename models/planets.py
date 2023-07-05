from utils.db import db
import uuid

class Planets(db.Model):
    __tablename__ = 'planets'
    uid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(50), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    # population = db.Column(db.Integer, nullable=False)
    # terrain = db.Column(db.String(80), nullable=False)
    # climate = db.Column(db.String(80), nullable=False)
    

    def __init__(self, name, diameter):
        self.id = str(uuid.uuid4())
        self.name = name
        self.diameter = diameter
        # self.population = population
        # self.terrain = terrain
        # self.climate = climate
    
    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}