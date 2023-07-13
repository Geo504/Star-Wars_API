from flask import Blueprint

from .users import users
from .people import people
from .planets import planets
from .vehicles import vehicles
from .auth import auth

api = Blueprint('api',__name__)

api.register_blueprint(users)
api.register_blueprint(people)
api.register_blueprint(planets)
api.register_blueprint(vehicles)
api.register_blueprint(auth)