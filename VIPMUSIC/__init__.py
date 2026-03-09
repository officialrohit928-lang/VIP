import json
import os

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.dir import dirr
from VIPMUSIC.core.git import git
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.platforms.youtube import vipboy
from VIPMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()

git()

dbb()

heroku()

sudo()

app = VIPBot()

userbot = Userbot()

from VIPMUSIC.platforms import (
    YouTubeAPI,
    CarbonAPI,
    SpotifyAPI,
    AppleAPI,
    RessoAPI,
    SoundAPI,
    TeleAPI
)

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
