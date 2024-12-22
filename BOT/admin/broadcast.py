import asyncio
import json
import threading
import time
from datetime import timedelta
from pyrogram import Client, filters
from FUNC.defs import *
from FUNC.usersdb_func import *


async def message_forward_xcc(original_message , user_id):
    try:
        await original_message.copy(chat_id = user_id)
        return True
    except:
        return False


@Client.on_message(filters.command("brod", [".", "/"]))
def multi(Client, message):
    t1 = threading.Thread(target=bcall, args=(Client, message))
    t1.start()


def bcall(Client, message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(brod_cmd(Client, message))
    loop.close()


async def brod_cmd(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @amitonmoyx !</b>"""
            await message.reply_text(resp, message.id)
            return
        
        original_message = message.reply_to_message
        all_user         = []
        get_user         = await getallusers()
        get_chat         = await getallchat()

        for user in get_user:
            all_user.append(int(user["id"]))

        for chat in get_chat:
            all_user.append(chat["id"])

        text = f"""<b>
Brodcast Started ✅
━━━━━━━━━━━━━━
Total Audience : {len(all_user)}

Status: Successfull</b>"""
        await message.reply_text(text, message.id)

        sent_brod  = 0
        not_sent   = 0
        start      = time.perf_counter()
        works      = [message_forward_xcc(original_message, i) for i in all_user]
        worker_num = 25

        while works:
            a = works[:worker_num]
            a = await asyncio.gather(*a)
            for i in a:
                if i == True:
                    sent_brod += 1
                else:
                    not_sent += 1

            works = works[worker_num:]
            
        taken                     = str(timedelta(seconds=time.perf_counter() - start))
        hours , minutes , seconds = map(float, taken.split(":"))
        hour                      = int(hours)
        min                       = int(minutes)

        done = f"""<b>
Brodcast Completed Successfully ✅
━━━━━━━━━━━━━━
Total Audience : {len(all_user)}
Message Sent : {sent_brod}
Failed to Sent : {not_sent}
Success Ratio : {int(sent_brod * 100 / len(all_user))}%

Time Taken : {hour} Hour {min} Min
        </b>"""

        await message.reply_text(done, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
