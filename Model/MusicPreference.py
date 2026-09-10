from sqlalchemy import Column, Integer, String
from Model.Base import Base

class MusicPreference(Base):
    __tablename__ = 'musicPreference'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    artista = Column(String(20))
    data_criacao = Column(String(100))
  

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "artista": self.artista,
            "data_criacao": self.data_criacao
        }