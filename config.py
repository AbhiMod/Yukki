import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","27733303"))
API_HASH = getenv("API_HASH","c3c9d5e5d89c99fb8bb85a22a0cb5a26")
BOT_TOKEN = getenv("BOT_TOKEN","1240287427:AAHNe5UPVag08IdI615i-VhHzqv30ncbiPY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "sultan11100")
BOT = getenv("BOT", "Anie X Yukki")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.9ztuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "99999999999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001971806089"))
OWNER_ID = int(getenv("OWNER_ID", "2105971379"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiMod/Yukki",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+jCS-YsVBVEE3NjQ1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+jCS-YsVBVEE3NjQ1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION","BQBpi-e5VltFQ1oCaatvhW3-jZObv7L7t33Os3FHAtlabRMZl7QklWc3Ay2LApQczgmwNWb0kRQlEczlCnusJvlX9rpXyHkVJ60uDmnhGtZlpSehTl8A90SX5Xg9vconvhwVtSjvWdx6yYC99v6wiTSTGjaw4MMetYhyg_-3oBySybY2aNEFDxkbbWzf6o_Exqg6wAYrCg6Rhqq82mtBXiGNVAiu9bz3UGRzGVfY-IkQ4DF6FAHbLcM18fFKdsFc4NFfnh3lBJ84-UzspyFYfAZJNGuCd0bIkBWt-Ek_jm2YkfH-vw9yZPasmZ0vaPiRcrWzEv9vl0dAMrMm4N_P0WR5AAAAAXkXdo8A")
STRING2 = getenv("STRING_SESSION2",None)
STRING3 = getenv("STRING_SESSION3",None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/581b45c9ca4ca334bc665.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/581b45c9ca4ca334bc665.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/581b45c9ca4ca334bc665.jpg"
STATS_IMG_URL = "https://graph.org/file/581b45c9ca4ca334bc665.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/581b45c9ca4ca334bc665.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/581b45c9ca4ca334bc665.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/581b45c9ca4ca334bc665.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
