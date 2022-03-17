from flask import Flask, jsonify, request
from http import HTTPStatus
from app.services import read_json, write_json
from app.models.car_model import Car
from app.exceptions.car_exc import CarAlreadyParkedError, SpotAlreadyParkedError


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
    try:
        return car.add_car(), HTTPStatus.CREATED
    except CarAlreadyParkedError:
        return {"error": f"Plate {car.plate} already parked"}, HTTPStatus.CONFLICT
    except SpotAlreadyParkedError:
        return {"error": f"Spot {car.spot} already parked"}, HTTPStatus.CONFLICT
