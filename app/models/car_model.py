from app.services import read_json, write_json

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


    def save_car(self):
        return write_json(self.DATABASE_FILEPATH, self.__dict__)
