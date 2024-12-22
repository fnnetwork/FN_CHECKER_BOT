from pyrogram import Client, filters


@Client.on_message(filters.command("getuser", [".", "/"]))
async def cmd_getuser(client, message):
    try:
        user = message.text.split(" ")[1]
    except IndexError:
        resp = """<b>
Usage:
/getuser id_or_username
        </b>"""
        await message.reply_text(resp, quote=True)
        return

    try:
        get         = await client.get_users(user)
        name        = get.first_name
        id          = get.id
        username    = get.username
        restriction = get.restriction_reason
        scam        = get.scam
        premium     = get.is_premium

        resp = f"""<b>
🔍 Info of '{user}' on Telegram
━━━━━━━━━━━━━━
👤 First Name: {name}
🆔 ID: {id}
📛 Username: @{username}
🔗 Profile Link: <a href="tg://user?id={id}">Profile Link</a>
🔒 TG Restrictions: {restriction}
🚨 TG Scamtag: {scam}
🌟 TG Premium: {premium}
        </b>"""
        await message.reply_text(resp, quote=True)

    except Exception:
        try:
            await message.reply_text("<b>Invalid Username or Incorrect ID ❌</b>", quote=True)
        except Exception:
            pass
