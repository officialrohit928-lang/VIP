import asyncio

# Create and set event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.userbot import Userbot

app = VIPBot()
userbot = Userbot()
