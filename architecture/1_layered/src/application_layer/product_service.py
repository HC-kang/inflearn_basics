"""
프레젠테이션 레이어에서 받은 입력을 비즈니스 로직대로 처리.
서비스를 구성하고, 필요에 따라 도메인 모델을 사용함
이후 결과를 프레젠테이션 레이어로 전달.
"""

from src.domain_layer.product import Product
from src.infrastructure_layer.database import db
from src.infrastructure_layer.repositories.product_repository import ProductRepository

def create_product(name: str, price: str) -> bool:
    try:
        product = Product(name, price)
        with db.Session() as session:
            product_repository = ProductRepository(session)
            product_repository.save(product)
            session.commit()
        return product
    except:
        raise Exception("Product Not Created")