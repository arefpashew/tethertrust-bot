import os import logging
from telegram import Bot from telegram.error import InvalidToken, TelegramError
=========================
Logging Configuration
=========================
logging.basicConfig( level=logging.INFO, format=”%(asctime)s - %(levelname)s - %(message)s” )
logger = logging.getLogger(name)
=========================
Telegram Configuration
=========================
BOT_TOKEN = os.getenv(“BOT_TOKEN”, “”).strip()
CHANNEL_ID = “@TetherTrust_Official”
=========================
Telegram Service
=========================
class TelegramService:
def __init__(self):

    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN is missing! "
            "Please configure BOT_TOKEN in Railway Variables."
        )

    if ":" not in BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN format is invalid. "
            "Please check your BotFather token."
        )

    try:

        self.bot = Bot(
            token=BOT_TOKEN
        )

        logger.info("Telegram Bot initialized successfully.")

    except InvalidToken:
        logger.error(
            "Invalid Telegram BOT_TOKEN. "
            "Check your Railway Variables."
        )
        raise

# =========================
# Send Message
# =========================

async def send_message(self, text):

    if not text:
        logger.warning("Empty Telegram message. Skipping.")
        return False

    try:

        await self.bot.send_message(
            chat_id=CHANNEL_ID,
            text=str(text)
        )

        logger.info(
            "Telegram message sent successfully."
        )

        return True

    except TelegramError as error:

        logger.error(
            "Telegram API Error: %s",
            error
        )

        return False

    except Exception:

        logger.exception(
            "Unexpected error while sending Telegram message."
        )

        return False

# =========================
# Close Bot Session
# =========================

async def close(self):

    try:

        await self.bot.shutdown()

        logger.info(
            "Telegram Bot session closed."
        )

    except Exception:

        logger.exception(
            "Error closing Telegram Bot session."
        )
=========================
Global Instance
=========================
telegram_service = TelegramService()
