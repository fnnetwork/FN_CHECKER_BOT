import json
from pyrogram import Client, filters
from FUNC.defs import *

@Client.on_message(filters.command("rmvbv", [".", "/"]))
async def remove_vbv(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @amitonmoyx !</b>"""
            await message.reply_text(resp, message.id)
            return
        
        # Extract the bin to be removed
        bin_to_remove = message.text.split(' ', 1)[1].strip()
        
        with open("FILES/vbvbin.txt", "r", encoding="utf-8") as file:
            vbv_tokens = file.readlines()
        
        # Filter out lines that contain the bin to be removed
        updated_tokens = [token for token in vbv_tokens if not token.startswith(bin_to_remove)]
        
        if len(updated_tokens) == len(vbv_tokens):
            resp = f"""<b>
No matching token found for BIN: {bin_to_remove}
    </b>"""
        else:
            with open("FILES/vbvbin.txt", "w", encoding="utf-8") as file:
                file.writelines(updated_tokens)
            resp = f"""<b>
VBV_TOKEN Successfully Removed ✅
━━━━━━━━━━━━━━
BIN: {bin_to_remove}

Status: Successful
    </b>"""
        
        await message.reply_text(resp, message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Error: {str(e)}</b>", message.id)
