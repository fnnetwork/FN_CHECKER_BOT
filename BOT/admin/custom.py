import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("cs", [".", "/"]))
async def cmd_cs(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return

        user_id , module , value = message.text.split(" ")
        await updateuserinfo(user_id, module, value)

        resp = f"""<b>
Custom Info Changed ✅
━━━━━━━━━━━━━━
User_ID : {user_id}
Key_Name : {module}
Key_Value : {value}

Status: Successfull
</b> """
        await message.reply_text(resp, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
