class GrabStore:
    def __init__(self):
        self.money = 0
        self.name = "그랩마켓"
        self.products = {
            1: {"name": "키보드", "price": 30_000},
            2: {"name": "모니터", "price": 50_000},
        }

    def set_money(self, money):
        self.money = money

    def set_products(self, products):
        self.products = products

    def get_money(self):
        return self.money

    def get_products(self):
        return self.products


class User:
    def __init__(self):
        self.money = 0
        self.store = GrabStore()
        self.belongs = []

    def set_money(self, money):
        self.money = money

    def set_belongs(self, belongs):
        self.belongs = belongs

    def get_money(self):
        return self.money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_product(self, product_id):
        products = self.store.get_products()
        return products[product_id]

    def purchase_product(self, product_id):
        product = self.see_product(product_id)
        if self.money >= product["price"]:
            self.store.products.pop(product_id)  # 상점에서 상품 꺼내기
            self.money -= product["price"]  # 사용자 금액 지불
            self.store.money += product["price"]  # 상점 금액 수령
            self.belongs.append(product)
            return product


if __name__ == "__main__":
    user = User()
    user.set_money(100_000)
    user.purchase_product(product_id=1)
