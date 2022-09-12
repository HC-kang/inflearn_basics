from fastapi import HTTPException

from app.infrastructure.database.repository.product import ProductRepository
from app.application.service.product import ProductService


def find_product(product_id: int):
    repository = ProductRepository()
    product_service = ProductService(repository=repository)
    try:
        product = product_service.get_product(product_id=product_id)
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
