from pydantic import BaseModel

class NewsRequestDTO(BaseModel):
    q: str

class NewsItemDTO(BaseModel):
    titulo: str
    conteudo: str
    url: str

class NewsResponseDTO(BaseModel):
    noticias: list[NewsItemDTO]