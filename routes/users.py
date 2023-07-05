from flask import Blueprint, request, jsonify
from utils.db import db
from models.users import User

users = Blueprint('users',__name__)

 
@users.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        users = User.query.all()
        list_users = [user.as_dict() for user in users]
        return jsonify(list_users), 200
    
    if request.method == 'POST':
        request_body = request.json
        if type(request_body) != dict or "user_name" not in request_body or "email" not in request_body:
            errors = {
                "add_error": "The request body must be an object with at least 'user_name' and 'email' properties."
            }
            return jsonify(errors), 400
        else:
            new_user = User(
                  user_name=request_body["user_name"],
                  email=request_body["email"]
                )
            db.session.add(new_user)
            db.session.commit()
            users = User.query.all()
            list_users = [user.as_dict() for user in users]
            return jsonify(list_users), 200



@users.route('/users/<users_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(users_id):
    user = User.query.get(users_id)
    if user is None:
        errors = {
          "get_error": f"User with the ID '{users_id}' doesn't exist."
        }
        return jsonify(errors), 404
    else:
        if request.method == 'GET':
            user_dict = user.as_dict()
            return jsonify(user_dict), 200
        
        if request.method == 'PUT':
            request_body = request.json

            user_dict = user.as_dict()
            user_dict.update(request_body)
            
            user.user_name = user_dict["user_name"]
            user.email = user_dict["email"]
            db.session.commit()

            users = User.query.get(users_id)
            users_dict = users.as_dict()
            return jsonify(users_dict), 200
        
        if request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()

            users = User.query.all()
            list_users = [user.as_dict() for user in users]
            return jsonify(list_users), 200