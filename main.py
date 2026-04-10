from fastapi import FastAPI
from controllers.user_controller import router
from controllers.news_controller import router as news_router

app = FastAPI()

app.include_router(router)
app.include_router(news_router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# inicia a API e registra as rotas