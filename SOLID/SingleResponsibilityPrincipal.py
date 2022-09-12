# AS-IS


class Employee:
    def coding(self):
        print("코딩")

    def design(self):
        print("디자인")

    def analyze(self):
        print("분석")


# TO-BE
class Developer:
    def coding(self):
        print("코딩")


class Designer:
    def design(self):
        print("디자인")


class Analyst:
    def analyze(self):
        print("분석")


# from abc import ABC, abstractmethod

# # appendix
# class Worker(ABC):
#     @abstractmethod
#     def work(self):
#         pass

# class Developer(Worker):
#     def work(self):
#         print('코딩')

# class Designer(Worker):
#     def work(self):
#         print('디자인')

# class Analyst(Worker):
#     def work(self):
#         print('분석')
