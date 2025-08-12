import os
import uuid
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils import detect_product, scrape_coles, scrape_woolies, save_price  # Adjust as needed

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        for attachment in message.attachments:
            path = f"./{uuid.uuid4()}.png"
            await attachment.save(path)

            try:
                item = detect_product(path)
                coles = scrape_coles(item)
                woolies = scrape_woolies(item)
                save_price(item, "Coles", coles)
                save_price(item, "Woolies", woolies)

                await message.channel.send(
                    f"📦 Item: `{item}`\n🏪 Coles: {coles}\n🏬 Woolies: {woolies}"
                )
            except Exception as e:
                await message.channel.send(f"❌ Error: {e}")
            finally:
                os.remove(path)

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))