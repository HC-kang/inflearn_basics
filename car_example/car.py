from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def accelerate(self) -> None:
        pass

    @abstractmethod
    def decelerate(self) -> None:
        pass
