from abc import ABC, abstractmethod

class IGoogleFinanceScraper(ABC):

    @abstractmethod
    def fetch(self, ticker: str) -> dict:
        pass