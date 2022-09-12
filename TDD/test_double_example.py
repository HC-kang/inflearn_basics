# AS-IS
from typing import Dict, Optional


def login(user_id: str, user_password: str) -> str:
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    if user.id == user_id and user.password == user_password:
        return create_token(user_id)
    else:
        raise Exception("로그인 인증에 실패했습니다.")


# TO-BE
class User:
    pass


class Repository:
    def __init__(self):
        pass


class FakeRepository(Repository):
    "DB를 이용하지 않고, 인메모리로 데이터를 저장하고 불러냄."

    def __init__(self, data: Dict[str, User]) -> None:
        self._data = data

    def find_by_id(self, id: str) -> Optional[User]:
        return self._data.get(id, None)


def create_token(user_id: str) -> str:
    return user_id + "_verified"


def login(user_id: str, user_password: str, repository: Repository) -> str:
    user = repository.find_by_id(user_id)
    if user_id == user["id"] and user["password"] == user_password:
        return create_token(user_id)
    else:
        raise Exception("로그인 인증에 실패했습니다.")


def test_login_successful():
    # given
    repository = FakeRepository(data={"ford": {"id": "ford", "password": "1234"}})
    user_id = "ford"
    user_password = "1234"

    # when
    actual = login(user_id, user_password, repository)

    # then
    assert actual == "ford_verified"
