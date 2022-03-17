from http import HTTPStatus

from flask import Flask, jsonify, request

from app.exceptions import (
    CarAlreadyParkedError,
    InvalidPlateError,
    SpotAlreadyParkedError,
)
from app.models.car_model import Car
from app.services import read_json, write_json

app = Flask(__name__)

FILEPATH = "parking_lot.json"


@app.get("/cars")
def retrieve():
    # return jsonify(read_json(FILEPATH)), HTTPStatus.OK
    return jsonify(Car.get_cars()), HTTPStatus.OK


@app.post("/cars")
def create():
    data = request.get_json()

    # return write_json(FILEPATH, data) , HTTPStatus.CREATED
    try:
        car = Car(**data)
        return car.add_car(), HTTPStatus.CREATED
    except InvalidPlateError as e:
        return {"error": e.message}, e.status_code
    except CarAlreadyParkedError as e:
        # return {"error": f"Plate {car.plate} already parked"}, HTTPStatus.CONFLICT
        return {"error": e.message}, e.status_code
    except SpotAlreadyParkedError as e:
        return {"error": e.message}, e.status_code
