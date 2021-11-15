import uvicorn
from fastapi import FastAPI

from app.controller.product import find_product
from app.infrastructure.database.orm import db, UserModel, ProductModel
from app.controller.user import signup

def create_app():
    app = FastAPI()
    app.add_api_route(
        path="/user",
        methods=['POST'],
        endpoint=signup,
    )
    app.add_api_route(
        path="/products/{product_id}",
        methods=['GET'],
        endpoint=find_product,
    )
    return app

def initialize_db():
    db.init(database="database.db")
    db.connect()

    UserModel.create_table()
    ProductModel.create_table()

if __name__ == "__main__":
    initialize_db()
    app = create_app()

    uvicorn.run(app, host="0.0.0.0", port=8000)

# 실행 스크립트
# python -m uvicorn app.infrastructure.fastapi.main:app --port 8000 --reload

