"""
클라이언트에게 입력을 받고, 이를 앱 서비스가 활용 할 수 있는 형태로 바꾸어 전달.
반대로, 앱 서비스에서 제공한 결과를 클라이언트에게 http통신으로 반환.
"""

from fastapi import FastAPI
from src.presentation_layer.web import app
from src.application_layer import product_service
        
@app.post("/products", status_code=200)
def register_products(json_req) -> None:
    product = product_service.create_product(name=json_req.name, price=json_req.price)
    response = {
        "product": product
    }
    return response
