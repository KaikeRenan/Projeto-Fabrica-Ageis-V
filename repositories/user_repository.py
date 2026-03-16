from typing import List
from sqlalchemy.orm import Session
from entities.user import User
from interfaces.user_repository_interface import UserRepositoryInterface
from data.models.user_model import UserModel


class UserRepository(UserRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> User:

        model = UserModel(
            id=str(user.id),
            name=user.name,
            email=user.email,
            password=user.password
        )

        self.db.add(model)
        self.db.commit()

        return User

    def get_all(self) -> List[User]:
        users = self.db.query(UserModel).all()

        return [
            User(u.id, u.name, u.email, u.password)
            for u in users
        ]


    def get_by_id(self, user_id: str) -> User:

        user = (
            self.db
            .query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

        if not user:
            return None

        return User(user.id, user.name, user.email, user.password)


    


    def update(self, user_id: str, user: User) -> User:

        model = (
            self.db
            .query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

        if model:
            model.name = user.name
            model.email = user.email
            model.password = user.password
            self.db.commit()

        return user


    def delete(self, user_id: str) -> bool:

        model = (
            self.db
            .query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

        if model:
            self.db.delete(model)
            self.db.commit()
            return True

        return False
