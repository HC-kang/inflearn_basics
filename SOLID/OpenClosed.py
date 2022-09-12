# AS-IS


class Developer:
    def coding(self):
        print("코딩")


class Designer:
    def design(self):
        print("디자인")


class Analyst:
    def analyze(self):
        print("분석")


class Company:
    def __init__(self, employees):
        self.employees = employees

    # employ가 다양해질수록 코드를 계속 변경해야 함
    def make_work(self):
        for employee in self.employees:
            if type(employee) == Developer:
                employee.coding()
            elif type(employee) == Designer:
                employee.design()
            elif type(employee) == Analyst:
                employee.analyze()


from abc import ABC, abstractmethod
from typing import List

# TO-BE

# 각 객체들의 역할을 아우르는 추상 클래스(고수준)을 생성
class Employee(ABC):
    @abstractmethod
    def word(self):
        ...


class Developer(Employee):
    def work(self):
        print("코딩")


class Designer(Employee):
    def work(self):
        print("디자인")


class Analyst(Employee):
    def work(self):
        print("분석")


class Manager(Employee):
    def work(self):
        print("매니징")


class Company:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    # employee가 늘어나도 변경에는 닫혀있다.
    def make_work(self):
        for employee in self.employees:
            employee.work()
