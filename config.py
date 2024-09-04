from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27896987"))
API_HASH = getenv("API_HASH", "0e017f716c49a52a0ba4a8bfa95ccaf7"))

BOT_TOKEN = getenv("BOT_TOKEN", "7223926558:AAH-0Z2AIcyI6W3g8F-SuV06gBMzc07G_xM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Matrixx_official")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Matrixx_official")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7067559685").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
