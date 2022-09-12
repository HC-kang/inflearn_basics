from data_engineer import DataEngineer
from designer import Designer
from job import Job


class User:
    def __init__(self, name: str, job: Job) -> None:
        self.name = name
        self.job = job

    def work(self) -> None:
        self.job.do()


user = User("heechan", DataEngineer())
user.work()

user2 = User("jong", Designer())
user2.work()
