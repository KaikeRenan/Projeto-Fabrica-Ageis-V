from interfaces.finance_repository_interface import IFinanceRepository
from interfaces.financeHealth_interface import (
    IFinancialHealthAnalyzer
)

class FinancialHealthService:

    def __init__(
        self,
        repository: IFinanceRepository,
        analyzer: IFinancialHealthAnalyzer
    ):
        self.repository = repository
        self.analyzer = analyzer

    def execute(self, ticker: str):

        data = self.repository.fetch_google_data(ticker)

        return self.analyzer.evaluate(data)