from fastapi import APIRouter, Depends
from services.user_service import UserService
from repositories.user_repository import UserRepository
from dtos.user_dto import UserCreateDTO, UserResponseDTO, UserUpdateDTO
from data.database import SessionLocal

router = APIRouter()

def get_service():
    db = SessionLocal()
    repository = UserRepository(db)
    return UserService(repository)

@router.post("/users", response_model=UserResponseDTO)
def create_user(user: UserCreateDTO, service: UserService = Depends(get_service)):
    return service.create_user(user)

@router.get("/users/{id}")
def get_by_id(id: str, service: UserService = Depends(get_service)):
    return service.get_user(id)

@router.get("/users")
def get_all(service: UserService = Depends(get_service)):
    return service.list_users()

# @router.put("/users/{id}")
# def update(id: str, user: dict):
#     return service.update_user(id, user)

@router.delete("/users/{id}")
def delete(id: str, service: UserService = Depends(get_service)):
    service.delete_user(id)
    return {"message": "user deleted"}


@router.put("/users/{id}")
def update(
    id: str, 
    user: UserCreateDTO, 
    service: UserService = Depends(get_service)):
    return service.update_user(id, user)

@router.patch("/users/{id}")
def partial_update(
    id: str,
    user: UserUpdateDTO, 
    service: UserService = Depends(get_service)):
    return service.patch_user(id, user)