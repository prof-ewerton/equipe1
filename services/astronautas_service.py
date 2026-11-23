from entities/astronauta.py import Astronauta
from database/insatll.py import install

def create(self, nome, idade, emMissao, especialidade ):
        if not nome.strip(): 
            raise ValueError("Nome obrigatório.")
        if not 
        astronauta = Astronauta(None, nome.strip(), idade, emMissao, especialidade)
        return self.install.create(astronauta)