import aiosqlite
import os
from config import DB_PATH

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


async def init_db():

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            full_name TEXT,
            plan TEXT DEFAULT 'free',
            daily_count INTEGER DEFAULT 0,
            joined_at TEXT
        )
        """)

        await db.commit()


async def add_user(user):

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute(
            """
            INSERT OR IGNORE INTO users
            (user_id, username, full_name, joined_at)
            VALUES (?, ?, ?, datetime('now'))
            """,
            (user.id, user.username, user.first_name)
        )

        await db.commit()
