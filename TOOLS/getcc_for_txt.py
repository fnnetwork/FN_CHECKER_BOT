import  os
from FUNC.defs import *


async def getcc_for_txt(file_name, role):
    try:
        file = open(f"downloads/{file_name}").read().splitlines()
        os.remove(f"downloads/{file_name}")
        ccs = []
        for i in file:
            get = await getcards(i)
            if get != None:
                cc     = get[0]
                mes    = get[1]
                ano    = get[2]
                cvv    = get[3]
                fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                ccs.append(fullcc)

        if role == "FREE" and len(ccs) > 1501:
            resp = f"""<b>
Limit Reached ⚠️

Message: Your Can Check 1500 CC at a Time . Buy Plan to Increase Your Limit .

Type /buy For Paid Plan
</b>"""
            return False, resp
        if (role == "PREMIUM" or role == "LIFETIME") and len(ccs) > 3001:            
            resp = f"""<b>
Limit Reached ⚠️

Message: Your Can Check 3001 CC at a Time . Buy Plan to Increase Your Limit .

Type /buy For Paid Plan
</b>"""
            return False, resp
        if len(ccs) == 0:
            resp = f"""<b>
CC Not Found ⚠️

Message: We Are Unable to Find Any CC Details From Your Input . Provide CC's Details To Check .
</b>"""
            return False, resp
        else:
            return True, ccs

    except:
        return False , "Try Again Later"
