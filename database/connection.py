import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "universo.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create(self, astronauta):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO astronautas (nome, idade, emMissao, especialidade)
                VALUES (?, ?, ?) """, (astronauta.nome, astronauta.idade, astronauta.emMissao, astronauta.especialidade))
        
            connection.commit()
            return cursor.lastrowid
            
        finally:
            connection.close()