def add(a, b):
    return a + b

def test_add():
    a, b = 1, 2
    assert add(a, b) == 3

def test_add2():
    a, b = 1, 3
    assert add(a, b) == 4 

def test_add3():
    a, b = 2, 5
    assert add(a, b) == 7


# if __name__ == "__main__":
    # print(add(1, 2) == 3)
    # print(add(3, 4) == 7)
