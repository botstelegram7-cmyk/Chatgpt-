from pyrogram import filters
from client import app
from utils.decorators import owner_only


@app.on_message(filters.command("ping"))
@owner_only
async def ping(client, message):

    await message.reply("🏓 Pong!")
