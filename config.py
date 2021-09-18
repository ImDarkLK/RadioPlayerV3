"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
from youtube_dl import YoutubeDL

from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://stream.zeno.fm/e646hfnqv38uv")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", "1277798523")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1316963576)
    CHAT = int(os.environ.get("CHAT", "-1001520980435"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001401314999")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "False":
        EDIT_TITLE=None
    RADIO_TITLE=os.environ.get("RADIO_TITLE", "Music 24/7 | Radio Mode")
    if RADIO_TITLE == "False":
        RADIO_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 750))
    DELAY = int(os.environ.get("DELAY", 10))
    API_ID = int(os.environ.get("API_ID", "3047095"))
    API_HASH = os.environ.get("API_HASH", "994ffa4835a9c6fb1d697bdf283addbc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2030043966:AAGxLhXyFIqv4JLjIzYJcJ4X_Q1-bRstur0")
    SESSION = os.environ.get("SESSION_STRING", "BQABYNENwi2ffvuXs4crVQOX0Nk2JpYi_a1vGC8Gh0p0qV_AW0_tw8_Is1swz0cA53A_sLSVva1QJyVLUN2nDC_dSY1nU1Zy_OB0RZQBJWl56UcO-y1NyRp7PNqLDk-w7976r6z9CaoknGjv64bra6nthEYGJxoK2eymlBPGMeqcrCckoXOoBDdavQkhm0JlC0ju93h2hFXA6n07so_0L83pAYdhNCLP4gXBULCl_94tnwZ9qs8xvrc-ZdziIuM2QxcEJ515cTWl877qzoX73hVbearQL6ZxFFPs9rshCeu_snKdbd9EnznoZpuYnpxW1yVsWoDXNyrgN6pTFyMB52-GasWa_AA")
    playlist=[]
    msg = {}

