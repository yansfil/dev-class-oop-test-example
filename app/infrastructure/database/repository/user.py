import dataclasses
from dataclasses import dataclass

from app.application.interfaces.user_repository import AbstractRepository
from app.domain.user import User
from app.infrastructure.database.orm import UserModel


class UserRepository(AbstractRepository):
    def create(self, model: User):
        UserModel.create(name=model.name)
        return model

    def find_one(self, model: User):
        user = UserModel.select().where(UserModel.name == model.name).first()
        if user:
            return User(name=user.name)
        return None
