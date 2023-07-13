from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
# import bcrypt
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models.users import User
from controllers.users_controller import get_users, post_user, get_user, update_user, delete_user

users = Blueprint('users',__name__)
 
@users.route("/api/users/", methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'GET':
            return get_users()
        
        if request.method == 'POST':
            if "email" not in request.json or "user_name" not in request.json or "password" not in request.json:
                return 'missing an "email", "user_name" or "password" keys in json', 400
            else:
                return post_user()
    except IntegrityError:
        return 'User with that email is already registered', 400
        



@users.route('/api/users/id/<users_id>', methods=['GET', 'PUT', 'DELETE'])
def index_user(users_id):
    user = User.query.get(users_id)
    if user is None:
        return f"User with the ID '{users_id}' doesn't exist.", 404
    else:
        if request.method == 'GET':
            return get_user(user)
        
        if request.method == 'PUT':
            return update_user(user)
        
        if request.method == 'DELETE':
            return delete_user(user)
