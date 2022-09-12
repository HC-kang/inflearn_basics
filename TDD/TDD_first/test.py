import requests
import pytest


def login(user_id: str, user_password: str) -> str:
    user_repository = UserRepository()
    user = user_repository.find_by_id(user_id)
    if user_id == user.id and user.password == user_password:
        return create_token(user_id)
    else:
        raise Exception("로그인 인증에 실패했습니다.")


def create_token(user_id: str) -> str:
    return user_id + "_verified"


# --------------------------------------------------
def test_login_endpoint():
    # given
    api_host = "http://localhost:8000"
    payload = {"id": "ford", "password": "1234"}

    # when
    res = requests.post(url=f"{api_host}/login", json=payload)

    # then
    assert res.data() == {"token": "ford_verified"}


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
    user_password = "wrong_password"

    # when && then
    with pytest.raises(Exception):
        login(user_id, user_password)


def test_create_token():
    actual = create_token("ford")
    expected = "ford_verified"
    assert actual == expected
