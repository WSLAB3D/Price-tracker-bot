# 🛒 Price Tracker Bot

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![YOLOv8](https://img.shields.io/badge/image--recognition-YOLOv8-green)
![Discord](https://img.shields.io/badge/integration-Discord-5865F2?logo=discord&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/WSLAB3D/Price-tracker-bot/ci.yml?label=CI)

Self-hosted Discord bot for tracking supermarket prices via image recognition, live web scraping, and persistent storage. Built with modular components and designed for extensibility.

---

## 🚀 Features

- 🖼️ YOLOv8-based image recognition of price tags
- 🔍 Live web scraping of store listings (Woolworths, Coles etc.)
- 💾 SQLite storage with historical tracking and charting
- 📊 Discord bot with embedded summaries and alerts
- 🔐 `.env` config support for secure deployment
- 🐳 Docker-ready for easy self-hosting

---

## 🧱 Architecture Overview

```mermaid
graph TD
  A[Discord Bot] --> B[Image Recognition (YOLOv8)]
  A --> C[Scraper Module]
  B --> D[Price Parser]
  C --> D
  D --> E[SQLite Database]
  E --> F[Charting & Historical Analysis]
  F --> G[Discord Alerts & Embeds]