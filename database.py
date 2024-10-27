# database.py
import sqlite3

def init_db():
    with sqlite3.connect("config.DB_PATH") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            type TEXT,
                            amount REAL,
                            category TEXT,
                            description TEXT
                        )''')
        conn.commit()

def add_transaction(entry_type, amount, category, description):
    with sqlite3.connect("config.DB_PATH") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (type, amount, category, description) VALUES (?, ?, ?, ?)",
                       (entry_type, amount, category, description))
        conn.commit()

def get_transactions():
    with sqlite3.connect("config.DB_PATH") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        return cursor.fetchall()
