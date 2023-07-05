from flask import Blueprint, request, jsonify
from utils.db import db
from models.vehicles import Vehicles

vehicles = Blueprint('vehicles',__name__)

@vehicles.route("/vehicles", methods=['GET', 'POST'])
def get_vehicles():
    if request.method == 'GET':
        vehicles = Vehicles.query.all()
        list_vehicles = [vehicle.as_dict() for vehicle in vehicles]
        return jsonify(list_vehicles), 200
    
    if request.method == 'POST':
        request_body = request.json
        if type(request_body) != dict or "model" not in request_body or "max_speed" not in request_body:
            errors = {
                "add_error": "The request body must be an object with at least 'model' and 'max_speed' properties."
            }
            return jsonify(errors), 400
        else:
            new_vehicle = Vehicles(
                model=request_body["model"],
                max_speed=request_body["max_speed"]
                )
            db.session.add(new_vehicle)
            db.session.commit()
            vehicles = Vehicles.query.all()
            list_vehicles = [vehicle.as_dict() for vehicle in vehicles]
            return jsonify(list_vehicles), 200



@vehicles.route('/vehicles/<vehicle_uid>', methods=['GET', 'PUT', 'DELETE'])
def get_vehicle(vehicle_uid):
    vehicle = Vehicles.query.get(vehicle_uid)
    if vehicle is None:
        errors = {
            "get_error": f"Vehicle with the UID '{vehicle_uid}' doesn't exist."
        }
        return jsonify(errors), 404
    else:
        if request.method == 'GET':
            vehicle_dict = vehicle.as_dict()
            return jsonify(vehicle_dict), 200
        
        if request.method == 'PUT':
            request_body = request.json

            vehicle_dict = vehicle.as_dict()
            vehicle_dict.update(request_body)
            
            vehicle.model = vehicle_dict["model"]
            vehicle.max_speed = vehicle_dict["max_speed"]
            db.session.commit()

            vehicle = vehicle.query.get(vehicle_uid)
            vehicle_dict = vehicle.as_dict()
            return jsonify(vehicle_dict), 200
        
        if request.method == 'DELETE':
            db.session.delete(vehicle)
            db.session.commit()

            vehicles = Vehicles.query.all()
            list_vehicles = [vehicle.as_dict() for vehicle in vehicles]
            return jsonify(list_vehicles), 200