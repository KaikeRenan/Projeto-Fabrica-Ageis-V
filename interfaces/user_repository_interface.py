from abc import ABC, abstractmethod # para criar classes abstratras
from typing import List # possibilita uma função retornar uma lista de objetos
from entities.user import User 

class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass
    
    @abstractmethod
    def get_by_id(self, id: str) -> User:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def delete(self, id: str):
        pass