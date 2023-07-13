from flask import Blueprint, request, jsonify

from models.planets import Planets
from controllers.planets_controller import get_planets, post_planet, get_planet, put_planet, delete_planet

planets = Blueprint('planets',__name__)


@planets.route("/api/planets/", methods=['GET', 'POST'])
def index():
    if request.method =='GET':
        return get_planets()
    
    if request.method =='POST':
        if type(request.json) != dict or "name" not in request.json or "diameter" not in request.json:
            errors = {
                "add_error": "The request body must be an object with at least 'name' and 'diameter' properties."
            }
            return jsonify(errors), 400
        else:
            return post_planet()



@planets.route('/api/planets/uid/<planet_uid>', methods=['GET', 'PUT', 'DELETE'])
def index_planet(planet_uid):
    planet = Planets.query.get(planet_uid)
    if planet is None:
        errors = {
            "get_error": f"Planet with the UID '{planet_uid}' doesn't exist."
        }
        return jsonify(errors), 404
    else:
        if request.method == 'GET':
            return get_planet(planet)
        
        if request.method == 'PUT':
            return put_planet(planet)
        
        if request.method == 'DELETE':
            return delete_planet(planet)