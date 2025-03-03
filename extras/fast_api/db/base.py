from abc import ABC, abstractmethod
from typing import List
from model.user import User


class Database(ABC):
    @abstractmethod
    def insert_user(self, user: User) -> bool:
        """Insert user into database"""
        pass

    @abstractmethod
    def list_all_users(self) -> List[User]:
        """Lists all users in Database"""
        pass
