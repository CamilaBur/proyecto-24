"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Vehicles
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import json
# from models import Person



app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


# ____________________________________

# GET ANTES DE FLASK

#@app.route('/todos', methods=['GET'])
#def hello_world():
 #   return jsonify(todos)

 #_____________________________________

@app.route('/characters', methods=['GET'])
def personajes():

    allpersoajes = Characters.query.all()
    results = list(map(lambda item: item.serialize(), allpersoajes))

    return jsonify(results), 200

# obteniendo info de un solo personaje:


@app.route('/characters/<int:character_id>', methods=['GET'])
def get_info_personaje(character_id):

    characters = Characters.query.filter_by(id=character_id).first()
    return jsonify(characters.serialize()), 200

# POST ANTES DEL FLASK

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
 #   request_body = request.get_json(force=True)
  #  todos.append(request_body)
   # return jsonify(todos)

#______________________characters__________________________________________


# @app.route('/characters', methods=['POST'])
# def add_new_todo():

#     me = User('admin', 'admin@example.com') 
#     db.session.add(me)
#     db.session.commit()


#     return jsonify(todos)


#_______________favs________________________

# @app.route('/favs', methods=['GET'])
# def handle_favs():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200


# ______________planets_______________________


@app.route('/planets', methods=['GET'])
def planetas():

    allplanetas = Planets.query.all()
    results = list(map(lambda item: item.serialize(), allplanetas))

    return jsonify(results), 200

# obteniendo info de un solo planeta:


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_info_planet(character_id):

    planets = Planets.query.filter_by(id=planet_id).first()
    return jsonify(planets.serialize()), 200

# ________________vehicles_____________________________


@app.route('/vehicles', methods=['GET'])
def vehiculos():

    allvehicles = Vehicles.query.all()
    results = list(map(lambda item: item.serialize(), allvehicles))

    return jsonify(results), 200

# obteniendo info de un solo vehiculo:


@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_info_vehicle(vehicle_id):

    vehicles = Vehicles.query.filter_by(id=vehicle_id).first()
    return jsonify(vehicles.serialize()), 200

# _____________________________________________

@app.route('/user', methods=['POST'])
def add_new_user():
      
        request_body = json.loads(request.data)
        print(request_body)

        user = User.query.filter_by(email=request_body["email"]).first()
        
        if user is  None:
            usuario = User(email=request_body["email"], password=request_body["password"], username=request_body["username"])
        
            db.session.add(usuario)
            db.session.commit()

            return jsonify("ok"), 200

        return jsonify("este email ya esta registrado"), 200
       

        # return jsonify("ok"), 200




@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()

    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()

    user = User.query.filter_by(email=current_user).first()

    response_body = {
        "msg": "ok",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

