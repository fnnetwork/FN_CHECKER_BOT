from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("credits", [".", "/"]))
async def cmd_credit(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = await getuserinfo(user_id)
        regdata = str(regdata)
        if regdata == "None":
            resp = f"""<b>
Unregistered Users ⚠️

Message: You Can't Use Me Unless You Register First .

Type /register to Continue
</b>"""
            await message.reply_text(resp, message.id)
            return

        getuser    = await getuserinfo(user_id)
        status     = getuser["status"]
        credit     = getuser["credit"]
        plan       = getuser["plan"]
        first_name = str(message.from_user.first_name)

        resp = f"""<b>
Name: {first_name}
Credits: {credit}
Status: {status}
Plan: {plan}

Want More ? Type /buy to Get more.
    </b>"""
        await message.reply_text(resp, message.id)
    except:
        import traceback
        await error_log(traceback.format_exc())
