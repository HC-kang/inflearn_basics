from morning_car import MorningCar
from porsche_car import PorscheCar

class User:
    def __init__(self, car_name) -> None:
        if car_name == 'morning':
            self.car = MorningCar()
        elif car_name == 'porsche':
            self.car = PorscheCar()
    
    def drive(self) -> None:
        self.car.accelerate()