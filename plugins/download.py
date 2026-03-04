from pyrogram import filters
from client import app
from downloader.core import download

@app.on_message(~filters.outgoing & filters.text)
async def handle_url(client, message):
    url = message.text.strip()
    msg = await message.reply("Downloading...")
    try:
        file = download(url)
        await message.reply_document(file)
        await msg.delete()
    except Exception as e:
        await msg.edit(f"Error: {e}")