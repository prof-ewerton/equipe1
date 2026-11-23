from database.connection import get_db_connection

def install():

    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS astronautas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                emMissao BOOLEAN NOT NULL DEFAULT TRUE,
                especialidade TEXT NOT NULL
            )
        """)
        
        connection.commit()
        finally:
            connection.close()
            
    #Tabela galaxias            
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS galaxias(
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                qtdEstrela INTEGER,
                tipo TEXT,
                habitavel BOOL NOT NULL DEFAULT TRUE
             )
        """)
        
        connection.commit()
    finally:
        connection.close()
        
    #População Galaxia
    def create(self, galaxia):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO VALUES itens (
                "Via lactea", 12, "gasosa", True,
                "Andromeda", 7, "luminosa", False,
                "Cinturião", 20, "terrosa", True,
                "Terraformar", 3, "venenosa", False,
                "Escaldante", 30, "flamejante", False
                 )
             """, (galaxia.nome, galaxia.qtdEstrela, galaxia.tipo, galaxia.habitavel))
            
            connection.commit()
        finally:
            connection.close()        

if __name__ == "__main__":
    install()      
