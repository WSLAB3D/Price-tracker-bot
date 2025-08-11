# 🛒 Price Tracker Bot

A self-hosted Discord bot that tracks supermarket prices using image recognition (YOLOv8), live web scraping, and historical analysis. Designed for automation enthusiasts who want actionable insights delivered straight to Discord.

---

## 📦 Features

- 🧠 **YOLOv8 Image Recognition**: Detects products and prices from flyers or shelf photos.
- 🌐 **Live Web Scraping**: Pulls current prices from online supermarket listings.
- 📊 **Historical Tracking**: Stores price data for trend analysis and charting.
- 📡 **Discord Integration**: Responds to commands, sends alerts, and visualizes price changes.
- 🐳 **Dockerized Deployment**: Easy to run locally or on a server.
- 🔐 **Secure Token Handling**: Uses `.env` for Discord and API credentials.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/WSLAB3D/Price-tracker-bot.git
cd Price-tracker-bot
```

### 2. Create a Discord Bot Token

- Go to the [Discord Developer Portal](https://discord.com/developers/applications)
- Create a new application → Add a bot
- Enable **Message Content Intent** under "Privileged Gateway Intents"
- Copy the bot token

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
DISCORD_TOKEN=your_discord_bot_token
```

Ensure `.env` is listed in `.gitignore`.

---

## 🐳 Docker Build & Run

### Build the Docker Image

```bash
docker build -t price-tracker-bot .
```

### Run the Container

```bash
docker run --env-file .env price-tracker-bot
```

### Or Use Docker Compose

```bash
docker-compose up --build
```

---

## 💬 Bot Usage

Once the bot is running and invited to your server, try these commands:

| Command               | Description                                      |
|----------------------|--------------------------------------------------|
| `!track [item]`       | Scrapes and returns current price for an item   |
| `!history [item]`     | Shows price trend over time                     |
| `!analyze [image]`    | Detects prices from uploaded image              |
| `!help`               | Lists available commands                        |

---

## 🧠 Architecture Overview

```text
Discord Bot
├── YOLOv8 Image Processor
├── Scraper Module
├── SQLite Storage
└── Chart Generator
```

---

## 📚 Development Notes

- Python 3.11+
- Dependencies managed via `requirements.txt`
- YOLOv8 model weights should be placed in `/models`
- Scraper logic lives in `/scraper`
- Discord bot logic in `/bot.py`

---

## 🛡️ Security & Rate Limiting

- Tokens and credentials are loaded via `.env`
- Scraping modules include polite headers and delay logic
- Discord bot uses minimal permissions

---

## 📈 Future Enhancements

- Multi-store support
- Interactive chart embeds
- Receipt OCR
- Price drop alerts
- Web dashboard

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT