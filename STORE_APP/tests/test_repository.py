import pytest

from app.domain.entity import User, Product
from app.infrastructure.database.orm import ProductModel, db, UserModel
from app.infrastructure.database.repository.user import UserRepository
from app.infrastructure.database.repository.product import ProductRepository


@pytest.fixture
def init_database():
    db.init(database=":memory:")
    db.connect()
    # db.create_tables([UserModel])
    UserModel.create_table()
    ProductModel.create_table()


def test_create_user_repository(init_database):
    name = "ford"
    _user = User(name=name)
    repository = UserRepository()

    created_user = repository.create(_user)
    # user = repository.find_one(_user)

    # assert user == created_user
    assert created_user == _user


def test_create_product_repository(init_database):
    repository = ProductRepository()
    product_id, product_name, product_price = 1, "맥북", 125000
    _product = Product(id=product_id)

    # Product 생성
    ProductModel.create(name=product_name, price=product_price)

    # Product 조회
    product = repository.find_one(model=_product)

    assert (
        product.id == product_id
        and product.name == product_name
        and product.price == product_price
    )
