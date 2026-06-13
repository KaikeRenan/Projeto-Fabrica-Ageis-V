from abc import ABC, abstractmethod

class IFinancialHealthAnalyzer(ABC):

    @abstractmethod
    def evaluate(self, data: dict) -> dict:
        pass