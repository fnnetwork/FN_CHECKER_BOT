import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = result
            hits = "NO"

    # KEY "Thank you for your purchase!" 
    # KEY "Order #" 
    # KEY "Your order is confirmed" 
    # KEY "CARD_SUCCEEDED" 
    # KEY "CARD_APPROVED" 
    # KEY "PaymentSucceeded" 
    # KEY "PaymentApproved" 
    # KEY "PaymentCompleted" 
    # KEY "CARD_COMPLETED" 
    # KEY "CARD_SUCCESS" 
    # KEY "SucceededReceipt" 
    # KEY "ApprovedReceipt" 
    # KEY "CompletedReceipt" 
    # KEY "succeeded" 
    # KEY "CARD_COMPLETED" 
    # KEY "CARD_SUCCEEDED" 
    # KEY "\"redirectUrl\":\"" 
    # KEY "Your order is confirmed" 
    # KEY "Thank you" 
    # KEY "Thank you for your purchase!" 



            if (
                "SUCCESS" in result or
                "Order #" in result or
                "CARD_SUCCEEDED" in result or
                "\"redirectUrl\":\"" in result or
                "CompletedReceipt" in result or
                "CARD_COMPLETED" in result or
                "ApprovedReceipt" in result or
                "SucceededReceipt" in result or
                "CARD_APPROVED" in result or
                "PaymentSucceeded" in result or
                "PaymentCompleted" in result or
                "PaymentApproved" in result or
                "Thank you for your purchase!" in result or
                "ThankYou" in result or
                "Thanks for you order" in result or
                "Thank you" in result or
                "thank_you" in result or
                "success" in result or
                "Your order is confirmed" in result or
                "your order is confirmed" in result or
                "classicThankYouPageUrl" in result
            ):
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                response = "order is confirmed 🔥"
                hits = "YES"

                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif "insufficient_funds" in result or "card has insufficient funds." in result or "2001 Insufficient Funds" in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ❎"
                response = "Insufficient Funds"
                hits = "YES"
                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif (
                    "INCORRECT_CVC" in result
                    or "INVALID_CVC" in result
                    or "2010 Card Issuer Declined CVV" in result
                    or "Your card's security code is incorrect." in result
                    or "Security code was not matched by the processor" in result


            ):
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ❎"
                response = "Security code was not matched by the processor"
                hits = "YES"
                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif "transaction_not_allowed" in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ❎"
                response = "Card Doesn't Support Purchase"
                hits = "YES"
                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif '"cvc_check": "pass"' in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ❎"
                response = "CVV LIVE"
                hits = "YES"
                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif (
                "three_d_secure_redirect" in result
                or "card_error_authentication_required" in result
                or "OTP Required" in result
                or "stripe_3ds2_fingerprint" in result
                or "stripe/authentications" in result
                or "3d_secure_2" in result
                or "CompletePaymentChallenge" in result
                or "AUTHENTICATION_ERROR" in result
                or "ActionRequiredReceipt" in result
                or "stripe_3ds2_fingerprint" in result
            ):
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ❎"
                response = "OTP Required"
                hits = "YES"
                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif "Your card does not support this type of purchase." in result:
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ❎"
                response = "Card Doesn't Support Purchase"
                hits = "YES"
                await forward_resp(fullcc, "SHOPIFY CHARGE [SG]", response)

            elif "ProxyError" in result:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Proxy Connection Refused"
                hits = "NO"
                await refundcredit(user_id)


            elif ("Card was declined" in result
                    or "Your card was declined." in result
                    or "CARD_DECLINED" in result
                    or "PAYMENTS_CREDIT_CARD_GENERIC" in result
                    or "Card number is incorrect" in result
                    or "The shipping options have changed for your order. Review your selection and try again" in result

                ):
                response = " Card was declined"

            elif "Your payment details couldn’t be verified. Check your card details and try again." in result:
                response = "Your payment details couldn’t be verified"

            elif "PAYMENTS_CREDIT_CARD_BASE_EXPIRED" in result:
                response = "CARD EXPIRE"

            else:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = await find_between(result, "System was not able to complete the payment. ", ".")
                if response is None:
                    response = "Card Declined"
                    await result_logs(fullcc, "Stripe Charge SG", result)
                response = "Card was declined"
                hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json

    except Exception as e:
        status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
        response = str(e) + " ❌"
        hits = "NO"

        json = {
            "status": status,
            "response": response,
            "hits": hits,
            "fullz": fullcc,
        }
        return json
