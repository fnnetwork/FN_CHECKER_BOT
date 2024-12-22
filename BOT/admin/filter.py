import httpx
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *
import re
import os


@Client.on_message(filters.command("fl", [".", "/"]))
async def filter(Client, message):
    try:
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]

        input_text = None
        if message.reply_to_message:
            input_text = message.reply_to_message.text
        else:
            input_text = message.text[len('/fl'):]

        if message.reply_to_message and message.reply_to_message.document:
            file = await message.reply_to_message.download()
            with open(file, 'r') as f:
                input_text = f.read()
            os.remove(file)

        if input_text:
            all_cards = input_text.split('\n')
        else:
            all_cards = []

        cards = ""
        for cc in all_cards:
            try:
                x = re.findall(r'\d+', cc)
                ccn = x[0]
                mm = x[1]
                yy = x[2]
                cvv = x[3]
                if mm.startswith('2'):
                    mm, yy = yy, mm
                if len(mm) >= 3:
                    mm, yy, cvv = yy, cvv, mm
                if len(ccn) < 15 or len(ccn) > 16:
                    pass
                else:
                    cards += f"{ccn}|{mm}|{yy}|{cvv}\n"
            except:
                pass

        if cards:
            if len(cards.split('\n')) >= 32:
                with open('MASTERϟFiltered.txt', 'w') as file:
                    file.write(cards)
                await message.reply_document('MASTERϟFiltered.txt', quote=True)
                os.remove('MASTERϟFiltered.txt')
            else:
                await message.reply_text(f"""<code>{cards}</code>""", quote=True)
        else:
            resp = """<b>
Filter Failed ⚠️

Message: No Valid CC Found in the Input.
            </b>"""
            await message.reply_text(resp, quote=True)

    except Exception as e:
        print("Error:", str(e))
