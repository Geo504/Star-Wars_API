from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
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
        refresh_token = create_refresh_token(identity=user.serialize_with_favorites())
        return jsonify(refresh_token=refresh_token)
    else:
        return 'Wrong password!!', 401
