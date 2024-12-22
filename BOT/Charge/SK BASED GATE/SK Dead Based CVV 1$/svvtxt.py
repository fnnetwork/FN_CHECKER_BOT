import time
import httpx
import threading
import asyncio
import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import timedelta
from .gate import *
from .response import *
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_txt import *

# Global flag to monitor stop state
stop_flag = False

async def get_checked_done_response(Client, message, ccs, key, hitsfile, start, stats, role, charged, live, chk_done):
    try:
        taken = str(timedelta(seconds=time.perf_counter() - start))
        hours, minutes, seconds = map(float, taken.split(":"))
        hour = int(hours)
        min = int(minutes)
        sec = int(seconds)
        if live != 0 or charged != 0:
            await Client.delete_messages(message.chat.id, stats.id)
            text = f"""
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED 1$ CVV ♻️

- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {len(ccs)}
- 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 - {charged}
- 𝐋𝐢𝐯𝐞 - {live}
- 𝐃𝐞𝐚𝐝 - {chk_done - charged - live }
- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - {chk_done}
- 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲 - <code>{key}</code>
- 𝐒𝐭𝐚𝐭𝐮𝐬 - Checked All ✅

- 𝗧𝗶𝗺𝗲 -  {hour}.h {min}.m {sec}.s </b>
"""
            await message.reply_document(document=hitsfile, caption=text, reply_to_message_id=message.id)

        else:
            text = f"""
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED 1$ CVV ♻️

- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {len(ccs)}
- 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 - {charged}
- 𝐋𝐢𝐯𝐞 - {live}
- 𝐃𝐞𝐚𝐝 - {chk_done - charged - live }
- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - {chk_done}
- 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲 - <code>{key}</code>
- 𝐒𝐭𝐚𝐭𝐮𝐬 - Checked All ✅

- 𝗧𝗶𝗺𝗲 -  {hour}.h {min}.m {sec}.s </b>
"""
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Stop", callback_data="stop_checking")]]
            )
            await Client.edit_message_text(message.chat.id, stats.id, text, reply_markup=keyboard)
    except:
        pass


async def get_checking_response(Client, message, ccs, key, i, start, stats, role, charged, live, chk_done):
    try:
        taken = str(timedelta(seconds=time.perf_counter() - start))
        hours, minutes, seconds = map(float, taken.split(":"))
        hour = int(hours)
        min = int(minutes)
        sec = int(seconds)
        cc = i["fullz"]
        response = i["response"]
        text = f"""
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED 1$ CVV ♻️

<code>{cc}</code>
- 𝐑𝐞𝐬𝐮𝐥𝐭 - {response}

- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {len(ccs)}
- 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 - {charged}
- 𝐋𝐢𝐯𝐞 - {live}
- 𝐃𝐞𝐚𝐝 - {chk_done - charged - live }
- 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - {chk_done}
- 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲 - <code>{key}</code>
<i>( Get Your Hits Key By "/gethits {key}" )</i>
- 𝐒𝐭𝐚𝐭𝐮𝐬 - Checked...

- 𝗧𝗶𝗺𝗲 -  {hour}.h {min}.m {sec}.s </b>
"""
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data="stop_checking")]]
        )
        await Client.edit_message_text(chat_id=message.chat.id, message_id=stats.id, text=text, reply_markup=keyboard)
    except:
        pass


async def xvvfunc(fullcc, sks, user_id, session):
    result = await create_deadsk_charge(fullcc, sks, session, user_id)
    getresp = await get_charge_resp(result, user_id, fullcc)
    return getresp


async def gcgenfunc(len=4):
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(len))


async def save_cc(i, file_name):
    try:
        cc = i["fullz"]
        response = i["response"]
        hitsfile = f"HITS/{file_name}"
        with open(hitsfile, "a", encoding="utf-8") as f:
            f.write(f"{cc}\nResult - {response}\n")
    except:
        pass


@Client.on_message(filters.command("svvtxt", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stripe_mass_txt_auth_cmd(Client, message))
    loop.close()


@Client.on_callback_query(filters.regex("stop_checking"))
async def stop_checking(client, callback_query):
    global stop_flag
    stop_flag = True
    await callback_query.message.edit_text("Checking process has been stopped.")


async def stripe_mass_txt_auth_cmd(Client, message):
    global stop_flag
    stop_flag = False  # Reset stop flag
    try:
        user_id = str(message.from_user.id)
        results = await getuserinfo(user_id)
        credit = results["credit"]
        first_name = str(message.from_user.first_name)
        checkall = await check_all_thing(Client, message)
        if checkall[0] == False:
            return

        role = checkall[1]
        try:
            random_text = await gcgenfunc(len=8)
            key = f"svvtxt_{message.from_user.id}_{random_text}"
            file_name = f"{key}.txt"
            hitsfile = f"HITS/{file_name}"
            await message.reply_to_message.download(file_name=file_name)
        except:
            resp = """<b>
Gate Name: SK BASED 1$ CVV ♻️
CMD: /svvtxt

Message: No CC Found in your input ❌

Usage: /svvtxt [ in reply to txt file ]
        </b> """
            await message.reply_text(resp, message.id)
            return

        getcc = await getcc_for_txt(file_name, role)
        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return

        ccs = getcc[1]
        user_id = str(message.from_user.id)
        results = await getuserinfo(user_id)
        credit = int(results["credit"])
        need_crt = len(ccs) - credit
        get_user_info = usersdb.find_one({"id": user_id}, {"_id": 0})
        if "∞" in get_user_info["plan"]:
            pass
        else:
            if credit < len(ccs):
                resp = f"""<b>
You have no credit, so check with less CC.. Try to Check CC under {credit}.
You need more {need_crt} Credits
If you Buy credit, then type /buy .
        </b> """
                await message.reply_text(resp, message.id)
                return

        text = f"""
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED 1$ CVV ♻️

- 𝐂𝐂 𝐀𝐦𝐨𝐮𝐧𝐭 - {len(ccs)}
- 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 - Checking CC For {first_name}
- 𝐍𝐨𝐭𝐞 - This Pop Up Will Change After 50 CC Checked . So Keep Patient .

- 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing...⌛️    """

        # Add stop button
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Stop", callback_data="stop_checking")]]
        )
        stats = await message.reply_text(text, reply_markup=keyboard)

        chk_done = 0
        charged = 0
        live = 0
        start = time.perf_counter()
        sks = await getallsk()
        session = httpx.AsyncClient(timeout=30, follow_redirects=True)
        works = [xvvfunc(i, sks, user_id, session) for i in ccs]
        worker_num = int(json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["THREADS"])

        while works:
            if stop_flag:
                await message.reply_text("Process stopped by user.", quote=True)
                break

            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                chk_done += 1
                if i["hits"] == "CHARGED":
                    charged += 1
                    await save_cc(i, file_name)

                if i["hits"] == "LIVE":
                    live += 1
                    await save_cc(i, file_name)

                if chk_done % 50 == 0:
                    await get_checking_response(Client, message, ccs, key, i, start, stats, role, charged, live, chk_done)

            works = works[worker_num:]

        await session.aclose()
        if not stop_flag:
            await get_checked_done_response(Client, message, ccs, key, hitsfile, start, stats, role, charged, live, chk_done)
            await massdeductcredit(user_id, len(ccs))
            await setantispamtime(user_id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
