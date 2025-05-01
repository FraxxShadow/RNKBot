import os
import logging
from logging.handlers import RotatingFileHandler

settings = {
    '_id': 1,  # don't change this line only, if you do you're dying by my hand
    "SPOILER": False,  # bool write True or False
    "FILE_AUTO_DELETE": 0,  # in seconds
    "AUTO_DEL": True,  # bool write True or False
    "STICKER_ID": "CAACAgUAAyEFAASUwGgHAAIS-mgI_buDCtillVa_5WUxbaIzkO6jAAIUAgACaoQ8NozqxwvIcaGdNgQ",
    "stk_del_timer": 5, # in seconds
    "bot_admin": [7086472788] #e.g. 1963929292,38739292827 differetiate admins with a comma
}

HELP_MSG = """help msg
"""

TG_BOT_TOKEN = '7696888023:AAEI5zizXTD1xq7xAnwTYC7iET8wOnja4xI'
APP_ID = int(os.environ.get("APP_ID", "28744454"))

API_HASH = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")

DB_CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1002415067779")

OWNER = os.environ.get("OWNER", "𝗘𝗥𝗔 『𝗗𝗔𝗥𝗞𝗫𝗦𝗜𝗗𝗘』 ♪")

OWNER_ID = 7086472788

SUDO = []
if OWNER_ID not in SUDO:
    SUDO.append(OWNER_ID)

# Port
PORT = os.environ.get("PORT", "8000")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "RNK")

# FSUBS configuration
FSUBS = [
    {'_id': -1002513795136, "CHANNEL_NAME": "𝘙𝘕𝘒 𝘈𝘕𝘐𝘔𝘌"}
]

START_MSG = os.environ.get("START_MESSAGE","<blockquote><b>ʙᴀᴋᴀ!!! </b><b>{mention}</b>\n<b>ɪ ᴀᴍ <a href='https://t.me/TheNamiRobot'>ɴᴀᴍɪ</a>, ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ </b><b><a href='https://t.me/AnimeMonth'>𝘈𝘯𝘪𝘮𝘦𝘔𝘰𝘯𝘵𝘩</a> ᴛᴏ ꜱʜᴀʀᴇ ᴀɴɪᴍᴇ ᴛᴏ ᴀ ʟᴀʀɢᴇ ɴᴜᴍʙᴇʀ </b><b>ᴏꜰ ꜰᴀɴꜱ ᴠɪᴀ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋꜱ...</blockquote>\n</b><blockquote><b>Pᴏᴡᴇʀᴇᴅ ʙʏ: <a href='https://t.me/RNK_Anime'>RNK Anime</a></b></blockquote>")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "8"))

# Start message
ADMINS = []
# Add other admin IDs here as needed, ensuring not to include OWNER_ID
other_admin_ids = []  # Replace with actual admin IDs
for admin_id in other_admin_ids:
    if admin_id != OWNER_ID:
        ADMINS.append(admin_id)

# Ensure OWNER_ID is not duplicated
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = None

# Set True if you want to prevent users from forwarding files from the bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Set true if you want to disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = True  # True or None

BOT_STATS_TEXT = "<blockquote><b>BOT UPTIME</b>\n{uptime}</blockquote>"
USER_REPLY_TEXT = "<blockquote><b>ɢɪᴠᴇ ᴍᴇ ᴏɴᴇ ʙɪʟʟɪᴏɴ ʙᴇʀʀɪᴇꜱ ᴀɴᴅ ɪ ᴡɪʟʟ ꜱᴛᴀʀᴛ ᴡᴏʀᴋɪɴɢ ꜰᴏʀ ʏᴏᴜ... ɴᴇxᴛ ᴏᴡɴᴇʀ</b></blockquote>"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
