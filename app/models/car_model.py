from app.services import read_json, write_json
from app.services.car_service import car_already_parked, spot_already_parked
from app.exceptions.car_exc import CarAlreadyParkedError, SpotAlreadyParkedError

class Car:
    DATABASE_FILEPATH = "parking_lot.json"

    def __init__(self, plate: str, company: str, model: str, color: str, spot: str):
        self.plate = plate
        self.company = company
        self.model = model
        self.color = color
        self.spot = spot

    @classmethod
    def get_cars(cls):
        return read_json(cls.DATABASE_FILEPATH)


    def add_car(self):
        if car_already_parked(self.DATABASE_FILEPATH, self.plate):
            raise CarAlreadyParkedError

        if spot_already_parked(self.DATABASE_FILEPATH, self.spot):
            raise SpotAlreadyParkedError

        return write_json(self.DATABASE_FILEPATH, self.__dict__)
