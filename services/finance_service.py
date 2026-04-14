import re
from entities.finance import FinanceEntity
from interfaces.finance_repository_interface import IFinanceRepository

class FinanceService:
    def __init__(self, repository: IFinanceRepository):
        self.repository = repository

    def execute(self, input_data: str):
        if "google.com" in input_data:
            ticker = input_data.split('/quote/')[-1].split('?')[0]
        else:
            ticker = input_data.strip()
        
        data = self.repository.fetch_google_data(ticker)
        
        return FinanceEntity(
            ticker=ticker,
            nome_empresa=data.get("nome_empresa", "Nome não encontrado"), 
            dados={
                "mercado": data.get("mercado"),
                "financeiro": data.get("financeiro")
            }
        )