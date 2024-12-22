import json
from .func import *
from pyrogram import Client, filters
from FUNC.defs import error_log


@Client.on_message(filters.command("getplan2", [".", "/"]))
async def cmd_getplan2(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>
You Don't Have Permission To Use This Command.    
Contact Bot Owner @amitonmoyx !

</b>"""
            await message.reply_text(resp, message.id)
            return 
        try:
            amt = int(message.text.split(" ")[1])
        except:
            amt = 10

        text = f"""<b>Giftcode Genarated ✅
Amount: {amt}\n</b>"""
        
        for _ in range(amt):
            GC = f"GRAND-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}-PAA"
            await insert_plan2(GC)
            text += f"""
➔ <code>{GC}</code>
<b>Value : Silver Plan 15 Days</b>\n"""

        text += f"""
<b>For Redeemtion 
Type /redeem FN-XXXX-XXXX-XXXX-CHECKER</b>"""
        
        await message.reply_text(text, message.id)
    except:
        import traceback
        await error_log(traceback.format_exc())
