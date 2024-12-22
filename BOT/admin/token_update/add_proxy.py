import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *

@Client.on_message(filters.command("addproxy", [".", "/"]))
async def addbrod(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return

        proxy      = str(message.reply_to_message.text)
        clear_file = open('FILES/proxy.txt', 'w',encoding="UTF-8").close()
        with open("FILES/proxy.txt", "a",encoding="UTF-8") as f:
            f.write(proxy)

        resp = f"""<b>
Proxy Successfully Added ✅
━━━━━━━━━━━━━━
{proxy}

Total Proxy Count: {len(proxy.splitlines())}
    </b>"""
        await message.reply_text(resp, message.id)
        
    except:
        import traceback
        await error_log(traceback.format_exc())