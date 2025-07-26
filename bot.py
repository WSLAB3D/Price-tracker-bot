@bot.event
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