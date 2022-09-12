import pytest


class UserRepository:
    def __init__(self):
        self.users = {
            "ford": {"id": "ford", "password": "1234"},
            "king": {"id": "king", "password": "1234"},
            "moka": {"id": "moka", "password": "1234"},
            "sherry": {"id": "sherry", "password": "1234"},
            "mark": {"id": "mark", "password": "1234"},
        }

    def find_by_id(self, user_id):
        try:
            return self.users[user_id]
        except:
            raise Exception("유저를 찾지 못했습니다.")


def create_token(user_id):
    return user_id + "_verified"


def login(user_id: str, user_password: str) -> str:
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    if user["id"] == user_id and user["password"] == user_password:
        return create_token(user_id)
    else:
        raise Exception("로그인 인증에 실패했습니다.")


def test_login_successful():
    # given
    user_id = "ford"
    user_password = "1234"

    # when
    actual = login(user_id, user_password)

    # then
    assert actual == "ford_verified"


def test_login_failed():
    # given
    user_id = "ford"
    user_password = "wrong password"

    # when & then
    with pytest.raises(Exception):
        login(user_id, user_password)
