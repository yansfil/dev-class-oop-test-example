from fastapi import HTTPException

from app.application.services.product import ProductService
from app.infrastructure.database.repository.product import ProductRepository


def find_product(product_id: int):
    product_service = ProductService(product_repository=ProductRepository())
    try:
        product = product_service.get_product(product_id=product_id)
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
