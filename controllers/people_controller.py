from flask import jsonify, request

from utils.db import db
from models.people import People

def get_people():
    people = People.query.all()
    people_list = [person.serialize_with_users() for person in people]
    return jsonify(people_list), 200


def post_person():
    new_person = People(**request.json)
    db.session.add(new_person)
    db.session.commit()
    return jsonify(new_person.serialize_with_users()), 200


def get_person(person):
    return jsonify(person.serialize_with_users()), 200


def update_person(person):
    person_dict = person.as_dict()
    person_dict.update(request.json)
    
    person.name = person_dict["name"]
    person.gender = person_dict["gender"]
    db.session.commit()

    updated_person = People.query.get(person.uid)
    return jsonify(updated_person.serialize_with_users()), 200


def delete_person(person):
    db.session.delete(person)
    db.session.commit()

    people = People.query.all()
    list_people = [person.serialize_with_users() for person in people]
    return jsonify(list_people), 200