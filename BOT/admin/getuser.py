import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("get", [".", "/"]))
async def cmd_add(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return

        info     = await getuserinfo(message.text.split(" ")[1])
        status   = info["status"]
        plan     = info["plan"]
        expiry   = info["expiry"]
        credit   = info["credit"]
        totalkey = info["totalkey"]
        reg_at   = info["reg_at"]

        send_info = f"""<b>
<b>{message.text.split(" ")[1]}</b> Info on MASTER Checker ⚡
━━━━━━━━━━━━━━
● ID: <code>{message.text.split(" ")[1]}</code>
● Profile Link: <a href="tg://user?id={message.text.split(" ")[1]}">Profile Link</a>
● Status: {status}
● Credit: {credit}
● Plan: {plan}
● Plan Expiry: {expiry}
● Key Redeemed : {totalkey}
● Registered at: {reg_at}</b>
"""
        await message.reply_text(send_info, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
