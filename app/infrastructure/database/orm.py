from peewee import CharField, Model, SqliteDatabase

# 참고 : https://github.com/coleifer/peewee

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "users"
