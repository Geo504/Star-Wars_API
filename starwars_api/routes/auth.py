from flask import Blueprint, request

from controllers.auth_controller import login, create_token


auth = Blueprint('auth',__name__)

@auth.route('/api/auth/login', methods=['POST'])
def login_routes():
    return login()

@auth.route('/api/auth/singup', methods=['POST'])
def sing_up_routes():
    return create_token()