import re
from entities.finance import FinanceEntity
from interfaces.finance_repository_interface import IFinanceRepository

class FinanceService:
    def __init__(self, repository: IFinanceRepository):
        self.repository = repository

    def execute(self, url: str):
        ticker = url.split('/')[-1].split('?')[0]
        
        data = self.repository.fetch_google_data(ticker)
        
        return FinanceEntity(
            ticker=ticker,
            nome_empresa=data.get("nome_empresa", "Nome não encontrado"), 
            dados={
                "mercado": data.get("mercado"),
                "financeiro": data.get("financeiro")
            }
        )