import httpx
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *

IPINFO_API_KEY = "9c3a2f3c00225d"  # Replace with your ipinfo.io API key

@Client.on_message(filters.command("ip", [".", "/"]))
async def cmd_bin(Client, message):
    try:
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]

        try:
            if message.reply_to_message:
                ip_address = str(message.reply_to_message.text)
            else:
                ip_address = str(message.text.split(" ")[1])
        except:
            resp = """<b>
Invalid IP Address ⚠️

Message: Not Found Valid IP Address From Your Input.
            </b>"""
            await message.reply_text(resp)
            return

        try:
            async with httpx.AsyncClient() as session:
                # Fetch IP information using freeipapi.com
                url = f"https://freeipapi.com/api/json/{ip_address}"
                response = await session.get(url)
                data = response.json()

                # Fetch scam score using ipinfo.io
                ipinfo_response = await session.get(f"https://ipinfo.io/{ip_address}/json?token={IPINFO_API_KEY}")
                ipinfo_data = ipinfo_response.json()

        except httpx.HTTPError as http_err:
            await error_log(f"HTTP Error: {http_err}")
            resp = """<b>
Error fetching IP info ⚠️

Message: Unable to fetch IP info. Check if the IP is valid.
            </b>"""
            await message.reply_text(resp)
            return
        except Exception as e:
            await error_log(f"Error: {e}")
            resp = """<b>
Error fetching IP info ⚠️

Message: Unable to fetch IP info. Check if the IP is valid.
            </b>"""
            await message.reply_text(resp)
            return

        IpVersion = data.get('ipVersion')
        IpAddress = data.get('ipAddress')
        Country = data.get('countryName')
        timezone = ipinfo_data.get('timezone')
        CountryCode = data.get('countryCode')
        ZipCode = data.get('zipCode')
        CityName = data.get('cityName')
        RegionName = data.get('regionName')
        ProxyCheck = data.get('isProxy')
        Continent = data.get('continent')

        resp = f"""<b>IP Address Fetched Successfully ✅</b>
━━━━━━━━━━━━━━
🌐 <b>IP:</b> <code>{IpAddress}</code>
🆔 <b>IP Version:</b> <code>{IpVersion}</code>
🌍 <b>Country:</b> <code>{Country}</code> -> <code>{CountryCode}</code>
🕰️ <b>Time Zone:</b> <code>{timezone}</code>
📮 <b>Zip Code:</b> <code>{ZipCode}</code>
🏙️ <b>City Name:</b> <code>{CityName}</code>
🌍 <b>Region Name:</b> <code>{RegionName}</code>
🛡️ <b>Proxy Check:</b> <code>{ProxyCheck}</code>
🌏 <b>Continent:</b> <code>{Continent}</code>
━━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [ {role} ]
<b>Bot by:</b> <a href="tg://user?id=6745804180">Toͥnmͣoͫy</a>
"""
        await message.reply_text(resp)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
