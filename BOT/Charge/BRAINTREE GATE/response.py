import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status = "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌"
            response = result
            hits = "NO"

        if (
            "SUCCESS" in result or
            '"status":"SUCCESS"' in result or
            "thank_you" in result or
            "Your order is confirmed" in result or
            "Your_order_is_confirmed" in result or
            "classicThankYouPageUrl" in result
        ):
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅"
            response = "Thanks for your donation 🔥"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif "insufficient_funds" in result or "card has insufficient funds." in result:
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅"
            response = "Insufficient Funds ❎"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif (
            "INCORRECT_CVC" in result or
            "invalid_cvc ❌" in result or
            "INCORRECT_CVC" in result or
            "Your card's security code is incorrect." in result or
            "Security code was not matched by the processor" in result
        ):
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ❎"
            response = "CCN LIVE ❎"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif "transaction_not_allowed" in result:
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ❎"
            response = "Card Doesn't Support Purchase ❎"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif '"cvc_check": "pass"' in result:
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅"
            response = "CVV LIVE ❎"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif (
            "CompletePaymentChallenge" in result
            or "card_error_authentication_required" in result
            or "OTP Required" in result
            or "CompletePaymentChallenge" in result
            or "AUTHENTICATION_ERROR" in result
            or "ActionRequiredReceipt" in result
            or "stripe_3ds2_fingerprint" in result
            or "stripe/authentications" in result
            or "3d_secure_2" in result
        ):
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ❎"
            response = "3D Challenge Required ❎"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif "Your card does not support this type of purchase." in result:
            status = "𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ❎"
            response = "Card Doesn't Support Purchase ❎"
            hits = "YES"
            await forward_resp(fullcc, "Donate br", response)

        elif ("Your payment details couldn’t be verified. Check your card details and try again" in result or
              "The shipping options have changed for your order. Review your selection and try again." in result or
              "CARD_DECLINED" in result or
              "Your card was declined." in result or
              "Card was declined" in result or
              "There was an issue processing your payment. Try again or use a different payment method." in result or
              '"status":"FAILED"' in result):
            status = "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌"
            response = "Card Was Declined"
            hits = "NO"

        elif "ProxyError" in result:
            status = "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌"
            response = "Proxy Connection Refused ❌"
            hits = "NO"
            await refundcredit(user_id)
        else:
            status = "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌"
            response = result + " ❌"
            hits = "NO"
            try:
                with open("result_shopify.txt", "a") as f:
                    f.write(fullcc + " - " + "SHOPIFY 11.50$" +
                            " - " + result + "\n")
            except:
                pass

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json

    except Exception as e:
        status = "𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌"
        response = str(e) + " ❌"
        hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json
