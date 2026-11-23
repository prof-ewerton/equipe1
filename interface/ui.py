from services.astronautas_service import create
from services.galaxia_service import create

class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Astronautas", self.menu_entity_one),
        ]

    def show(self):
        while True:
            print("\n===== Universo =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")
            print("1 - Astronauta")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break
            elif option == "1":
                menu_entity_one()
                break

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== Universo =====")
        print("== Astronautas ==")
        print("0 - Sair")
        print("1 - Cadastrar astronauta")
        print("2 - Cadastrar galaxia")
        
        option = input("Escolha uma opção: ")
        
        if option == "0":
            print("Saindo...")
            show()
            
        elif option == "1":
            def create(self):
                nome = input("Nome: ")
                idade = input("Idade: ")
                emMissao = input("Em missão: ")
                especialidade = input("Especialidade: ")
            
            try:
                astronauta_id = self.astronautas_service.create(nome, idade, emMissao, especialidade)
                print(f"Cadastrado realizado com ID {item_id}.")
            except ValueError as erro:
                print(f"Erro: {erro}")
        
        elif option == "2":
            def create(self):    
                nome = input("Nome: ")
                qtdEstela = input("Quantidade estrela: ")
                tipo = input("Tipo: ")
                habitavel = input("Habitável? (s/n): ")
                
            try:
                galaxia_id = self.service.create(nome, qtdEstela, tipo, habitavel)
                print(f"Cadastrado com ID {galaxia_id}.")
            except ValueError as erro:
                print(f"Erro: {erro}")
