# 🛍️ Image Price Bot

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![discord.py](https://img.shields.io/badge/discord.py-2.x-green?logo=discord)
![YOLOv8](https://img.shields.io/badge/YOLOv8-ImageDetection-orange?logo=openai)
![Docker Ready](https://img.shields.io/badge/Docker-ready-blue?logo=docker)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)
![License](https://img.shields.io/github/license/your-username/image-price-bot.svg)
![Last Commit](https://img.shields.io/github/last-commit/your-username/image-price-bot)
![Issues](https://img.shields.io/github/issues/your-username/image-price-bot)

> A self-hosted Discord bot that detects grocery products via image recognition, scrapes Australian supermarket prices, tracks price history, and sends price-drop alerts to your Discord server.

---

## 🔧 Features

- 📸 Upload a product image — YOLOv8 detects item name
- 🛒 Scrapes Woolworths & Coles websites for live prices
- 🧠 Persists data in SQLite with timestamped entries
- 📈 Generates price trend charts using Matplotlib
- 💬 Discord bot interface for tracking, alerts & control
- 🗓️ Scheduled scraping via `APScheduler` or cron
- 🐳 Dockerized for portable deployment

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/image-price-bot.git
cd image-price-bot