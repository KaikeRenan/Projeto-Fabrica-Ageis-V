from fastapi import APIRouter
from repositories.news_repository import NewsRepository
from services.news_service import NewsService

router = APIRouter(prefix="/news", tags=["News"])

repo = NewsRepository()
service = NewsService(repo)

#To-Do: implementar um modo de pegar o Ticket da empresa e usar ele como query para a API de notícias
@router.get("/")
def fetch_news(q: str = "petrobras"):

    return service.get_news(q)
