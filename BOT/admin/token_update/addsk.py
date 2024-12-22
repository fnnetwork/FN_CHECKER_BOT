import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *


@Client.on_message(filters.command("skadd", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return
        
        await addsk(message.reply_to_message.text)
        resp = f"""<b>
SK Key ( Stripe Key ) Successfully Added ✅
━━━━━━━━━━━━━━
{message.reply_to_message.text}

Status: Successfull
    </b>"""
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())




import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *

@Client.on_message(filters.command("addsk", [".", "/"]))
async def update_live_sk_key(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perform This Action, You Need Admin Level Power. 

Contact @amitonmoyx For More Info ✅</b>"""
            await message.reply_text(resp)
            return

        new_sk_key = str(message.reply_to_message.text)

        with open("FILES/deadsk.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        data["LIVE_SK"] = new_sk_key

        with open("FILES/deadsk.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4)

        resp = f"""<b>
SK Key ( Stripe Key ) Successfully Added ✅
━━━━━━━━━━━━━━
{message.reply_to_message.text}

Status: Successfull
    </b>"""
        await message.reply_text(resp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())


