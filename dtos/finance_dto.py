from pydantic import BaseModel

class FinanceRequestDTO(BaseModel):
    url: str

class FinanceResponseDTO(BaseModel):
    ticker: str
    nome_empresa: str  
    dados: dict