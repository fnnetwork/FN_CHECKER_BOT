import json
import requests
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from FUNC.defs import *




def check_proxy(proxy_url):
    try:
        proxy_parts = proxy_url.split(":")
        if len(proxy_parts) != 4:
            raise ValueError("Proxy URL format is incorrect. Should be ip:port:user:password")

        proxy_ip = proxy_parts[0]
        proxy_port = proxy_parts[1]
        proxy_user = proxy_parts[2]
        proxy_password = proxy_parts[3]
        
        proxies = {
            "http": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
            "https": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
        }
        
        response = requests.get("http://www.google.com", proxies=proxies, timeout=5)
        response.raise_for_status()
        return response.status_code == 200
    except requests.exceptions.ProxyError as e:
        # print(f"ProxyError: {e}")
        return False
    except requests.exceptions.ConnectTimeout as e:
        # print(f"ConnectTimeout: {e}")
        return False
    except requests.exceptions.HTTPError as e:
        # print(f"HTTPError: {e}")
        return False
    except Exception as e:
        # print(f"Exception: {e}")
        return False
    




# @Client.on_message(filters.command("setproxy", [".", "/"]))
async def addproxy(client, message):
    try:
        user_id = str(message.from_user.id)
        get_user_info = await getuserinfo(user_id)
        proxy_url = message.text.split()[1]  # Assuming the proxy is the second word in the message

        if check_proxy(proxy_url):
            await updateuserinfo(user_id, "user_proxy", proxy_url)
            
            resp = f"""<b>
Proxy Successfully Added ✅
━━━━━━━━━━━━━━
{proxy_url}
Your proxy is live 🌐

Status: Successful
    </b>"""
        else:
            resp = "<b>Your proxy is dead ❌</b>"
        
        await message.reply_text(resp, message.id)
    except IndexError:
        await message.reply_text("<b>Invalid proxy format. Please provide a valid proxy.</b>", message.id)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Something went wrong ❌: {e}</b>", message.id)




# @Client.on_message(filters.command("rmproxy", [".", "/"]))
async def removeproxy(client, message):
    try:
        user_id = str(message.from_user.id)
        await updateuserinfo(user_id, "user_proxy", "N/A")
        resp = "<b>Proxy successfully removed ✅</b>"
        await message.reply_text(resp, message.id)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Something went wrong ❌: {e}</b>", message.id)




# @Client.on_message(filters.command("viewproxy", [".", "/"]))
async def viewproxy(client, message):
    try:
        user_id = str(message.from_user.id)
        user_info = await getuserinfo(user_id)
        proxy_url = user_info.get("user_proxy", "N/A")
        resp = f"<b>Your current proxy: {proxy_url}</b>"
        await message.reply_text(resp, message.id)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Something went wrong ❌: {e}</b>", message.id)










# /////////////////////////////////////////////////////user sk //////////////////////////////



@Client.on_message(filters.command("setamt", [".", "/"]))
async def add_brod(client, message):
    try:
        user_id = str(message.from_user.id)

        if len(message.command) > 1:
            amount = message.command[1].strip()
        elif message.reply_to_message and message.reply_to_message.text:
            amount = message.reply_to_message.text.strip()
        else:
            resp = "<b>Error: Please provide the amount either as a command argument or by replying to a message containing the amount.</b>"
            await message.reply_text(resp, reply_to_message_id=message.id)
            return

        await updateuserinfo(user_id, "damt", amount)

        resp = f"<b>{amount}$ charge amount added</b>"
        await message.reply_text(resp, reply_to_message_id=message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())






@Client.on_message(filters.command("rmsk", [".", "/"]))
async def removesk(client, message):
    user_id = str(message.from_user.id)  # Ensure user_id is defined before use
    user_info = await getuserinfo(user_id)
    sk_key = user_info.get("dsk", "N/A")

    if sk_key == "N/A":
        await message.reply_text("Please set a new sk using /setsk command..")
        return  # Exit early if no secret key is set

    try:
        await updateuserinfo(user_id, "dsk", "N/A")
        await updateuserinfo(user_id, "dpk", "N/A")
        await updateuserinfo(user_id, "dcr", "N/A")

        user_info = await getuserinfo(user_id)
        sk_key = user_info.get("dsk", "N/A")
        pk_key = user_info.get("dpk", "N/A")
        currency = user_info.get("dcr", "N/A")

        resp = f"""<b>
Sk Successfully Removed ✅
━━━━━━━━━━━━━━
Secret Key: {sk_key}

Publishable Key: {pk_key}

Currency: {currency}

Status: Successful
    </b>"""

        await message.reply_text(resp)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Something went wrong ❌: {e}</b>")








@Client.on_message(filters.command("mysk", [".", "/"]))
async def mysk(client, message):

    user_id = str(message.from_user.id)  # Ensure user_id is defined before use
    user_info = await getuserinfo(user_id)
    sk_key = user_info.get("dsk", "N/A")

    if sk_key == "N/A":
        await message.reply_text("Please set a new sk using /setsk command..")
        return  # Exit early if no secret key is set

    try:
        user_id = str(message.from_user.id)
        user_info = await getuserinfo(user_id)
        sk_key = user_info.get("dsk", "N/A")
        pk_key = user_info.get("dpk", "N/A")
        currency = user_info.get("dcr", "N/A")
        amount = user_info.get("damt", "N/A")
        resp = f"""<b>
Sk Successfully Added ✅
━━━━━━━━━━━━━━
Secret Key: {sk_key}

Publishable Key: {pk_key}

Currency: {currency}

{amount}$ CHARGE

Status: Successful
    </b>"""
        await message.reply_text(resp, message.id)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b>Something went wrong ❌: {e}</b>", message.id)













@Client.on_message(filters.command("selfcmd", [".", "/"]))
async def selfcmd(client, message):
    try:
        user_id = str(message.from_user.id)
        resp = f"""<b>

<span style="color: #3498db; font-size: 16px;">MASTER Self Command Zone:</span>

<span style="color: #e74c3c;">SETUP PROXY..UNACTIVE THIS CMD-❌</span>

<span style="color: #2ecc71;">You can use your own proxy using this... also if you can remove your proxy.</span>
1. <span style="color: #f1c40f;">/setproxy ip:port:user:pass</span>
2. <span style="color: #f1c40f;">/rmproxy</span>
3. <span style="color: #f1c40f;">/viewproxy see your proxy</span>

<span style="color: #e74c3c;">SETUP SK_LIVE..👍 ONLY FOR SVV GATE 👍[OTHER CVV OR CCN COMING SOON]</span>

<span style="color: #2ecc71;">If you have live sk_key then you can use your own private sk and check cc</span>
1. <span style="color: #f1c40f;">/setsk sk_key [ automatic generate pk or other necessary info. ]</span>
2. <span style="color: #f1c40f;">/mysk checking your sk_key</span>
3. <span style="color: #f1c40f;">/rmsk if you want to use my sk then remove your sk first else not worked..</span>
4. <span style="color: #f1c40f;">/setamt some sk need high amount like 3-10 dollar so you want to update your amount just use /setamt 5 [ any amount ]</span>
 
    </b>"""
        await message.reply_text(resp, reply_to_message_id=message.id)
    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"<b><span style='color: #e74c3c;'>Something went wrong ❌: {e}</span></b>", reply_to_message_id=message.id)

async def error_log(error_message):
    pass
