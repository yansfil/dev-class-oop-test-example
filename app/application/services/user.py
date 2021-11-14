from app.application.interfaces.user_repository import AbstractRepository
from app.domain.user import User


class UserService:
    def __init__(self, user_repository: AbstractRepository):
        self.user_repository = user_repository

    def create_user(self, user_name: str):
        _user = User(name=user_name)
        if self.user_repository.find_one(model=_user):
            raise ValueError("유저가 이미 존재합니다.")
        user = self.user_repository.create(model=_user)
        return user
