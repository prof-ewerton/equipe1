from entities/galaxia.py import Galaxia
from database/insatll.py import install

def create(self, nome, qtdEstela, tipo, habitavel):
    if not nome.strip():
        raise ValueError("Nome obrigatório.")
    elif qtdEstela < 0:
        raise ValueError("Valor inexistente.")
    objeto_galaxia = Galaxia(None, nome.strip(), qtdEstela, tipo, habitavel=True)
    return self.install.create(objeto_galaxia)
        