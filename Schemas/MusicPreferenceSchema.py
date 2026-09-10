from pydantic import BaseModel

class MusicPreferenceSchema(BaseModel):
    nome: str
    genero: str
    artista: str
    data_criacao: str
   