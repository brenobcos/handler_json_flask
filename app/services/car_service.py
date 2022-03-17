from turtle import st
from .handler_json import read_json

def car_already_parked(filepath: str, plate:str):
    cars_list = read_json(filepath)

    for car in cars_list:
        if car["plate"] == plate:
            return True
    return False

def spot_already_parked(filepath:str, spot:str):
    cars_list = read_json(filepath)

    #equivale a verificação car_already_parked
    return [car for car in cars_list if car["spot"] == spot]