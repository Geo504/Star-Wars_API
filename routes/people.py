from flask import Blueprint, request, jsonify
from utils.db import db
from models.people import People

people = Blueprint('people',__name__)

 
@people.route("/people", methods=['GET', 'POST'])
def get_people():
    if request.method == 'GET':
        people = People.query.all()
        list_people = [person.as_dict() for person in people]
        return jsonify(list_people), 200
    
    if request.method == 'POST':
        request_body = request.json
        if type(request_body) != dict or "name" not in request_body or "gender" not in request_body:
            errors = {
                "add_error": "The request body must be an object with at least 'name' and 'gender' properties."
            }
            return jsonify(errors), 400
        else:
            new_person = People(
                name=request_body["name"],
                gender=request_body["gender"]
                )
            db.session.add(new_person)
            db.session.commit()
            people = People.query.all()
            list_people = [person.as_dict() for person in people]
            return jsonify(list_people), 200



@people.route('/people/<person_uid>', methods=['GET', 'PUT', 'DELETE'])
def get_person(person_uid):
    person = People.query.get(person_uid)
    if person is None:
        errors = {
            "get_error": f"Character with the UID '{person_uid}' doesn't exist."
        }
        return jsonify(errors), 400
    else:
        if request.method == 'GET':
            person_dict = person.as_dict()
            return jsonify(person_dict), 200
        
        if request.method == 'PUT':
            request_body = request.json

            person_dict = person.as_dict()
            person_dict.update(request_body)
            
            person.name = person_dict["name"]
            person.gender = person_dict["gender"]
            db.session.commit()

            people = People.query.get(person_uid)
            people_dict = people.as_dict()
            return jsonify(people_dict), 200
        
        if request.method == 'DELETE':
            db.session.delete(person)
            db.session.commit()

            people = People.query.all()
            list_people = [person.as_dict() for person in people]
            return jsonify(list_people), 200