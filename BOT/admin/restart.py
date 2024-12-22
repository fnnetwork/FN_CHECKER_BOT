import os
import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *

@Client.on_message(filters.command("restart", [".", "/"]))
async def cmd_reboot(client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        
        if user_id not in OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: To perform this action, you need admin level power. 

Contact @amitonmoyx For More Info ✅</b>"""
            await message.reply_text(resp, message.id)
            return

        await message.reply_text("Clearing cache files and rebooting the system...")
        
        os.system("python3 /root/new/cache_clear.py")
        
        os.system("sudo reboot")

    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        import traceback
        await error_log(traceback.format_exc())
