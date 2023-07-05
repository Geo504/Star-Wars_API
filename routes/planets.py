from flask import Blueprint, request, jsonify, redirect
from utils.db import db
from models.planets import Planets

planets = Blueprint('planets',__name__)


@planets.route("/planets", methods=['GET', 'POST'])
def get_people():
    if request.method =='GET':
        planets = Planets.query.all()
        list_planets = [planet.as_dict() for planet in planets]
        return jsonify(list_planets), 200
    
    if request.method =='POST':
        request_body = request.json
        if type(request_body) != dict or "name" not in request_body or "diameter" not in request_body:
            errors = {
                "add_error": "The request body must be an object with at least 'name' and 'diameter' properties."
            }
            return jsonify(errors), 400
        else:
            new_planets = Planets(
                name=request_body["name"],
                diameter=request_body["diameter"]
                )
            db.session.add(new_planets)
            db.session.commit()
            planets = Planets.query.all()
            list_planets = [planet.as_dict() for planet in planets]
            return jsonify(list_planets), 200



@planets.route('/planets/<planet_uid>', methods=['GET', 'PUT', 'DELETE'])
def get_planet(planet_uid):
    planet = Planets.query.get(planet_uid)
    if planet is None:
        errors = {
            "get_error": f"Planet with the ID '{planet_uid}' doesn't exist."
        }
        return jsonify(errors), 404
    else:
        if request.method == 'GET':
            planet_dict = planet.as_dict()
            return jsonify(planet_dict), 200
        
        if request.method == 'PUT':
            request_body = request.json

            planet_dict = planet.as_dict()
            planet_dict.update(request_body)
            
            planet.name = planet_dict["name"]
            planet.gender = planet_dict["diameter"] 
            db.session.commit()

            planet = Planets.query.get(planet_uid)
            planet_dict = planet.as_dict()
            return jsonify(planet_dict), 200
        
        if request.method == 'DELETE':
            db.session.delete(planet)
            db.session.commit()

            planets = Planets.query.all()
            list_planets = [planet.as_dict() for planet in planets]
            return jsonify(list_planets), 200