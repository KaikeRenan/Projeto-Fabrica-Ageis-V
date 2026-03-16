from dataclasses import dataclass # para evitar repetição de código: __init__, self.
from uuid import UUID, uuid4 # para identificadores unicos e função para gerer aletório

@dataclass 
class User:
    id: UUID
    name: str
    email: str
    password: str

    @staticmethod 
    def create(name: str, email: str, password: str):
        return User(uuid4(), name, email, password)