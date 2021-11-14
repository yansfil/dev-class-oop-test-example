from app.application.interfaces.user_repository import AbstractRepository
from app.domain.user import User


class UserService:
    def __init__(self, user_repository: AbstractRepository):
        self.user_repository = user_repository

    def create_user(self, user_name: str):
        _user = User(name=user_name)
        user = self.user_repository.create(_user)
        return user
