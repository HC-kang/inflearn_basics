from abc import ABC, abstractmethod


class Job(ABC):
    @abstractmethod
    def do(self) -> None:
        pass
