from fastapi import FastAPI
from controllers.user_controller import router
from controllers.finance_controller import router as finance_router

app = FastAPI()

app.include_router(router)
app.include_router(finance_router)
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# inicia a API e registra as rotas