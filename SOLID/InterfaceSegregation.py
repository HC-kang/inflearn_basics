from abc import ABC, abstractmethod

# As-Is


class SmartPhone(ABC):
    @abstractmethod
    def call(self):
        ...

    @abstractmethod
    def send_message(self):
        ...

    @abstractmethod
    def see_youtube(self):
        ...

    @abstractmethod
    def take_picture(self):
        ...


class PhoneWithoutCamera(SmartPhone):
    ...  # take_picture()메소드는 쓸모없어졌다.


# TO-BE


class Telephone(ABC):
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def send_message(self):
        pass


class Camera(ABC):
    @abstractmethod
    def take_picture(self):
        pass


class Application(ABC):
    @abstractmethod
    def see_youtube(self):
        pass


class PhoneWithoutCamera(Telephone, Application):
    pass
