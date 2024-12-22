import traceback
from pyrogram import Client, filters
from FUNC.usersdb_func import *
import asyncio
import pymongo
import json
from mongodb import client, folder
from pathlib import Path
import time

users_db = folder.USERSDB
chats_auth_db = folder.CHATS_AUTH
gc_db = folder.GCDB


@Client.on_message(filters.command("import", [".", "/"]))
async def stats(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            msg1 = await message.reply_text(resp, message.id)
        else:
            try:
                file_name = "import.json"
                await message.reply_to_message.download(file_name=file_name)
                all_data = (
                    open("downloads/import.json", "r", encoding="UTF-8")
                    .read()
                    .splitlines()
                )
                data_list = []
                amt = 0
                for i in all_data:
                    amt += 1
                    data = json.loads(i)
                    data_list.append(data)
                getfile = True
            except Exception as e:
                getfile = False
            if getfile == True:
                try:
                    msg = message.text.split(" ")[1]
                    status = True
                except:
                    status = False
                    resp = f"""<b>
Wrong Format ❌

Usage:
For Users Data Import : /import users
For Chats Data Import : /import chats
For GC Data Import : /import gc
                   </b> """
                    await message.reply_text(resp, message.id)
                if "users" in msg and status == True:
                    try:
                        resp = "<b>IMPORTING TO XCC DATABASE...</b>"
                        delete = await message.reply_text(resp, message.id)
                        start = time.time()
                        insert = users_db.insert_many(data_list)
                        end = time.time()
                        await Client.delete_messages(message.chat.id, delete.id)
                        resp = f"""<b>
IMPORT DONE ✅

Total Number: {amt}
Data Type: JSON
Last Updated: a while ago
Time Taken: {end - start:0.4f}s
Requested Time: {message.date}
                        </b>"""
                        await message.reply_text(resp, message.id)
                        if insert:
                            name = "downloads/import.json"
                            my_file = Path(name)
                            my_file.unlink()
                    except:
                        await message.reply_text("ERROR HAPPEND IMPORTING", message.id)
                elif "chats" in msg and status == True:
                    try:
                        resp = "<b>IMPORTING TO XCC DATABASE...</b>"
                        delete = await message.reply_text(resp, message.id)
                        start = time.time()
                        insert = chats_auth_db.insert_many(data_list)
                        end = time.time()
                        await Client.delete_messages(message.chat.id, delete.id)
                        resp = f"""<b>
IMPORT DONE ✅

Total Number: {amt}
Data Type: JSON
Last Updated: a while ago
Time Taken: {end - start:0.4f}s
Requested Time: {message.date}
                        </b>"""
                        await message.reply_text(resp, message.id)
                        if insert:
                            name = "downloads/import.json"
                            my_file = Path(name)
                            my_file.unlink()
                    except:
                        await message.reply_text("ERROR HAPPEND IMPORTING", message.id)
                elif "gc" in msg and status == True:
                    try:
                        resp = "<b>IMPORTING TO XCC DATABASE...</b>"
                        delete = await message.reply_text(resp, message.id)
                        start = time.time()
                        insert = gc_db.insert_many(data_list)
                        end = time.time()
                        await Client.delete_messages(message.chat.id, delete.id)
                        resp = f"""<b>
IMPORT DONE ✅

Total Number: {amt}
Data Type: JSON
Last Updated: a while ago
Time Taken: {end - start:0.4f}s
Requested Time: {message.date}
                        </b>"""
                        await message.reply_text(resp, message.id)
                        if insert:
                            name = "downloads/import.json"
                            my_file = Path(name)
                            my_file.unlink()
                    except:
                        await message.reply_text(
                            "<b>ERROR HAPPEND IMPORTING ❌</b>", message.id
                        )
                else:
                    await message.reply_text(
                        "<b>PLEASE SPECIFY A DATABASE NAME ❌</b>", message.id
                    )
            else:
                await message.reply_text(
                    "<b>PROVIDE A JSON FILE FOR IMPORTING ❌</b>", message.id
                )
    except Exception as e:
        await message.reply_text(e, message.id)
