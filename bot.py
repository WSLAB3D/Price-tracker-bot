import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable if you're reading message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
async def on_message(message):
    if message.attachments:
        for attachment in message.attachments:
            path = f"./{attachment.filename}"
            await attachment.save(path)
            item = detect_product(path)
            coles = scrape_coles(item)
            woolies = scrape_woolies(item)
            save_price(item, "Coles", coles)
            save_price(item, "Woolies", woolies)
            await message.channel.send(
                f"📦 Item: `{item}`\n🏪 Coles: {coles}\n🏬 Woolies: {woolies}"
            )
    await bot.process_commands(message)
    
# At the end of bot.py
bot.run(os.getenv("DISCORD_TOKEN"))