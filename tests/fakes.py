from app.application.interfaces.user_repository import AbstractRepository
from app.domain.user import User


class FakeUserRepository(AbstractRepository):
    def __init__(self):
        self.users = []

    def create(self, model: User):
        self.users.append(model)
        return model

    def find_one(self, model: User):
        for _user in self.users:
            if _user.name == model.name:
                return model
        return None

    def find_by_id(self, id: int):
        ...

