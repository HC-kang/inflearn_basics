from abc import ABC, abstractmethod

# Bad 1

class Employee(ABC):
    @abstractmethod
    def work(self):
        ...


class Developer(Employee):
    def work(self):
        print('코딩')
        return ["if..", "for..."]


class FrontEndDeveloper(Developer):
    def work(self):
        print('프론트엔드 개발')
        # no return

if __name__ == "__main__":
    def make_code(developer: Developer):
        code = developer.work()
        print(f"총 {len(code)} 줄의 코드를 작성하였습니다.")
        
    make_code(Developer())
    make_code(FrontEndDeveloper())


# Bad 2

class Rectangle:
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height


if __name__ == "__main__":
    square = Square()
    square.set_width(20)
    square.set_height(30)

    check = square.get_width() == 20 and square.get_height() ==30