import httpx
from pyrogram import Client, filters
from bs4 import BeautifulSoup
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *


@Client.on_message(filters.command("fake", [".", "/"]))
async def cmd_fake(Client, message):
    try:
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]

        try:
            if len(message.text.split(" ")) > 1:
                country_code = message.text.split(" ")[1].lower()
            else:
                country_code = 'us'  # Default to United States if no country code is provided

            async with httpx.AsyncClient() as client:
                response = await client.get(f'https://www.fakexy.com/fake-address-generator-{country_code}')
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extracting fake address details
                fake_name = soup.find('td', text='Full Name').find_next_sibling(
                    'td').get_text(strip=True).title()
                fake_address = soup.find('td', text='Street').find_next_sibling(
                    'td').get_text(strip=True).title()
                fake_city = soup.find(
                    'td', text='City/Town').find_next_sibling('td').get_text(strip=True).title()
                fake_state = soup.find(
                    'td', text='State/Province/Region').find_next_sibling('td').get_text(strip=True).title()
                fake_country = soup.find('td', text='Country').find_next_sibling(
                    'td').get_text(strip=True).title()
                fake_zipcode = soup.find(
                    'td', text='Zip/Postal Code').find_next_sibling('td').get_text(strip=True).title()
                fake_gender = soup.find('td', text='Gender').find_next_sibling(
                    'td').get_text(strip=True).title()
                fake_phone = soup.find('td', text='Phone Number').find_next_sibling(
                    'td').get_text(strip=True).title()

                resp = f"""
<b>Fake Info Created Successfully ✅</b>
━━━━━━━━━━━━━━
🆔 <b>Full Name:</b> <code>{fake_name}</code>
👤 <b>Gender:</b> <code>{fake_gender}</code>
🏠 <b>Street:</b> <code>{fake_address}</code>
🏙️ <b>City/Town/Village:</b> <code>{fake_city}</code>
🌍 <b>State/Province/Region:</b> <code>{fake_state}</code>
📮 <b>Postal Code:</b> <code>{fake_zipcode}</code>
📞 <b>Phone Number:</b> <code>{fake_phone}</code>
🌏 <b>Country:</b> <code>{fake_country}</code>
━━━━━━━━━━━━━━
<b>Checked By:</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [ {role} ]
<b>Bot by:</b> <a href="tg://user?id=7593550190">𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
"""
                await message.reply_text(resp)  # Reply to the original message

        except Exception as e:
            import traceback
            await error_log(traceback.format_exc())

    except Exception as outer_exception:
        import traceback
        await error_log(traceback.format_exc())
