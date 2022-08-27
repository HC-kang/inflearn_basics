from main import Product

def test_show_product(grab_store):
    # given
    product_id = 1
    
    # when
    product = grab_store.show_product(product_id=product_id)
    
    # then
    assert product == Product(name="키보드", price=30000)


def test_take_money(grab_store):
    price = 100
    pre_money = grab_store._money
    
    grab_store._take_money(money=price)
    
    assert grab_store._money == pre_money + price


def test_return_money(grab_store):
    price = 100
    pre_money = grab_store._money
    
    grab_store._return_money(money=price)
    
    assert grab_store._money == pre_money - price


def test_take_out_product(grab_store):
    product_id = 1
    
    product = grab_store._take_out_product(product_id=product_id)

    assert product == Product(name="키보드", price=30000)
    assert not grab_store._products.get(product_id, None)