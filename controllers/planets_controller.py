from flask import jsonify, request

from utils.db import db
from models.planets import Planets

def get_planets():
    planets = Planets.query.all()
    planets_list = [planet.as_dict() for planet in planets]
    return jsonify(planets_list), 200


def post_planet():
    new_planet = Planets(**request.json)
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(new_planet.as_dict()), 200


def get_planet(planet):
    return jsonify(planet.as_dict()), 200


def put_planet(planet):
    planet_dict = planet.as_dict()
    planet_dict.update(request.json)
    
    planet.name = planet_dict["name"]
    planet.diameter = planet_dict["diameter"]
    db.session.commit()

    updated_planet = Planets.query.get(planet.uid)
    return jsonify(updated_planet.as_dict()), 200


def delete_planet(planet):
    db.session.delete(planet)
    db.session.commit()

    planets = Planets.query.all()
    list_planets = [planet.as_dict() for planet in planets]
    return jsonify(list_planets), 200