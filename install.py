from database.connection import get_connection

def install():

    connection = get_connection()
    try:
        cursor = connection.cursor()
        
        #Tabela astronautas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS astronautas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                emMissao BOOLEAN NOT NULL DEFAULT TRUE,
                especialidade TEXT NOT NULL
            )
        """)
        
        #Tabela galaxias 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS galaxias(
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                qtdEstrela INTEGER,
                tipo TEXT,
                habitavel BOOL NOT NULL DEFAULT TRUE
             )
        """)
        
        cursor.execute("SELECT COUNT(*) FROM astronautas")
        if cursor.fetchone()[0] == 0:
            astronautas_iniciais = [("Natalia", 19, True, "luas"),
                                    ("Ediene", 22, False, "planetas"),
                                    ("Jamili", 21, True, "cometas"),
                                    ("Lucas", 20, False, "buracos negros"),
                                    ("Felipe" 21, True, "estrelas")]
            cursor.executemany("INSERT INTO astronautas (nome, idade, emMissao, especialidade) VALUES (?, ?, ?, ?)", astrounautas_iniciais)     
        
        def create(self, galaxia):
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