import abc
from typing import Optional

from app.domain.user import Domain


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def find_one(self, model: Domain) -> Optional[Domain]:
        ...

    @abc.abstractmethod
    def create(self, model: Domain) -> Domain:
        ...

    @abc.abstractmethod
    def find_by_id(self, id: int) -> Optional[Domain]:
        ...