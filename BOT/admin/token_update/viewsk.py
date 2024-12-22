import traceback, json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *


@Client.on_message(filters.command("viewsk", [".", "/"]))
async def viewsk(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return

        sks     = await getallsk()
        amt_sk  = 0
        sk_text = ""

        for sk in sks:
            amt_sk += 1
            sk_text += f"{amt_sk}.{sk}\n"
        resp = f"""<b>
Current SK Keys Retrieved Successfully ✅
━━━━━━━━━━━━━━ 
{sk_text}

Total SK Amount : {len(sks)}
        </b>"""

        await message.reply_text(resp, message.id)

    except Exception as e:
        await message.reply_text(e, message.id)
        await error_log(traceback.format_exc())
