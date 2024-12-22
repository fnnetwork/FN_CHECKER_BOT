import csv
import pycountry
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *

async def singlebinget(message):
    try:
        parts = message.text.split()
        if len(parts) >= 2:
            return parts[1], None, None, None
        else:
            return False
    except:
        return False

def get_bin_info_from_csv(fbin, csv_file='FILES/bins_all.csv'):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == fbin:
                    return {
                        "bin": row[0],
                        "country": row[1],
                        "flag": row[2],
                        "brand": row[3],
                        "type": row[4],
                        "level": row[5],
                        "bank": row[6]
                    }
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return {}

def get_country_name(code, fallback_country_name):
    try:
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else fallback_country_name
    except Exception as e:
        print(f"Error getting country name: {e}")
        return fallback_country_name

@Client.on_message(filters.command("bin", [".", "/"]))
async def cmd_bin(client, message):
    try:
        checkall = await check_all_thing(client, message)
        if checkall[0] == False:
            return

        bin = await singlebinget(message)
        if bin == False:
            bin = await getmessage(message)
            if bin == False:
                resp = """
𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ⚠️

𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐍𝐨 𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 𝐰𝐚𝐬 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐢𝐧𝐩𝐮𝐭.
"""
                await message.reply_text(resp, quote=True)
                return

        fbin = bin[0][:6]
        bin_info = get_bin_info_from_csv(fbin)

        if not bin_info:
            resp = """
𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ⚠️

𝐌𝐞𝐬𝐬𝐚𝐠𝐞: 𝐍𝐨 𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞.
"""
            await message.reply_text(resp, quote=True)
            return

        brand = bin_info.get("brand", "N/A").upper()
        card_type = bin_info.get("type", "N/A").upper()
        level = bin_info.get("level", "N/A").upper()
        bank = bin_info.get("bank", "N/A").upper()
        country_code = bin_info.get("country", "N/A").upper()
        flag = bin_info.get("flag", "N/A").upper()
        country_full_name = get_country_name(country_code, country_code)

        resp = f"""
𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽 𝗥𝗲𝘀𝘂𝗹𝘁 🔍

𝗕𝗜𝗡: <code>{fbin}</code>
𝗜𝗻𝗳𝗼: <code>{brand} - {card_type} - {level}</code>
𝐁𝐚𝐧𝐤: <code>{bank} 🏛</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country_full_name} {flag}</code>
"""
        await message.reply_text(resp, quote=True)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())
