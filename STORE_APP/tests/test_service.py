import pytest

from app.application.service.user import UserService
from app.domain.entity import User
from fakes import FakeUserRepository


@pytest.fixture
def user_service():
    repository = FakeUserRepository(users=[])

    user_service = UserService(repository=repository)
    return user_service


def test_create_user_well(user_service):
    user_name = "ford"

    user = user_service.create_user(user_name=user_name)

    assert user == User(name=user_name)


def test_create_user_duplicated(user_service):
    user_name = "ford"

    user_service.create_user(user_name=user_name)

    # 중복가입하는 경우
    with pytest.raises(ValueError):
        user_service.create_user(user_name=user_name)
