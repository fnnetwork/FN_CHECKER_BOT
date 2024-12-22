import json
from pyrogram import Client, filters
from FUNC.defs import *

@Client.on_message(filters.command("addvbv", [".", "/"]))
async def addvbv(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @amitonmoyx !</b>"""
            await message.reply_text(resp, message.id)
            return
        
        new_token = message.text.split(' ', 1)[1].strip()
        new_bin = new_token.split('|')[0].strip()
        
        with open("FILES/vbvbin.txt", "r", encoding="utf-8") as file:
            vbv_tokens = file.readlines()
        
        token_exists = False
        full_match = False
        updated_tokens = []
        for token in vbv_tokens:
            token_bin = token.split('|')[0].strip()
            if token_bin == new_bin:
                if token.strip() == new_token:
                    full_match = True
                token_exists = True
            else:
                updated_tokens.append(token)
        
        if full_match:
            resp = f"""<b>
The token is already added: {new_token}
    </b>"""
        else:
            updated_tokens.append(new_token + '\n')
            with open("FILES/vbvbin.txt", "w", encoding="utf-8") as file:
                file.writelines(updated_tokens)
            resp = f"""<b>
VBV_TOKEN Successfully Added ✅
━━━━━━━━━━━━━━
{new_token}

Status: Successful
    </b>"""
        
        await message.reply_text(resp, message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Error: {str(e)}</b>", message.id)
