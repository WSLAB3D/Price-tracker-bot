🛒 Price Tracker Bot
A self-hosted Python bot that tracks item prices from Coles and Woolworths using live scraping and YOLOv8 image recognition, with Discord integration and historical analysis.

🚀 Features
Live price scraping from Coles & Woolworths
YOLOv8 image recognition for item detection
Historical price tracking via SQLite
Discord bot with dynamic commands
Hourly scheduler for automated updates
GitHub-ready structure with CI/CD support
⚙️ Setup
Clone the Repository
git clone https://github.com/WSLAB3D/Price-tracker-bot.git
cd Price-tracker-bot

Install Dependencies
pip install -r requirements.txt

Configure Environment
Create a .env file in the root directory with the following:
DISCORD_TOKEN=your_bot_token
DISCORD_CHANNEL_ID=your_channel_id

Start the Bot
python bot.py

(Optional) Start the Scheduler
python scheduler.py

💬 Bot Commands
!trackadd – Adds an item to the tracked list
!price – Scrapes and returns current prices
!history – Shows historical price chart (WIP)
!listtracked – Lists all currently tracked items

⏱️ Scheduler
Runs hourly and posts updates to your Discord channel:
📦 TimTams update:
🏬 Coles: $3.50
🏪 Woolies: $3.60

Uses schedule to trigger run_scrape() every hour. See scheduler.py.

📁 Project Structure
price-tracker-bot/
├── bot.py – Discord bot logic
├── scheduler.py – Hourly scraping + Discord updates
├── scraper.py – Coles/Woolies scraping functions
├── yolo.py – YOLOv8 image recognition
├── storage.py – SQLite storage and retrieval
├── tasks.py – Shared scraping logic
├── tracked_items.txt – List of tracked items
├── requirements.txt – Python dependencies
├── Dockerfile – Docker configuration
└── README.md – Project documentation

🛠️ Dev Tips
Use .env for secrets and tokens
Dockerize for deployment (optional)
Add unit tests for scraper and bot logic
Extend with charts, alerts, or a web dashboard
📦 CI/CD Badges (Optional)
✅ CI Status – Continuous Integration
🐳 Docker Pulls – Docker image stats
📊 Coverage – Test coverage
