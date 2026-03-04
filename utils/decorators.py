from functools import wraps
from config import OWNER_IDS

def owner_only(func):
    @wraps(func)
    async def wrapper(client, message):
        if message.from_user.id not in OWNER_IDS:
            return await message.reply("🚫 Owner only command")
        return await func(client, message)
    return wrapper