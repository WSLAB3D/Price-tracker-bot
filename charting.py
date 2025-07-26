import matplotlib.pyplot as plt
import sqlite3

def generate_chart(item):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, price FROM prices WHERE item=?", (item,))
    data = cursor.fetchall()
    
    dates = [d for d, _ in data]
    prices = [float(p.replace("$", "")) for _, p in data]
    
    plt.plot(dates, prices, marker="o")
    plt.title(f"Price Trend - {item}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{item}_trend.png")
    return f"{item}_trend.png"