from pydantic import BaseModel

class MusicPreferenceUpdateSchema(BaseModel):
    id: int

    nome: str
    genero: str
    artista: str
    data_criacao: str
    