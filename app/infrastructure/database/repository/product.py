from typing import Optional

from app.application.interfaces.user_repository import AbstractRepository
from app.domain.user import Product
from app.infrastructure.database.orm import ProductModel


class ProductRepository(AbstractRepository):
    def create(self, model: Product) -> Product:
        ...

    def find_one(self, model: Product) -> Product:
        ...

    def find_by_id(self, product_id: int) -> Optional[Product]:
        product = ProductModel.select().where(ProductModel.id == product_id).first()
        if product:
            return Product(id=product.id, name=product.name, price=product.price)
        return None
