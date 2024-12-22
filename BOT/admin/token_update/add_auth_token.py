import json
from pyrogram import Client, filters
from FUNC.defs import *

async def update_api_token(TOKEN_NAME , TOKEN):
    TOKEN_DB.update_one({"id": TOKEN_NAME}, {"$set": {"api_key": TOKEN}})


@Client.on_message(filters.command("addauthtoken", [".", "/"]))
async def addauthtoken(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return

        AUTH_TOKEN = str(message.reply_to_message.text)
        await update_api_token("AUTH_TOKEN", AUTH_TOKEN)

        resp = f"""<b>
Auth API Token Successfully Added ✅
━━━━━━━━━━━━━━
{AUTH_TOKEN}

Status: Successfull
    </b>"""
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
