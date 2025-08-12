🛒 Discord Price Tracker Bot

A self-hosted Python bot that tracks item prices from Coles and Woolworths using live scraping and image recognition (YOLOv8), with Discord integration and historical analysis.

🚀 Features

🔍 Live price scraping from Coles & Woolworths

🧠 YOLOv8 image recognition for item detection

📊 Historical price tracking via SQLite

💬 Discord bot with dynamic commands

🕒 Hourly scheduler for automated updates

📁 GitHub-ready structure with CI/CD support

⚙️ Setup

1. Clone the repo

git clone https://github.com/yourusername/price-tracker-bot.git
cd price-tracker-bot

2. Install dependencies

pip install -r requirements.txt

3. Configure environment

Create a .env file or set environment variables:

DISCORD_TOKEN=your_bot_token
DISCORD_CHANNEL_ID=your_channel_id

4. Start the bot

python bot.py

5. Start the scheduler (optional)

python scheduler.py

💬 Bot Commands

Command

Description

!trackadd <item>

Adds an item to the tracked list

!price <item>

Scrapes and returns current prices

!history <item>

Shows historical price chart (WIP)

!listtracked

Lists all currently tracked items

🕒 Scheduler

Runs hourly and posts updates to your Discord channel:

📦 `TimTams` update:
🏪 Coles: $3.50
🏬 Woolies: $3.60

Uses schedule to trigger run_scrape() every hour. See scheduler.py.

📁 Repo Structure

price-tracker-bot/
├── bot.py               # Discord bot logic
├── scheduler.py         # Hourly scraping + Discord updates
├── scraper.py           # Coles/Woolies scraping functions
├── yolo.py              # YOLOv8 image recognition
├── storage.py           # SQLite storage and retrieval
├── tasks.py             # Shared scraping logic
├── tracked_items.txt    # List of tracked items
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation

🛠️ Dev Tips

✅ Use .env for secrets and tokens

🐳 Dockerize for deployment (optional)

🧪 Add unit tests for scraper and bot logic

📈 Extend with charts, alerts, or web dashboard

🛠️ CI/CD Badges

Badge

Description



Continuous Integration status



Docker image pull count



Test coverage percentage

