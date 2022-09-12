class Developer:
    name = "dev"

    def develop(self):
        self.drink_coffee()
        self.turn_on_computer()
        self.open_ide()

    def drink_coffee(self):
        print("drink coffee")

    def turn_on_computer(self):
        print("turn on computer")

    def open_ide(self):
        print("open_ide")


class Company:
    def make_work(self):
        developer = Developer()
        developer.develop()
