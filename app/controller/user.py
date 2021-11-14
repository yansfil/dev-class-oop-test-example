from app.application.services.user import UserService
from app.infrastructure.database.repository.user import UserRepository


def signup():
    user_service = UserService(user_repository=UserRepository())
    user = user_service.create_user(user_name="grab")
    return user

