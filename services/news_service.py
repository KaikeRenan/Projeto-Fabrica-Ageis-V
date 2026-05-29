from repositories.news_repository import NewsRepository

class NewsService:

    def __init__(self, repo: NewsRepository):
        self.repo = repo

    def get_news(self, query: str):
        return self.repo.fetch_news(query)