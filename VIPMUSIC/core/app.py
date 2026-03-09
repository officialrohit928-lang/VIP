import asyncio

asyncio.set_event_loop(asyncio.new_event_loop())

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.userbot import Userbot

app = VIPBot()
userbot = Userbot()
