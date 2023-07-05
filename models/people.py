from utils.db import db
import uuid

class People(db.Model):
    __tablename__ = 'peoples'
    uid = db.Column(db.Integer,primary_key=True)
    id = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    # height = db.Column(db.Integer, nullable=False)
    # mass = db.Column(db.Integer, nullable=False)
    # birth_year = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    

    def __init__(self, name, gender):
        self.id = str(uuid.uuid4())
        self.name = name
        self.gender = gender
        # self.height = height
        # self.mass = mass
        # self.birth_year = birth_year
    
    def __repr__(self):
        return f'<People {self.name}>'
    
    def serialize(self):
        return {
            "uid": self.uid,
            "id": self.id,
            "name": self.name,
            "gender": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}