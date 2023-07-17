from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
# import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.users import User
from controllers.users_controller import post_user, update_user, delete_user

users = Blueprint('users',__name__)
 
@users.route("/api/users/", methods=['POST'])
def index():
    try:
        # if request.method == 'POST':
        if "email" not in request.json or "user_name" not in request.json or "password" not in request.json or "favorites" not in request.json:
            return 'missing an "email", "user_name" or "password" keys in json', 400
        else:
            return post_user()
    except IntegrityError:
        return 'User with that email is already registered', 400
        



@users.route('/api/users/', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def index_user():
    user = get_jwt_identity()
    if user is None:
        return f"User doesn't exist.", 404
    else:
        if request.method == 'GET':
            return jsonify(user)
        
        if request.method == 'PUT':
            return update_user(user)
        
        if request.method == 'DELETE':
            return delete_user(user)
