from pyrogram import Client, filters
from FUNC.defs import *


@Client.on_message(filters.command("howgp", [".", "/"]))
async def cmd_howgp(Client, message):
    try:
        texta = f"""<b>
TO THIS ADD THIS BOT TO YOUR GROUP -

Requirements: <b>Your Group Must Have Atleast 50 Members.</b>

Steps To Get Your Group Authorised:
➔ Add @MASTER_checker_bot To Your Group As Admin .
➔ Copy Your Group Username or Group Invite Link .
➔ Knock @FNxELECTRA And Give Him The Group Username or Group Invite Link

Thats It . Now Once He is got online , He will Approved Your Group ✅ .
</b>"""
        await message.reply_text(texta, message.id)

    except Exception as e:
        import traceback

        await error_log(traceback.format_exc())
