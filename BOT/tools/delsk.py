import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *


@Client.on_message(filters.command("delsk", [".", "/"]))
async def delbrod(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: To Perform This Action, You Need Admin Level Power. 

Contact @amitonmoyx For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        if len(message.command) != 2:
            resp = "<b>Please provide the SK key to delete.</b>"
            await message.reply_text(resp, message.id)
            return

        sk_to_delete = message.command[1]
        await delsk(sk_to_delete)

        resp = "<b>SK Key (Stripe Key) Successfully Deleted ✅</b>"
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())