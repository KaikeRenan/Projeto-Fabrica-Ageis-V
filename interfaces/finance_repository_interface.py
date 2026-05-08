from abc import ABC, abstractmethod

class IFinanceRepository(ABC):
    @abstractmethod
    def fetch_google_data(self, ticker: str) -> dict:
        pass