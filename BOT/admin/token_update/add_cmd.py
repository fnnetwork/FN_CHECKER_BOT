import json
from pyrogram import Client, filters
from FUNC.usersdb_func import *



@Client.on_message(filters.command("damt", [".", "/"]))
async def update_dead_amount(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perform This Action, You Need Admin Level Power. 

Contact @FNxELECTRA For More Info ✅</b>"""
            await message.reply_text(resp)
            return
        try:
            new_dead_amount = str(message.text.split(" ")[1])
        except:
            new_dead_amount = str(message.reply_to_message.text)


        with open("FILES/deadsk.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        data["DEAD_AMOUNT"] = new_dead_amount

        with open("FILES/deadsk.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4)

        resp = f"""<b>
DEAD_AMOUNT Updated Successfully ✅
━━━━━━━━━━━━━━
NEW DEAD_AMOUNT: {new_dead_amount}
    </b>"""
        await message.reply_text(resp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())















@Client.on_message(filters.command("setso", [".", "/"]))
async def update_shopify_url(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>Privilege Not Found ⚠️

Message: Do Perform This Action, You Need Admin Level Power. 

Contact @FNxELECTRA For More Info ✅</b>"""
            await message.reply_text(resp)
            return

        new_url_so = str(message.reply_to_message.text)

        with open("FILES/deadsk.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        data["AUTO_SHOPIFY_SO"] = new_url_so

        with open("FILES/deadsk.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4)

        resp = f"""<b>
Auto Shopify Url Updated ✅
━━━━━━━━━━━━━━
NEW SITE: {new_url_so}
    </b>"""
        await message.reply_text(resp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())





















