import pytest

from app.domain.user import User
from app.infrastructure.database.orm import db, UserModel, ProductModel
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture
def init_database():
    db.init(database=":memory:")  # memory db를 띄우기에 실제 db에 영향을 주지 않음
    db.connect()
    db.create_tables([UserModel])

def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name=name)
    repository = UserRepository()

    created_user = repository.create(_user)
    user = repository.find_one(_user)

    assert user == created_user
