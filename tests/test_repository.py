import pytest

from app.domain.user import User
from app.infrastructure.database.orm import db, UserModel, ProductModel
from app.infrastructure.database.repository.product import ProductRepository
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture(scope="session")
def init_database():
    db.init(database=":memory:")  # memory db를 띄우기에 실제 db에 영향을 주지 않음
    db.connect()
    db.create_tables([UserModel, ProductModel])


def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name=name)
    repository = UserRepository()

    created_user = repository.create(_user)
    user = repository.find_one(_user)

    assert user == created_user


def test_find_product_repository(init_database):
    _product = ProductModel(name="맥북", price=1000000)
    _product.save()

    repository = ProductRepository()

    product = repository.find_by_id(product_id=_product.id)
    assert product.id == _product.id and product.name == _product.name
