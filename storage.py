import sqlite3
from datetime import datetime

conn = sqlite3.connect("products.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS prices (
    item TEXT,
    store TEXT,
    price TEXT,
    date TEXT
)""")

def save_price(item, store, price):
    cursor.execute("INSERT INTO prices VALUES (?, ?, ?, ?)", (item, store, price, datetime.today().isoformat()))
    conn.commit()