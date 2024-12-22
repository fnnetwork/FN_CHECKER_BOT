import json
import time
import threading
import asyncio
import httpx
from pyrogram import Client, filters
from datetime import timedelta
from FUNC.usersdb_func import *
from FUNC.defs import *
from TOOLS.check_all_func import *
from TOOLS.getcc_for_mass import *

async def masscvvfunc(fullcc, user_id, session, bin_status):
    try:
        bin_number = fullcc.split('|')[0][:6]
        if bin_number.startswith("3"):
            status = "Card Error"
            response = "Unsupported card type."
        elif bin_number in bin_status:
            status = bin_status[bin_number]["status"]
            response = bin_status[bin_number]["response"]
        else:
            status = "Unknown"
            response = "No Response"

        return f"Card↯ <code>{fullcc}</code>\n<b>Status - {status}</b>\n<b>Result -⤿ {response} ⤾</b>\n\n"
    except Exception:
        import traceback
        await error_log(traceback.format_exc())
        return f"<code>{fullcc}</code>\n<b>Result - Lookup Error ❌</b>\n"

@Client.on_message(filters.command("mvbv", [".", "/"]))
def multi(client, message):
    t1 = threading.Thread(target=bcall, args=(client, message))
    t1.start()

def bcall(client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(stripe_mass_auth_cmd(client, message))
    loop.close()

async def stripe_mass_auth_cmd(client, message):
    try:
        user_id = str(message.from_user.id)
        first_name = str(message.from_user.first_name)

        checkall = await check_all_thing(Client, message)

        if checkall[0] == False:
            return

        role = checkall[1]
        getcc = await getcc_for_mass(message, role)
        if getcc[0] == False:
            await message.reply_text(getcc[1], message.id)
            return

        ccs = getcc[1]

        if len(ccs) > 25:
            await message.reply_text(f"Error: The maximum number of CC entries allowed is 25. You provided {len(ccs)}.", message.id)
            return

        bin_numbers = [cc.split('|')[0][:6] for cc in ccs]

        processing_msg = "Processing your request..."
        nov = await message.reply_text(processing_msg, message.id)
        with open("FILES/vbvbin.txt", "r", encoding="utf-8") as file:
            vbv_data = file.readlines()

        bin_status = {}
        for bin in bin_numbers:
            bin_found = False
            for line in vbv_data:
                if line.startswith(bin):
                    bin_found = True
                    parts = line.strip().split('|')
                    bin_status[bin] = {
                        "status": parts[1],
                        "response": parts[2]
                    }
                    break
            if not bin_found:
                bin_status[bin] = {
                    "status": "Error",
                    "response": "Lookup Card Error"
                }

        text = f"""
MASS VBV CHECK [/mvbv]

Number Of CC Check : [{len(ccs)} / 25]
\n"""
        amt = 0
        start = time.perf_counter()
        async with httpx.AsyncClient(timeout=30, follow_redirects=True) as session:
            works = [masscvvfunc(i, user_id, session, bin_status) for i in ccs]
            worker_num = int(json.loads(open("FILES/config.json", "r", encoding="utf-8").read())["THREADS"])

            while works:
                a = works[:worker_num]
                a = await asyncio.gather(*a)
                for i in a:
                    amt += 1
                    text += i
                    if amt % 5 == 0:
                        try:
                            await client.edit_message_text(message.chat.id, nov.id, text)
                        except Exception:
                            pass
                await asyncio.sleep(1)
                works = works[worker_num:]

        taken = str(timedelta(seconds=time.perf_counter() - start))
        hours, minutes, seconds = map(float, taken.split(":"))
        hour = int(hours)
        min = int(minutes)
        sec = int(seconds)

        text += f"""
𝗧𝗶𝗺𝗲 ⇾ {time.perf_counter() - start:0.2f} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀
"""
        await client.edit_message_text(message.chat.id, nov.id, text)
        await massdeductcredit(user_id, len(ccs))
        await setantispamtime(user_id)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())
