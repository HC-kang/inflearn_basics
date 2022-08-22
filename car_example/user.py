from morning_car import MorningCar

class User:
    def __init__(self) -> None:
        self.car = MorningCar()
    
    def drive(self) -> None:
        self.car.accelerate()