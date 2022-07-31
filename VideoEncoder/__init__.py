from telethon import TelegramClient
from decouple import config
import logging
import os
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Basics
api_id = 7405235
api_hash = "5c9541eefe8452186e9649e2effc1f3f"

try:
    bot_token = config("BOT_TOKEN", default=None)
    mongo = config("MONGO_URL", default= "mongodb+srv://s1com:s1com@cluster0.wrrwz.mongodb.net/Cluster0?retryWrites=true&w=majority")
except Exception as e:
    logging.warning(e)
    exit(0)


data = []
download_dir = "downloads/"
if not os.path.isdir(download_dir):
    os.makedirs(download_dir)

try:
    mongo_db = AsyncIOMotorClient(mongo)
except Exception as e:
    logging.warning(e)
    exit(0)

bot_db = mongo_db["VideoEncoder"]

try:
    BotzHub = TelegramClient("BotzHub", api_id, api_hash).start(bot_token=bot_token)
except Exception as e:
    logging.info(f"Error\n{e}")
    exit(0)
