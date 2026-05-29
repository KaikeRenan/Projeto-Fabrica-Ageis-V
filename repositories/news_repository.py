import httpx
from interfaces.news_repository_interface import INewsRepository

API_KEY = "SUA_API_KEY"

class NewsRepository(INewsRepository):

    def fetch_news(self, query: str) -> dict:

        url = "https://newsapi.org/v2/everything"

        params = {
            "q": query,
            "language": "pt",
            "sortBy": "publishedAt",
            "apiKey": API_KEY
        }

        with httpx.Client() as client:
            response = client.get(url, params=params)

        data = response.json()

        noticias = []

        for article in data.get("articles", []):

            noticias.append({
                "titulo": article.get("title"),
                "conteudo": article.get("description"),
                "url": article.get("url")
            })

        return {
            "noticias": noticias
        }