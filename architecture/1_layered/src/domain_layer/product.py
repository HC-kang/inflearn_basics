"""
도메인 레이어는 도메인의 내용들을 표현.
"""

from sqlalchemy import Column, String, Integer

# DB와 연결하는 일은 인프라스트럭처 레이어에서의 일입니다.
from src.infrastructure_layer.database import Base

# 도메인 레이어의 컴포넌트(Product)는 인프라스트럭쳐 레이어의 컴포넌트(Base)에 의존합니다.
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
