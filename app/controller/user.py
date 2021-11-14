from fastapi import HTTPException

from app.application.services.user import UserService
from app.infrastructure.database.repository.user import UserRepository


def signup():
    user_service = UserService(user_repository=UserRepository())
    try:
        user = user_service.create_user(user_name="grab")
        return user
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


