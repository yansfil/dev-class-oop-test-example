import abc

from app.domain.user import Domain


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def find_one(self, model: Domain) -> Domain:
        ...

    @abc.abstractmethod
    def create(self, model: Domain) -> Domain:
        ...
