import httpx
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
import asyncio
import time


@Client.on_message(filters.command("skuser", [".", "/"]))
async def cmd_skuser(client, message):
    try:
        checkall = await check_all_thing(client, message)
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

        asyncio.create_task(auto_reload_and_send(sk, message))

    except Exception as e:
        await error_log(f"Error in cmd_skuser: {e}")


async def get_charges(sk, start_index, end_index):
    session = httpx.AsyncClient()
    headers = {"Authorization": f"Bearer {sk}"}

    try:
        charges_response = await session.get("https://api.stripe.com/v1/charges", headers=headers)
        charges_data = charges_response.json()
    except Exception as e:
        await error_log(f"Error fetching charges: {e}")
        return []

    return charges_data.get('data', [])[start_index:end_index]


async def send_skuser_info(sk, start_index=0, end_index=10):
    charges_info = "SK USERS\n\n"
    charge_count = 0

    charges_batch = await get_charges(sk, start_index, end_index)
    for charge in charges_batch:
        charge_count += 1
        description = charge['description'] if charge['description'] else 'N/A'
        if description != 'N/A':
            charges_info += f"{charge_count}. {description}\n\n"

    return charges_info


async def auto_reload_and_send(sk, message, max_refresh=10):
    sent_message = await message.reply_text(
        f"""<b>
SK USER INFO FETCHED SUCCESSFULLY ✅
━━━━━━━━━━━━━━ 
SK:➺ 
<code>{sk}</code>

Loading...

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=7593550190">𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
        </b> """
    )

    refresh_count = 0
    while refresh_count < max_refresh:
        try:
            charges_info = await send_skuser_info(sk)
            current_time = time.strftime("%H:%M:%S", time.gmtime())
            last_updated = 'Refresh Reached' if refresh_count == max_refresh - 1 else current_time
            await sent_message.edit_text(
                f"""<b>
SK USER INFO FETCHED SUCCESSFULLY ✅
━━━━━━━━━━━━━━ 
SK:➺ 
<code>{sk}</code>

{charges_info}

Last Updated: {last_updated}

Checked By <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 
Bot by - <a href="tg://user?id=6745804180">Toͥnmͣoͫy</a>
                    </b> """
            )
            refresh_count += 1
        except Exception as e:
            await error_log(f"Error in auto_reload_and_send: {e}")

        await asyncio.sleep(2)
