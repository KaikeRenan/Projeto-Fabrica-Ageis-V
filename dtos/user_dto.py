from pydantic import BaseModel
from typing import Optional

class UserCreateDTO(BaseModel):
    name: str
    email: str
    password: str

class UserUpdateDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponseDTO(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_model = True