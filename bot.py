import os
import uuid
import discord
from discord.ext import commands
from dotenv import load_dotenv

from scraper import scrape_coles, scrape_woolies
from image_handler import detect_product
from storage import save_price, get_price_history

from collections import defaultdict
from datetime import datetime

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 📦 Utility: Summarize average prices
def summarize_prices(records):
    store_prices = defaultdict(list)
    for store, price, _ in records:
        try:
            value = float(price.replace("$", "").strip())
            store_prices[store].append(value)
        except:
            continue
    return {
        store: round(sum(prices) / len(prices), 2)
        for store, prices in store_prices.items()
    }

# ✅ Bot startup
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# 📷 Image handler
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        for attachment in message.attachments:
            path = f"./{uuid.uuid4()}.png"
            await attachment.save(path)

            try:
                items = detect_product(path)
                for item in items:
                    coles = scrape_coles(item)
                    woolies = scrape_woolies(item)

                    save_price(item, "Coles", coles["price"])
                    save_price(item, "Woolies", woolies["price"])

                    await message.channel.send(
                        f"📦 Item: `{item}`\n"
                        f"🏪 Coles: {coles['price']} ({coles['title']})\n"
                        f"🏬 Woolies: {woolies['price']} ({woolies['title']})"
                    )
            except Exception as e:
                await message.channel.send(f"❌ Error: {e}")
            finally:
                os.remove(path)

    await bot.process_commands(message)

# 📈 !history command
@bot.command(name="history")
async def history(ctx, *, item: str):
    records = get_price_history(item)
    if not records:
        await ctx.send(f"📦 No history found for `{item}`.")
        return

    lines = [f"📈 Price history for `{item}`:"]
    for store, price, date in records[-10:]:
        date_fmt = datetime.fromisoformat(date).strftime("%d %b %Y")
        lines.append(f"• {store}: {price} on `{date_fmt}`")

    summary = summarize_prices(records)
    for store, avg in summary.items():
        lines.append(f"📊 Avg {store}: ${avg:.2f}")

    await ctx.send("\n".join(lines))

# ⚖️ !compare command
@bot.command(name="compare")
async def compare(ctx, *, item: str):
    coles = scrape_coles(item)
    woolies = scrape_woolies(item)

    lines = [f"🛒 Price comparison for `{item}`:"]
    lines.append(f"🏪 Coles: {coles['price']} ({coles['title']})")
    lines.append(f"🏬 Woolies: {woolies['price']} ({woolies['title']})")

    await ctx.send("\n".join(lines))

TRACKED_ITEMS_FILE = "tracked_items.txt"

def add_tracked_item(item):
    items = set()
    if os.path.exists(TRACKED_ITEMS_FILE):
        with open(TRACKED_ITEMS_FILE, "r") as f:
            items = set(line.strip() for line in f)
    items.add(item)
    with open(TRACKED_ITEMS_FILE, "w") as f:
        for i in sorted(items):
            f.write(i + "\n")

@bot.command(name="trackadd")
async def trackadd(ctx, *, item: str):
    add_tracked_item(item)
    await ctx.send(f"✅ `{item}` added to tracked items.")

# 🚀 Run bot
bot.run(os.getenv("DISCORD_TOKEN"))