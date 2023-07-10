from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

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



@users.route('/api/users/token', methods=['POST'])
def create_token():
    if "email" not in request.json or "password" not in request.json:
            return 'missing an "email" or "password" keys in json', 400
    
    email_user = request.json["email"]
    password_user = request.json["password"]

    user = User.query.filter_by(email=email_user).first()
    if user is None:
        return 'User not found', 404
    
    if bcrypt.checkpw(password_user.encode('utf-8'), user.password):
        access_token = create_access_token(identity=email_user)
        return jsonify(access_token=access_token)
    else:
        return 'Wrong password!!'
