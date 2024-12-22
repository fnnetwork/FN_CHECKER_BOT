import os
import json
import traceback
from pyrogram import Client, filters
from FUNC.usersdb_func import *


def extract_user_details(user_list):
    return [
        {
            "User ID": user.get("id", "Unknown"),
            "Username": user.get("username", "Unknown"),
            "Status": user.get("status", "Unknown"),
            "Plan": user.get("plan", "Unknown"),
            "Expiry": user.get("expiry", "Unknown"),
            "Credit": user.get("credit", "Unknown"),
            "Antispam Time": user.get("antispam_time", "Unknown"),
            "Total Keys": user.get("totalkey", "Unknown"),
            "Registration Date": user.get("reg_at", "Unknown")
        }
        for user in user_list
    ]


@Client.on_message(filters.command("showuser", [".", "/"]))
async def showuser(Client, message):
    try:
        user_id = str(message.from_user.id)
        OWNER_ID = json.loads(
            open("FILES/config.json", "r", encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """𝐏𝐫𝐢𝐯𝐢𝐥𝐞𝐠𝐞 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 ⚠️

𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐃𝐨 𝐏𝐞𝐫𝐟𝐨𝐫𝐦 𝐓𝐡𝐢𝐬 𝐀𝐜𝐭𝐢𝐨𝐧, 𝐘𝐨𝐮 𝐍𝐞𝐞𝐝 𝐀𝐝𝐦𝐢𝐧 𝐋𝐞𝐯𝐞𝐥 𝐏𝐨𝐰𝐞𝐫. 

𝐂𝐨𝐧𝐭𝐚𝐜𝐭 @FNxELECTRA 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨 ✅"""
            await message.reply_text(resp)
            return

        all_users = list(await getallusers())
        CHATS_AUTH = list(await getallchat())

        owner_users = [
            user for user in all_users if user.get("status") == "OWNER"]
        lifetime_users = [
            user for user in all_users if user.get("status") == "LIFETIME"]
        premium_users = [
            user for user in all_users if user.get("status") == "PREMIUM"]

        data = {
            "Owner Users": len(owner_users),
            "Owner Users Details": extract_user_details(owner_users),
            "Lifetime Users": len(lifetime_users),
            "Lifetime Users Details": extract_user_details(lifetime_users),
            "Premium Users": len(premium_users),
            "Premium Users Details": extract_user_details(premium_users),
            "Authorized Chats": len(CHATS_AUTH),
            "Chat IDs": CHATS_AUTH,
            "Checked On": str(message.date)
        }

        file_path = "user.json"

        try:
            with open(file_path, "w") as output_file:
                json.dump(data, output_file, indent=4)

            await message.reply_document(document=file_path)

            os.remove(file_path)

        except Exception as e:
            print(f"Error while saving JSON file: {e}")
            await error_log(traceback.format_exc())

    except Exception as e:
        await error_log(traceback.format_exc())

if __name__ == "__main__":
    app = Client("my_bot")
    app.run()
