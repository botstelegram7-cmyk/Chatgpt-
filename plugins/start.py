from pyrogram import filters
from client import app
from database import add_user


@app.on_message(filters.command("start") & ~filters.outgoing)
async def start_cmd(client, message):

    user = message.from_user

    if user:
        await add_user(user)

    await message.reply_text(
"""⋆｡° ✮ °｡⋆

-ˏˋ⋆ ᴡ ᴇ ʟ ᴄ ᴏ ᴍ ᴇ ⋆ˊˎ-

»»──── ✦ ────««

▸ Send any URL to download
▸ Supported: YouTube, Instagram, TikTok
▸ Direct files also supported

⋆ ｡˚ Serena Downloader Bot ˚｡ ⋆
"""
)
