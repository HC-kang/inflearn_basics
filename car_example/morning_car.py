class MorningCar:
    def __init__(self) -> None:
        self.speed = 0
        self._fuel = 0
    
    def accelerate(self) -> None:
        self.speed += 1
    
    def decelerate(self) -> None:
        self.speed -= 1