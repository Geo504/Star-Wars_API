from flask import jsonify, request

from utils.db import db
from models.vehicles import Vehicles

def get_vehicles():
    vehicles = Vehicles.query.all()
    vehicles_list = [vehicle.serialize_with_users() for vehicle in vehicles]
    return jsonify(vehicles_list), 200


def post_vehicle():
    new_vehicle = Vehicles(**request.json)
    db.session.add(new_vehicle)
    db.session.commit()
    return jsonify(new_vehicle.serialize_with_users()), 200


def get_vehicle(vehicle):
    return jsonify(vehicle.serialize_with_users()), 200


def put_vehicle(vehicle):
    vehicle_dict = vehicle.as_dict()
    vehicle_dict.update(request.json)
    
    vehicle.model = vehicle_dict["model"]
    vehicle.max_speed = vehicle_dict["max_speed"]
    db.session.commit()

    updated_vehicle = Vehicles.query.get(vehicle.uid)
    return jsonify(updated_vehicle.serialize_with_users()), 200


def delete_vehicle(vehicle):
    db.session.delete(vehicle)
    db.session.commit()

    vehicles = Vehicles.query.all()
    list_vehicles = [vehicle.serialize_with_users() for vehicle in vehicles]
    return jsonify(list_vehicles), 200