from fastapi import APIRouter
from services.news_service import get_news

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/")
def fetch_news(q: str = "petrobras"):
    return get_news(q)