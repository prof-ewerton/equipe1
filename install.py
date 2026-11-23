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
        
        cursor.execute("SELECT COUNT(*) FROM astronautas")
        if cursor.fetchone()[0] == 0:
            astronautas_iniciais = [("Natalia", 19, True, "luas"),
                                    ("Ediene", 22, False, "planetas"),
                                    ("Jamili", 21, True, "cometas"),]
            cursor.executemany(
                "INSERT INTO astronautas (nome, idade, emMissao, especialidade) VALUES (?, ?, ?, ?)", astrounautas_iniciais)
        
        connection.commit("Conexao com o banco de dados estabelecida")
    finally:
        connection.close()
