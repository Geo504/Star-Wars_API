from flask import Blueprint, request

from controllers.auth_controller import login


auth = Blueprint('auth',__name__)

@auth.route('/api/auth/login', methods=['POST'])
def login_routes():
    return login()