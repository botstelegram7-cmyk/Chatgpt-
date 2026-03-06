import asyncio
import logging
from pyrogram import idle

from client import app
from web.app import start_web
from database import init_db

# Import plugins BEFORE start
import plugins.start
import plugins.download
import plugins.admin


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("serena-bot")


async def main():

    logger.info("Initializing database...")
    await init_db()

    logger.info("Starting Pyrogram client...")
    await app.start()

    logger.info("Bot started successfully")

    # This is required for receiving updates
    await idle()

    logger.info("Stopping bot...")
    await app.stop()


if __name__ == "__main__":

    # Start Render web server
    start_web()

    asyncio.run(main())
