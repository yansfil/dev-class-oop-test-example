from peewee import CharField, Model, SqliteDatabase, IntegerField

# 참고 : https://github.com/coleifer/peewee

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "users"


class ProductModel(BaseModel):
    name = CharField(null=False)
    price = IntegerField(null=False)

    class Meta:
        table_name = "products"
