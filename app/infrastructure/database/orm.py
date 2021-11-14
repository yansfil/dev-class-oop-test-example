from peewee import CharField, Model, SqliteDatabase, IntegerField

# 참고 : https://github.com/coleifer/peewee
# DB의 경로를 동적으로 넣어줘야함 https://docs.peewee-orm.com/en/latest/peewee/database.html#run-time-database-configuration
db = SqliteDatabase(None)




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
