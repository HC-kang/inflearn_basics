from car import Car


class User:
    def __init__(self, car: Car) -> None:
        self.car = car

    def drive(self) -> None:
        print("User: driving start")
        self.car.accelerate()

    def stop(self) -> None:
        print("User: Stop")
        self.car.decelerate()
