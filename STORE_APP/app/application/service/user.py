from app.domain.entity import User
from app.application.interface.user_repository import AbstractRepository


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create_user(self, user_name: str):
        _user = User(name=user_name)
        user = self.repository.create(_user)

        return user
