class MorningCar:
    def __init__(self, fuel: int) -> None:
        self.speed = 0
        self._current_fuel = fuel
        self._max_fuel = 50
        if fuel > self._max_fuel:
            raise Exception(f"최대로 넣을 수 있는 연료는 {self._max_fuel}L 입니다.")
        print("연료량:", self._current_fuel)

    def accelerate(self) -> None:
        if self._current_fuel == 0:
            raise Exception("남아있는 연료가 없습니다.")
        self._current_fuel -= 1
        self.speed += 1
        print("연료량:", self._current_fuel)

    def decelerate(self) -> None:
        if self._current_fuel == 0:
            raise Exception("남아있는 연료가 없습니다.")
        self._current_fuel -= 1
        self.speed -= 1
        print("연료량:", self._current_fuel)

    def refuel(self, fuel: int) -> None:
        if self._current_fuel + fuel > self._max_fuel:
            raise Exception(
                f"추가로 더 넣을 수 있는 최대 연료는 {self._max_fuel - self._current_fuel}L 입니다."
            )
        self._current_fuel += fuel
        print("연료량:", self._current_fuel)

    def get_current_fuel_percentage(self) -> str:
        return f"{self._current_fuel / self._max_fuel * 100}"


car = MorningCar(30)

car.accelerate()
car.accelerate()
car.accelerate()
car.refuel(30)
print(f"{car._current_fuel / car._max_fuel * 100}%")  # 54%
