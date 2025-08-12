import sqlite3
from datetime import datetime

DB_PATH = "products.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            store TEXT,
            price TEXT,
            date TEXT
        )
        """)
        conn.commit()

def save_price(item, store, price):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO prices (item, store, price, date) VALUES (?, ?, ?, ?)",
            (item, store, price, datetime.today().isoformat())
        )
        conn.commit()

def get_price_history(item):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT store, price, date FROM prices WHERE item = ?", (item,))
        return cursor.fetchall()

# Initialize DB on import
init_db()