import json
from pyrogram import Client

with open("FILES/config.json", "r",encoding="utf-8") as f:
    DATA         = json.load(f)
    API_ID       = DATA["API_ID"]
    API_HASH     = DATA["API_HASH"]
    BOT_TOKEN    = DATA["BOT_TOKEN"]
    PHONE_NUMBER = DATA["PHONE_NUMBER"]

user = Client("Scrapper",
              api_id       = API_ID,
              api_hash     = API_HASH ,
              phone_number = PHONE_NUMBER
              )

user.start()


