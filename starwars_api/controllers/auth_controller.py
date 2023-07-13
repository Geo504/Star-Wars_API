from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt

from models.users import User

def login():
    if "email" not in request.json or "password" not in request.json:
      return 'missing an "email" or "password" keys in json', 400
    
    email_user = request.json["email"]
    password_user = request.json["password"]

    user = User.query.filter_by(email=email_user).first()
    if user is None:
        return 'User not found!', 404
    
    if bcrypt.checkpw(password_user.encode('utf-8'), user.password):
        access_token = create_access_token(identity=user.serialize())
        return jsonify(access_token=access_token)
    else:
        return 'Wrong password!!', 401



def create_token():
    if "email" not in request.json or "password" not in request.json:
            return 'missing an "email" or "password" keys in json', 400
    
    email_user = request.json["email"]
    password_user = request.json["password"]

    user = User.query.filter_by(email=email_user).first()
    if user is None:
        return 'User not found!', 404
    
    if bcrypt.checkpw(password_user.encode('utf-8'), user.password):
        access_token = create_access_token(identity=email_user)
        return jsonify(access_token=access_token)
    else:
        return 'Wrong password!!', 401