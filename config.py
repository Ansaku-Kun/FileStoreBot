import os

API_ID = int(os.environ.get("14330679", 0))
API_HASH = os.environ.get("2538f84ebb078c08228934552ec603ec", None)
BOT_TOKEN = os.environ.get("6891969964:AAFsviVRAHONUgcC7lnEALfC-R5IV8ozFTM", None)
DB_CHANNEL_ID = os.environ.get("2096075327")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("1224669766"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
