from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.people import people
from routes.planets import planets
from routes.vehicles import vehicles
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/starwars_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(people)
app.register_blueprint(planets)
app.register_blueprint(vehicles)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
