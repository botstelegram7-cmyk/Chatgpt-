from pyrogram import filters
from client import app
from downloader.core import download


@app.on_message(filters.text & ~filters.command(["start","ping"]) & ~filters.outgoing)
async def handle_url(client, message):

    url = message.text.strip()

    msg = await message.reply("⏬ Downloading...")

    try:

        file_path = download(url)

        await message.reply_document(file_path)

        await msg.delete()

    except Exception as e:

        await msg.edit(f"❌ Error:\n{e}")
