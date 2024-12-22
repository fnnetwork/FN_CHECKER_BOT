from FUNC.defs import *
import re


async def getcc_for_mass(message, role):
    try:
        ccs = []

        if message.reply_to_message:
            text = message.reply_to_message.text
        else:
            text = message.text

        for i in text.split("\n"):
            get = await getcards(i)
            if get is not None:
                cc = get[0]
                mes = get[1]
                ano = get[2]
                cvv = get[3]
                fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                ccs.append(fullcc)

        if role == "FREE" and len(ccs) > 16:
            resp = f"""<b>
Limit Reached ⚠️

Message: You Can Check 15 CC at a Time. Buy Plan to Increase Your Limit.

Type /buy For Paid Plan
</b>"""
            return False, resp
        if (role == "PREMIUM" or role == "LIFETIME") and len(ccs) > 25:            
            resp = f"""<b>
Limit Reached ⚠️

Message: You Can Check 25 CC at a Time. If You Increase limit Then Buy Customize Plan  to Knock @amitonmoyx.

Type /buy For Paid Plan
</b>"""
            return False, resp
        if len(ccs) == 0:
            resp = f"""<b>
CC Not Found ⚠️

Message: We Are Unable to Find Any CC Details From Your Input. Provide CC's Details To Check.
</b>"""
            return False, resp
        else:
            return True, ccs

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        return False, "Try Again Later"



