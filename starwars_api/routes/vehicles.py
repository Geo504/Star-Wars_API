from flask import Blueprint, request, jsonify

from models.vehicles import Vehicles
from controllers.vehicles_controller import get_vehicles, post_vehicle, get_vehicle, put_vehicle, delete_vehicle

vehicles = Blueprint('vehicles',__name__)

@vehicles.route("/api/vehicles/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return get_vehicles()
    
    if request.method == 'POST':
        if type(request.json) != dict or "model" not in request.json or "max_speed" not in request.json:
            errors = {
                "add_error": "The request body must be an object with at least 'model' and 'max_speed' properties."
            }
            return jsonify(errors), 400
        else:
            return post_vehicle()



@vehicles.route('/api/vehicles/uid/<vehicle_uid>', methods=['GET', 'PUT', 'DELETE'])
def index_vehicle(vehicle_uid):
    vehicle = Vehicles.query.get(vehicle_uid)
    if vehicle is None:
        errors = {
            "get_error": f"Vehicle with the UID '{vehicle_uid}' doesn't exist."
        }
        return jsonify(errors), 404
    else:
        if request.method == 'GET':
            return get_vehicle(vehicle)
        
        if request.method == 'PUT':
            return put_vehicle(vehicle)
        
        if request.method == 'DELETE':
            return delete_vehicle(vehicle)