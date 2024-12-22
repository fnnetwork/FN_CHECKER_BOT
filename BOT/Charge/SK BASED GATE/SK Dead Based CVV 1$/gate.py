import random
import uuid
from fake_useragent import UserAgent
from FUNC.defs import *
from FUNC.usersdb_func import *
import json



async def create_deadsk_charge(fullcc, sks, session,user_id):
    user_info = await getuserinfo(user_id)

    if not user_info:
        raise ValueError(f"No user found with user_id: {user_id}")
    checksk = user_info.get("dsk", "N/A")
    if checksk == "N/A":
        with open("FILES/deadsk.json", "r", encoding="utf-8") as f:
            gates_data = json.load(f)
        sk_key = gates_data.get("DEAD_SK_KEY")
        pk_key = gates_data.get("DEAD_PK_KEY")
        dcr = gates_data.get("DEAD_CURRENCY")
        damt = gates_data.get("DEAD_AMOUNT")
    else:
        sk_key = user_info.get("dsk", "N/A")
        pk_key = user_info.get("dpk", "N/A")
        dcr = user_info.get("dcr", "N/A")
        amount = user_info.get("damt", "N/A")
        try:
            damt = int(amount) * 100
        except ValueError:
            return "Set Charge Amount /setamt amount"


    try:
        cc, mes, ano, cvv = fullcc.split("|")
        max_amt = 0
        max_retry = 200
        sk = random.choice(sks)
        data = await get_random_info(session)
        fname = data["fname"]
        lname = data["lname"]
        email = data["email"]
        phone = data["phone"]
        add1 = data["add1"]
        city = data["city"]
        state_short = data["state_short"]
        zip = data["zip"]
        user_agent = UserAgent().random

        url = "https://api.stripe.com/v1/payment_methods"
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded',
            "Authorization":  f"Bearer {pk_key}",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent':  user_agent,
        }
        data = {
            "type": "card",
            "billing_details[name]": fname + " " + lname,
            "billing_details[address][city]": city,
            "billing_details[address][country]": "US",
            "billing_details[address][line1]": add1,
            "billing_details[address][postal_code]": zip,
            "billing_details[address][state]": state_short,
            "card[number]": cc,
            "card[cvc]": cvv,
            "card[exp_month]": mes,
            "card[exp_year]": ano,
            "guid": str(uuid.uuid4()),
            "muid": str(uuid.uuid4()),
            "sid": str(uuid.uuid4()),
            "payment_user_agent": "stripe.js/fb7ba4c633; stripe-js-v3/fb7ba4c633; split-card-element",
            "time_on_page": random.randint(10021, 10090),
        }
        while True:
            result = await session.post(url=url, headers=headers, data=data)
            if max_amt == max_retry:
                return "429 Too Many Requests"
            if "Invalid API Key provided" in result.text or "testmode_charges_only" in result.text or "api_key_expired" in result.text or "Your account cannot currently make live charges." in result.text:
                await delsk(sk)
                return 'api_key_expired'
            if "Request rate limit exceeded." in result.text:
                max_amt += 1
                continue
            else:
                break
        try:
            id = result.json()["id"]
        except:
            return result

        url = "https://api.stripe.com/v1/payment_intents"
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US',
            'content-type': 'application/x-www-form-urlencoded',
            "Authorization":  f"Bearer {sk_key}",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent':  user_agent,
        }
        data = {
            # "amount": random.randint(60, 70),
            "amount": damt,
            "currency": dcr,
            "payment_method_types[]": "card",
            "payment_method":  id,
            "confirm": "true",
            "off_session": "true",
            "use_stripe_sdk": "true",
            "description": "None",
            "receipt_email":  email,
            "metadata[order_id]":  str(random.randint(100000000000000000, 999999999999999999)),
        }
        while True:
            result = await session.post(url=url, headers=headers, data=data)
            # print(result.text)
            if max_amt == max_retry:
                return "429 Too Many Requests"
            if "Invalid API Key provided" in result.text or "testmode_charges_only" in result.text or "api_key_expired" in result.text or "Your account cannot currently make live charges." in result.text:
                await delsk(sk)
                # await refundcredit(user_id)

                return 'api_key_expired'

            if "Request rate limit exceeded." in result.text:
                max_amt += 1
                continue
            else:
                break
        return result

    except Exception as e:
        return str(e)
