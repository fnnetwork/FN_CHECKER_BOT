from .func import *
from pyrogram import Client, filters
from FUNC.usersdb_func import *


@Client.on_message(filters.command("redeem", [".", "/"]))
async def cmd_gc(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = await getuserinfo(user_id)
        regdata = str(regdata)

        if regdata == "None":
            resp = f"""<b>
Unregistered Users ⚠️

Message: You Can't Use Me Unless You Register First .

Type /register to Continue
</b>"""
            await message.reply_text(resp, message.id)
            return

        try:
            gc  = message.text.split(" ")[1]
        except:
            resp = "<b>Please Provide A Valid Giftcode ❌</b>"
            await message.reply_text(resp, message.id)
            return

        detail = await getgc(gc)
        if str(detail) == "None":
            resp = "<b>Please Provide A Valid Giftcode ❌</b>"
            await message.reply_text(resp, message.id)
            return
        

        get_user_info = usersdb.find_one({"id": user_id})
        if "∞" in get_user_info["plan"]:
            resp = "<b>You have already active plan, you cannot redeem!</b>"
            await message.reply_text(resp, message.id)
            return


        status = str(detail["status"])
        type   = str(detail["type"])
        if status == "ACTIVE" and type == "PREMIUM":
            await onlycredits(user_id)
            await updategc(gc)
            resp = f"""<b>
Redeemed Successfully ✅
━━━━━━━━━━━━━━
● Giftcode: {gc}
● User ID: {user_id}

Message: Congratz ! Your Provided Giftcode Successfully Redeemed to Your Acoount And You Got "100 Credits + Premium Subscription " .
</b>"""
            await message.reply_text(resp, message.id)

        elif status == "ACTIVE" and type == "PLAN1":
            await plan1gc(user_id)
            await updategc(gc)
            resp = f"""<b>
Redeemed Successfully ✅
━━━━━━━━━━━━━━
● Giftcode: {gc}
● User ID: {user_id}

Message: Congratz ! Your Provided Giftcode Successfully Redeemed to Your Acoount And You Got "Starter Plan For 7 Days " .
</b>"""
            await message.reply_text(resp, message.id)

        elif status == "ACTIVE" and type == "PLAN2":
            await plan2gc(user_id)
            await updategc(gc)
            resp = f"""<b>
Redeemed Successfully ✅
━━━━━━━━━━━━━━
● Giftcode: {gc}
● User ID: {user_id}

Message: Congratz ! Your Provided Giftcode Successfully Redeemed to Your Acoount And You Got "Silver Plan For 15 Days " .
</b>"""
            await message.reply_text(resp, message.id)

        elif status == "ACTIVE" and type == "PLAN3":
            await plan3gc(user_id)
            await updategc(gc)
            resp = f"""<b>
Redeemed Successfully ✅
━━━━━━━━━━━━━━
● Giftcode: {gc}
● User ID: {user_id}

Message: Congratz ! Your Provided Giftcode Successfully Redeemed to Your Acoount And You Got "Gold Plan For 30 Days " .
</b>"""
            await message.reply_text(resp, message.id)

        elif status == "USED":
            resp = f"""<b>
Already Redeemed ⚠️

Giftcode: {gc}

Message: This Giftcode is Already Redeemed by another users .
</b> """
            await message.reply_text(resp, message.id)

        else:
            resp = f"""<b>
Invalid Giftcode ❌

Giftcode: {gc}

Message: We can't find any giftcode like that . your provided giftcode is invalid .   
        </b>"""
            await message.reply_text(resp, message.id)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())
