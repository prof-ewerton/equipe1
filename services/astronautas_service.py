from entities.astronauta import Astronauta
from database.insatll import install

def create(self, nome, idade, emMissao, especialidade ):
    if not nome.strip(): 
        raise ValueError("Nome obrigatório.")
    astronauta = Astronauta(None, nome.strip(), idade, emMissao, especialidade)
    return self.install.create(astronauta)