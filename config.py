import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")

OWNER_IDS = [int(x) for x in os.getenv("OWNER_IDS","").split(",") if x]

DB_PATH = os.getenv("DB_PATH","/tmp/serena_db/bot.db")
DL_DIR = os.getenv("DL_DIR","/tmp/serena_dl")

FREE_LIMIT = int(os.getenv("FREE_LIMIT","3"))
BASIC_LIMIT = int(os.getenv("BASIC_LIMIT","15"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT","50"))

LOG_LEVEL = os.getenv("LOG_LEVEL","INFO")
PORT = int(os.getenv("PORT","10000"))