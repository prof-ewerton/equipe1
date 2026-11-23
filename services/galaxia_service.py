class GalaxiaService:
    def __init__(self, database):
        self.database = database
        
    def create(self, nome, qtdEstela, tipo, habitavel):
        if not nome.strip():
            raise ValueError("Nome obrigatório.")
        elif qtdEstela < 0:
            raise ValueError("Valor inexistente.")
        objeto_galaxia = Galaxia(nome.strip(), qtdEstela, tipo, habitavel=True)
        return self.database.create(objeto_galaxia)
        