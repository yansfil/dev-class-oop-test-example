import pytest
from starlette.testclient import TestClient

from app.infrastructure.database.orm import db, UserModel, ProductModel
from app.infrastructure.fastapi.main import create_app

app = create_app()

@pytest.fixture
def init_database(tmpdir):
    db.init(database=f"{tmpdir}/test.db")  # fastapi testclient에서 memory db 이용에 문제가 있음.
    db.connect()
    db.create_tables([UserModel, ProductModel])
    yield db
    db.drop_tables([UserModel, ProductModel])




@pytest.fixture
def fastapi_client(init_database):
    return TestClient(app=app)


def test_get_product_api(fastapi_client):
    with fastapi_client as client:
        product_id = 1
        # Product 미리 생성해두기
        ProductModel.bulk_create(
            [
                ProductModel(name="키보드", price=30000),
            ]
        )

        result = client.get(f"/products/{product_id}").json()

        assert result == {"id": 1, "name": "키보드", "price": 30000}

