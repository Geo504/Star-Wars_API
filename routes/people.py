from flask import Blueprint, request, jsonify

from models.people import People
from controllers.people_controller import get_people, post_person, get_person, update_person, delete_person

people = Blueprint('people',__name__)
 
@people.route("/api/people/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return get_people()
    
    if request.method == 'POST':
        if type(request.json) != dict or "name" not in request.json or "gender" not in request.json:
            errors = {
                "add_error": "The request body must be an object with at least 'name' and 'gender' properties."
            }
            return jsonify(errors), 400
        else:
            return post_person()



@people.route('/api/people/uid/<person_uid>', methods=['GET', 'PUT', 'DELETE'])
def index_person(person_uid):
    person = People.query.get(person_uid)
    if person is None:
        errors = {
            "get_error": f"Character with the UID '{person_uid}' doesn't exist."
        }
        return jsonify(errors), 404
    else:
        if request.method == 'GET':
            return get_person(person)
        
        if request.method == 'PUT':
            return update_person(person)
        
        if request.method == 'DELETE':
            return delete_person(person)