import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *

@Client.on_message(filters.command("add", [".", "/"]))
async def cmd_add(client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = (
                "<b>⛔️ Access Denied</b>\n\n"
                "<i>You do not have permission to use this command.</i>\n"
                "Please contact the bot owner @amitonmoyx for access."
            )
            await message.reply_text(resp, quote=True)
            return

        try:
            chat_id = str(message.text.split(" ")[1])
        except IndexError:
            chat_id = str(message.chat.id)

        getchat = await getchatinfo(chat_id)
        getchat = str(getchat)
        
        if getchat == "None":
            await addchat(chat_id)
            resp = (
                "<b>✅ Group Authorized</b>\n\n"
                f"<b>Group Chat ID:</b> <code>{chat_id}</code>\n\n"
                "<i>This group is now authorized to use the bot.</i>"
            )
            await message.reply_text(resp, quote=True)
            
            chat_resp = (
                "<b>✅ Authorized</b>\n\n"
                f"<b>Group Chat ID:</b> <code>{chat_id}</code>\n\n"
                "<i>This group is now authorized to use our bot. Authorized by @FNxELECTRA.</i>"
            )
            try:
                await client.send_message(chat_id, chat_resp)
            except Exception:
                pass

        else:
            find = await getchatinfo(chat_id)
            find = str(find)
            if find != "None":
                resp = (
                    "<b>⚠️ Already Authorized</b>\n\n"
                    f"<b>Group Chat ID:</b> <code>{chat_id}</code>\n\n"
                    "<i>This group is already authorized to use the bot.</i>"
                )
                await message.reply_text(resp, quote=True)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
