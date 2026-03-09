import asyncio

# Ensure a running loop exists for Pyrogram
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.userbot import Userbot

app = VIPBot()
userbot = Userbot()
