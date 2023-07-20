import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate


from models.favorites_people import Favorite_people
from models.favorites_planets import Favorite_planet
from models.favorites_vehicles import Favorite_vehicle
from routes.api import api
from utils.db import db

# static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'front', 'build')

app = Flask(__name__) #, static_folder=static_file_dir
CORS(app)

load_dotenv()

app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(api)

with app.app_context():
    db.create_all()

# @app.route('/')
# @app.route('/<path:path>', methods=['GET'])
# def serve_any_other_file(path='index.html'):
#     response = send_from_directory(static_file_dir, path)
#     return response


if __name__ == "__main__":
    app.run(debug=True)
