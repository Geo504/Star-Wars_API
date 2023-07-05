from flask import Blueprint

from .users import users
from .people import people
from .planets import planets
from .vehicles import vehicles

api = Blueprint('api',__name__)

api.register_blueprint(users)
api.register_blueprint(people)
api.register_blueprint(planets)
api.register_blueprint(vehicles)