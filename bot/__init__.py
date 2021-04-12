import os
import logging

class Config:

    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")

     # Sql Database url
    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    # the download location, where the HTTP Server runs
    DOWNLOAD_DIRECTORY = "./DOWNLOADS"

    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", "")

    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", "")
  
    SUDO_USERS = []
    
    SUPPORT_CHAT_LINK = "https://t.me/HxSupport"
    


logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

