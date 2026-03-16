from fastapi import FastAPI
from controllers.user_controller import router

app = FastAPI()

app.include_router(router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# inicia a API e registra as rotas