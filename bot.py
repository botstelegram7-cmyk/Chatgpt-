import asyncio
import logging
from client import app
from web.app import start_web
from config import LOG_LEVEL

# Import plugins BEFORE start (CRITICAL RULE)
import plugins.start
import plugins.download
import plugins.admin

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("serena-bot")

async def main():
    logger.info("Starting Serena Downloader Bot...")
    await app.start()
    logger.info("Bot started successfully")
    await asyncio.Event().wait()

if __name__ == "__main__":
    start_web()
    asyncio.run(main())