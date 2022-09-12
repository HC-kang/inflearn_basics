from app.domain.entity import User
from app.application.interface.repository import AbstractRepository


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create_user(self, user_name: str):
        _user = User(name=user_name)
        # DB에 해당 이름과 같은 이름이 있는지 확인하고, 있으면 예외처리
        if self.repository.find_one(model=_user):
            raise ValueError("유저가 이미 존재합니다.")
        user = self.repository.create(_user)

        return user
