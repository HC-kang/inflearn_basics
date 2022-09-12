class MorningCar:
    def __init__(self, fuel: int) -> None:
        self.speed = 0
        self.current_fuel = fuel
        self.max_fuel = 50
        if fuel > self.max_fuel:
            raise Exception(f"최대 연료는 {self.max_fuel}L 입니다.")
        print("연료량:", self.current_fuel)

    def accelerate(self) -> None:
        if self.current_fuel == 0:
            raise Exception("남아있는 연료가 없습니다.")
        self.speed += 1
        self.current_fuel -= 1
        print("연료량:", self.current_fuel)

    def decelerate(self) -> None:
        if self.current_fuel == 0:
            raise Exception("남아있는 연료가 없습니다.")
        self.speed -= 1
        self.current_fuel -= 1
        print("연료량:", self.current_fuel)


car = MorningCar(30)

car.accelerate()
car.accelerate()
car.accelerate()
car.current_fuel += 50
print(f"{car.current_fuel / car.max_fuel * 100}%")  # 154%
