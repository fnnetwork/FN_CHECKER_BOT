import traceback
from FUNC.defs import *
from FUNC.usersdb_func import *


async def get_charge_resp(result, user_id, fullcc):
    try:

        if type(result) == str:
            status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
            response = result
            hits = "NO"

            if (
                "Nice! New payment method added" in result
            ):
                status = "𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅"
                # response = "Approved ✅"
                response = "1000: Approved"
                hits = "YES"
                await forward_resp(fullcc, "BRAINTREE AUTH", response)

            elif ("Status code cvv: Gateway Rejected: cvv" in result):
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Gateway Rejected: cvv"
                hits = "NO"

            elif ("Declined - Call Issuer" in result):
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Declined - Call Issuer"
                hits = "NO"

            elif ("Cannot Authorize at this time" in result):
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Cannot Authorize at this time"
                hits = "NO"

            elif ("Processor Declined - Fraud Suspected" in result):
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Fraud Suspected"
                hits = "NO"

            elif "Status code risk_threshold: Gateway Rejected: risk_threshold" in result:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Gateway Rejected: risk_threshold"
                hits = "NO"

            elif ("We're sorry, but the payment validation failed. Declined - Call Issuer" in result or
                  "Payment failed: Declined - Call Issuer" in result
                  ):
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Declined - Call Issuer"
                hits = "NO"

            elif "ProxyError" in result:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                response = "Proxy Connection Refused"
                hits = "NO"
                await refundcredit(user_id)

            else:
                status = "𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌"
                try:
                    response = result.split('"message": "')[
                        1].split('"')[0] + " ❌"
                except:
                    response = result
                    await result_logs(fullcc, "Braintree Auth", result)
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
