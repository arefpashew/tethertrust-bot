import os

from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = os.getenv(
    "8616982240:AAGVHsK0aUZ5g5Oyw5ODdyFr9UvfR4j32Do"
)


CHANNEL_ID = os.getenv(
    "CHANNEL_ID",
    "@TetherTrust_Official"
)


SUPPORT_ID = os.getenv(
    "SUPPORT_ID",
    "@TetherTrust_Support"
)


HISTORY_FILE = "history.json"


PRICE_INTERVAL = 15
