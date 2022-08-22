class Developer:
    name = 'dev'
    def drink_coffee(self):
        print('drink coffee')
        
    def turn_on_computer(self):
        print('turn on computer')
        
    def open_ide(self):
        print('open_ide')


class Company:
    def make_work(self):
        developer = Developer()
        print(f"{developer.name}가 일을 시작합니다.")
        developer.drink_coffee()
        developer.turn_on_computer()
        developer.open_ide();

