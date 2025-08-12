import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime
import re

def generate_chart(item):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, price FROM prices WHERE item=?", (item,))
    data = cursor.fetchall()
    conn.close()

    if not data:
        return None

    try:
        dates = [datetime.fromisoformat(d) for d, _ in data]
        prices = [float(p.replace("$", "").strip()) for _, p in data]
    except ValueError:
        return None

    plt.figure(figsize=(8, 4))
    plt.plot(dates, prices, marker="o", linestyle="-", color="teal")
    plt.title(f"Price Trend - {item}")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.gcf().autofmt_xdate()

    safe_name = re.sub(r"\W+", "_", item)
    filename = f"{safe_name}_trend.png"
    plt.savefig(filename)
    plt.close()

    return filename