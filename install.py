from database.connection import get_connection

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
        
        connection.commit("Conexao com o banco de dados estabelecida")
    finally:
        connection.close()
