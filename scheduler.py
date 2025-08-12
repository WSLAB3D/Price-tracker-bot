import schedule
import time
import requests
import os
from tasks import scheduled_scrape

TRACKED_ITEMS_FILE = "tracked_items.txt"

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

def load_tracked_items():
    if not os.path.exists(TRACKED_ITEMS_FILE):
        return []
    with open(TRACKED_ITEMS_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def send_discord_message(content):
    url = f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages"
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"content": content}
    requests.post(url, headers=headers, json=payload)

def run_scrape():
    items = load_tracked_items()
    for item in items:
        coles = scheduled_scrape(item, "Coles")
        woolies = scheduled_scrape(item, "Woolies")
        message = (
            f"📦 `{item}` update:\n"
            f"🏪 Coles: {coles}\n"
            f"🏬 Woolies: {woolies}"
        )
        send_discord_message(message)

schedule.every().hour.at(":00").do(run_scrape)

print("[Scheduler] Started hourly scraping task.")
while True:
    schedule.run_pending()
    time.sleep(60)