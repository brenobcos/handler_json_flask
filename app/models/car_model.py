from app.exceptions import CarAlreadyParkedError, SpotAlreadyParkedError
from app.services import read_json, write_json
from app.services.car_service import (
    car_already_parked,
    spot_already_parked,
    validate_plate,
)


class Car:
    DATABASE_FILEPATH = "parking_lot.json"

    def __init__(self, plate: str, company: str, model: str, color: str, spot: str):
        self.plate = validate_plate(plate)
        self.company = company
        self.model = model
        self.color = color
        self.spot = spot

    @classmethod
    def get_cars(cls):
        return read_json(cls.DATABASE_FILEPATH)

    def add_car(self):
        parked = car_already_parked(self.DATABASE_FILEPATH, self.plate)
        print(f"{parked=}")

        if parked:
            sport_parked = parked[0]
            print(f"{sport_parked=}")

            raise CarAlreadyParkedError(spot=sport_parked, plate=self.plate)

        if spot_already_parked(self.DATABASE_FILEPATH, self.spot):
            raise SpotAlreadyParkedError(spot=self.spot)

        return write_json(self.DATABASE_FILEPATH, self.__dict__)
