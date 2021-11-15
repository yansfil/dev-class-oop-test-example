from app.application.interfaces.user_repository import AbstractRepository


class ProductService:
    def __init__(self, product_repository: AbstractRepository):
        self.product_repository = product_repository

    def get_product(self, product_id: int):
        product = self.product_repository.find_by_id(product_id)
        return product
