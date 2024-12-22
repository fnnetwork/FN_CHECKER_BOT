import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("del", [".", "/"]))
async def cmd_del(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @amitonmoyx !</b>"""
            await message.reply_text(resp)
            return
        else:
            try:
                chat_id = str(message.text.split(" ")[1])
            except:
                chat_id = str(message.chat.id)

            getchat = await getchatinfo(chat_id)
            getchat = str(getchat)

            if getchat != "None":
                await delchat(chat_id)
                resp = f"""<b>
Group Deauthorized ❌

Group Chat ID: {chat_id}

Message: This Group (<code>{chat_id}</code>) is Successfully Deauthorized.
       </b> """
                await message.reply_text(resp)
                user_resp = f"""<b>
Deauthorized ❌

Group Chat ID: {chat_id}

Message: This Group is no longer Authorized to use Our Bot. Deauthorized By @FNxELECTRA
       </b> """
                try:
                    await Client.send_message(chat_id, user_resp)
                except:
                    pass
            else:
                resp = f"""<b>
Chat Not Found ⚠️

Group Chat ID: {chat_id}

Message: This Group (<code>{chat_id}</code>) is not in the list of authorized chats.
       </b> """
                await message.reply_text(resp)

    except Exception as e:
        await message.reply_text(str(e))
        await error_log(traceback.format_exc())
