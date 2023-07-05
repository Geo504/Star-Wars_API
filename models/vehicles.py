from utils.db import db
import uuid

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    uid = db.Column(db.Integer,primary_key=True)
    id = db.Column(db.String(80), unique=True)
    model = db.Column(db.String(50), nullable=False)
    max_speed = db.Column(db.Integer, nullable=False)
    # length = db.Column(db.Integer, nullable=False)
    # cargo_capacity = db.Column(db.Integer, nullable=False)
    # crew = db.Column(db.Integer, nullable=False)
    

    def __init__(self, model, max_speed):
        self.id = str(uuid.uuid4())
        self.model = model
        self.max_speed = max_speed
        # self.length = length
        # self.cargo_capacity = cargo_capacity
        # self.crew = crew
    
    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}