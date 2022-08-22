from car import Car

class PorscheCar(Car):
    def __init__(self):
        print('---Porsche: Ready---')
        self.speed = 0
        self._fuel = 0
        
    def accelerate(self):
        print('---Porsche: speed up!---')
        self.speed += 3
    
    def decelerate(self):
        print('---Porsche: slowdown---')
        self.speed -= 3