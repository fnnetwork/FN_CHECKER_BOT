import httpx
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *

@Client.on_message(filters.command("skinfo", [".", "/"]))
async def cmd_bin(Client, message):
    try:
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]
        try:
            sk = message.text.split(" ")[1]
        except IndexError:
            resp = """<b>
Invalid SK ⚠️

Message: Not Found Any Valid SK From Your Input.
            </b>"""
            await message.reply_text(resp)
            return

        skinfo = None
        session = httpx.AsyncClient()
        try:
            headers = {
                "Authorization": f"Bearer {sk}"
            }
            # Fetch SK info
            skinfo_response = await session.get("https://api.stripe.com/v1/account", headers=headers)
            skinfo = skinfo_response.json()

            # Fetch balance info
            balance_response = await session.get("https://api.stripe.com/v1/balance", headers=headers)
            balance_info = balance_response.json()
        except Exception as e:
            await error_log(str(e))
            resp = """<b>
Error fetching SK info ⚠️

Message: Unable to fetch SK info. Check if the SK is valid.
            </b>"""
            await message.reply_text(resp)
            return
        finally:
            await session.aclose()

        charges_enabled = skinfo.get("charges_enabled", False)

        if charges_enabled:
            # If charges are enabled, call the addsk function
            await addsk(sk)

        url = skinfo.get("business_profile", {}).get("url", "N/A")
        name_data = skinfo.get("business_profile", {}).get("name", "N/A")
        currency = skinfo.get("default_currency", "N/A").upper()
        country = skinfo.get("country", "N/A")
        email = skinfo.get("email", "N/A")
        available_balance = balance_info.get("available", [{}])[0].get("amount", "N/A")
        pending_balance = balance_info.get("pending", [{}])[0].get("amount", "N/A")
        livemode = balance_info.get("livemode", False)

        resp = f"""<b>SK Info Fetched Successfully ✅</b>
━━━━━━━━━━━━━━
🔑 <b>SK:</b> <code>{sk}</code>
🏢 <b>Name:</b> {name_data}
🌐 <b>Site Info:</b> {url}
🌍 <b>Country:</b> {country}
💱 <b>Currency:</b> {currency}
📧 <b>Email:</b> {email}
💰 <b>Balance Info:</b>
   - Live Mode: {livemode}
   - Charges Enabled: {charges_enabled}
   - Available Balance: {available_balance}
   - Pending Balance: {pending_balance}
━━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [ {role} ]
<b>Bot by:</b> <a href="tg://user?id=7593550190">𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
"""
        await message.reply_text(resp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
