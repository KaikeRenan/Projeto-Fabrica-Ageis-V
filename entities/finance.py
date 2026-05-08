from dataclasses import dataclass

@dataclass
class FinanceEntity:
    ticker: str
    nome_empresa: str
    dados: dict