from entities.user import User
from interfaces.user_repository_interface import UserRepositoryInterface
from dtos.user_dto import UserCreateDTO

class UserService:

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def create_user(self, dto: UserCreateDTO):
        user = User.create(dto.name, dto.email, dto.password)
        return self.repository.create_user(user)

    def get_user(self, id):
        return self.repository.get_by_id(id)    

    def list_users(self):
        return self.repository.get_all()
    
    def delete_user(self, id):
        return self.repository.delete(id)
    
    def update_user(self, id, dto: UserCreateDTO):
        return self.repository.update(id, dto.dict())
    
    def patch_user(self, id, dto: UserCreateDTO):
        data = dto.dict(exclude_unset=True)
        return self.repository.update(id, data)