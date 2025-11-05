import sqlite3

conn = sqlite3.connect("bemfarma.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    mensagem TEXT NOT NULL
);
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")
