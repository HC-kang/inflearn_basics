from peewee import *

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    username = CharField(unique=True)

    class Meta:
        table_name = "users"
