from morning_car import MorningCar
from user import User


def main():
    print("hello. main function start")
    morning = MorningCar()
    user = User(morning)
    user.drive()
    user.stop()


if __name__ == "__main__":
    main()
