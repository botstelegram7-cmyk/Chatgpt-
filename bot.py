import asyncio
import logging

from client import app
from web.app import start_web
from database import init_db

# Import plugins BEFORE start
import plugins.start
import plugins.download
import plugins.admin


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("serena-bot")


async def run_bot():

    logger.info("Initializing database...")
    await init_db()

    logger.info("Starting Pyrogram client...")
    await app.start()

    logger.info("Bot started successfully")

    # Keep bot alive
    await asyncio.Event().wait()


if __name__ == "__main__":

    # Start Render web server
    start_web()

    # Run bot loop
    asyncio.run(run_bot())
