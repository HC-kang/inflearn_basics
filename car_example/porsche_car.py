class PorscheCar:
    def __init__(self):
        self.speed = 0
        self._fuel = 0
        
    def accelerate(self):
        self.speed += 3
    
    def decelerate(self):
        self.speed -= 3