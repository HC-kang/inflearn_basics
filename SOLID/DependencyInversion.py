from abc import ABC

# AS-IS
class InMemoryDatabase:
    def __init__(self):
        pass
    
    def store_data(self, data):
        pass
    

class App():
    def __init__(self):
        self.inMemoryDB = InMemoryDatabase()
    
    def save_user(self, data):
        self.inMemoryDB.store_data(data)


if __name__ == "__main__":
    app = App()
    app.save_user({'id': 1, 'name': 'grab'})


# TO-BE
# 1. 의존성 역전
class Database(ABC):
    def __init__(self):
        pass


class InMemoryDatabase(Database):
    def __init__(self):
        pass
    
    def store_data(self, data):
        pass

class App():
    def __init__(self):
        # 고수준을 의존하지만 구현체를 구현하는 코드가 함께 있어, 반쪽짜리 의존성 역전임.
        self.inMemoryDB: Database = InMemoryDatabase()
    
    def save_user(self, data):
        self.inMemoryDB.store_data(data)


if __name__ == "__main__":
    app = App()
    app.save_user({'id': 1, 'name': 'grab'})


# 2. 의존성 주입
class App():
    def __init__(self, database: Database):
        self.database = database
    
    def save_user(self, data):
        self.database.store_data(data)


if __name__ == "__main__":
    inMemoryDB = InMemoryDatabase()
    app = App(inMemoryDB)
    app.save_user({'id': 1, 'name': 'grab'})
