from abc import ABC, abstractmethod

class INewsRepository(ABC):

    @abstractmethod
    def fetch_news(self, query: str) -> dict:
        pass