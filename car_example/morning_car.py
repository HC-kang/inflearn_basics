from car import Car


class MorningCar(Car):
    def __init__(self) -> None:
        print("---morning: ready---")
        self.speed = 0
        self._fuel = 0

    def accelerate(self) -> None:
        print("---morning: speed up---")
        self.speed += 1

    def decelerate(self) -> None:
        print("---morning: slowdown---")
        self.speed -= 1
