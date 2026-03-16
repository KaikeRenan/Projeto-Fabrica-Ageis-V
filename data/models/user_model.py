from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class UserModel(base):

    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(36))
    email = Column(String(36), unique=True)
    password = Column(String(36))