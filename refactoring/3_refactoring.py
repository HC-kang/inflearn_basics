# 1번. 다른 Store 추가 시?
# 개선점
# 1. store를 추상화
# 2. 의존성을 주입

# 2번. Store에 있는 상품과 돈에 User가 마음대로 접근
# 개선점
# 1. Store의 책임을 정의하고 캡슐화
# 2. User의 결제 로직을 수정한다.
# 3. User도 캡슐화 하자.

from abc import ABC, abstractmethod


class Store(ABC):
    @abstractmethod
    def __init__(self, products):
        self._money = 0
        self.name = ''
        self._products = products
    
    @abstractmethod
    def show_product(self, product_id):
        pass
    
    @abstractmethod
    def give_product(self, product_id):
        pass
    
    @abstractmethod
    def take_money(self, money):
        pass
    

class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = '그랩마켓'
        self._products = products
        # self._products = {
        #     1: {'name': '키보드', 'price': 30_000},
        #     2: {'name': '모니터', 'price': 50_000},
        # }
    
    def set_money(self, money):
        self._money = money
    
    def set_products(self, products):
        self._products = products
    
    def show_product(self, product_id):
        return self._products[product_id]

    def give_product(self, product_id):
        self._products.pop(product_id)
    
    def take_money(self, money):
        self._money += money
    
    
class FruitStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = '과일마켓'
        self._products = products
        # self._products = {
        #     1: {'name': '바나나', 'price': 3_000},
        #     2: {'name': '사과', 'price': 5_000},
        # }
    
    def set_money(self, money):
        self._money = money
    
    def set_products(self, products):
        self._products = products
    
    def show_product(self, product_id):
        return self._products[product_id]

    def give_product(self, product_id):
        self._products.pop(product_id)
    
    def take_money(self, money):
        self._money += money


class User:
    def __init__(self, money, store: Store):
        self.money = money
        self.store = store
        self.belongs = []
    
    def get_money(self):
        return self.money
    
    def get_belongs(self):
        return self.belongs
    
    def get_store(self):
        return self.store
    
    def see_product(self, product_id):
        product = self.store.show_product(product_id=product_id)
        return product
    
    def purchase_product(self, product_id):
        product = self.see_product(product_id=product_id)
        if self.money >= product['price']:
            self.store.give_product(product_id=product_id) # 상점에서 상품 꺼내기
            self.money -= product['price'] # 사용자 금액 지불
            self.store.take_money(product['price']) # 상점 금액 수령
            self.belongs.append(product)
            return product
        else:
            raise Exception('잔돈이 부족합니다.')
    

if __name__ == '__main__':
    store_a = GrabStore(
        products = {
            1: {'name': '키보드', 'price': 30_000},
            2: {'name': '모니터', 'price': 50_000},
        }
    )
    store_b = FruitStore(   
        products = {
            1: {'name': '바나나', 'price': 3_000},
            2: {'name': '사과', 'price': 5_000},
        }
    )
    
    user_a = User(100_000, store = store_a)
    user_b = User(30_000, store = store_b)
    
    user_a.purchase_product(product_id=1)
    user_b.purchase_product(product_id=2)
    print(f"user_a가 {user_a.get_belongs()} 구매")
    print(f"user_b가 {user_b.get_belongs()} 구매")
    