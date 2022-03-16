from flask import Flask, jsonify, request
from http import HTTPStatus
from app.services import read_json, write_json
from app.models.car_model import Car


app = Flask(__name__)

FILEPATH = "parking_lot.json"

@app.get("/cars")
def retrieve():
    # return jsonify(read_json(FILEPATH)), HTTPStatus.OK
    return jsonify(Car.get_cars()), HTTPStatus.OK

@app.post("/cars")
def create():
    data = request.get_json()
    car = Car(**data)

    # return write_json(FILEPATH, data) , HTTPStatus.CREATED
    return car.save_car(), HTTPStatus.CREATED
