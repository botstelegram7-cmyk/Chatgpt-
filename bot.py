import asyncio
import logging

from client import app
from web.app import start_web
from database import init_db

# Import plugins BEFORE start (CRITICAL RULE)
import plugins.start
import plugins.download
import plugins.admin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("serena-bot")


async def main():

    logger.info("Starting Serena Downloader Bot...")

    # Initialize database
    await init_db()

    # Start bot
    await app.start()

    logger.info("Bot started successfully")

    # Keep running
    await asyncio.Event().wait()


if __name__ == "__main__":

    # Start web server (Render health check)
    start_web()

    asyncio.run(main())
