from database import engine
from models.user_model import base

base.metadata.create_all(bind=engine)