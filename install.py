from database.connection import get_db_connection

def install():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS galaxias(
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                qtdEstrela INTEGER,
                tipo TEXT,
                habitavel BOOL NOT NULL DEFAULT FALSE
             )
        """)
        
        connection.commit()
    finally:
        connection.close()        
        




