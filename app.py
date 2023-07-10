from dotenv import load_dotenv
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


from models.users_favorites import User_favorite
from routes.api import api
from utils.db import db

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
