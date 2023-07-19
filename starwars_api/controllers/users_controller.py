from flask import jsonify, request
import bcrypt

from utils.db import db
from models.users import User
from models.people import People
# from models.planets import Planets
# from models.vehicles import Vehicles


def post_user():
    user_username = request.json.get('user_name')
    user_email = request.json.get('email')
    user_password = request.json.get('password')
    user_favorites = request.json.get('favorites')
    favorites_db = []

    for favorite in user_favorites:
        favorite = db.session.get(People, favorite)
        if favorite:
            favorites_db.append(favorite)
    
    new_user = User(
        user_name = user_username,
        email = user_email,
        password = user_password,
        favorites = favorites_db
    )

    pw_hash = bcrypt.hashpw(new_user.password.encode('utf-8'), bcrypt.gensalt())
    new_user.password = pw_hash

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize_with_favorites()), 201


def update_user(user):
    # user_username = request.json.get('user_name')
    user_favorites = request.json.get('favorites')
    favorites_db = []

    for favorite in user_favorites:
        favorite_person = People.query.filter_by(id=favorite).first()
        # favorite_planet = Planets.query.filter_by(id=favorite).first()
        # favorite_vehicles = Vehicles.query.filter_by(id=favorite).first()
        
        if favorite_person:
            favorites_db.append(favorite_person)
        # if favorite_planet:
        #     favorites_db.append(favorite_planet)
        # if favorite_vehicles:
        #     favorites_db.append(favorite_vehicles)
    
    user_db = User.query.get(user["id"])
    # user_db.user_name = user_username
    user_db.favorites = favorites_db
    db.session.commit()

    updated_user = User.query.get(user_db.id)
    return updated_user.serialize_with_favorites()


def delete_user(user):
    db.session.delete(User.query.get(user["id"]))
    db.session.commit()

    users = User.query.all()
    list_users = [user.serialize_with_favorites() for user in users]
    return jsonify(list_users), 200