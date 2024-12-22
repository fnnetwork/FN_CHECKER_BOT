from FUNC.defs import *
from datetime import date
from datetime import timedelta
from mongodb import *














async def getuserinfo(user_id):
    return usersdb.find_one({"id": user_id}, {"_id": 0})


async def randgen(len=6):
    import random
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(len))


async def getallusers():
    return usersdb.find({}, {"_id": 0})


async def updateuserinfo(user_id, module, value):
    usersdb.update_one({"id": user_id}, {"$set": {module: value}})


async def premiumuser(user_id):
    usersdb.update_one({"id": user_id}, {"$set": {"status": "PREMIUM"}})


async def freeuser(user_id):
    usersdb.update_one({"id": user_id}, {"$set": {"status": "FREE"}})


async def directcredit(user_id, amt):
    usersdb.update_one({"id": user_id}, {"$set": {"credit": amt}})


async def addchat(chat_id):
    chats_auth.insert_one({"id": chat_id, "status": "approved"})

async def delchat(chat_id):
    chats_auth.delete_one({"id": chat_id})


async def addsupergroup(chat_id):
    chats_auth.insert_one({"id": chat_id, "status": "sp-approved"})


async def getchatinfo(chat_id):
    return chats_auth.find_one({"id": chat_id}, {"_id": 0})


async def getallchat():
    return chats_auth.find({}, {"_id": 0})


async def setantispamtime(user_id):
    import time
    usersdb.update_one({"id": user_id}, {"$set": {"antispam_time": int(time.time())}})


async def deductcredit(user_id):
    user_id = str(user_id)
    get_user_info = usersdb.find_one({"id": user_id}, {"_id": 0})
    if "∞" in get_user_info["plan"]:
        return
    setcredit = int(get_user_info["credit"]) - 1
    usersdb.update_one({"id": user_id}, {"$set": {"credit": setcredit}})
    

# async def deductcredit(user_id, chat_id):
#     user_id = str(user_id)
#     get_user_info = usersdb.find_one({"id": user_id}, {"_id": 0})
#     if "∞" in get_user_info["plan"]:
#         return
#     chat_info = chats_auth.find_one({"id": chat_id}, {"_id": 0})
#     if get_user_info in chat_info.get("status") == "sp-approved":
#         return
#     setcredit = int(get_user_info["credit"]) - 1
#     usersdb.update_one({"id": user_id}, {"$set": {"credit": setcredit}})












async def massdeductcredit(user_id, amt):
    user_id = str(user_id)
    get_user_info = usersdb.find_one({"id": user_id}, {"_id": 0})
    if "∞" in get_user_info["plan"]:
        return
    setcredit = int(get_user_info["credit"]) - amt
    usersdb.update_one({"id": user_id}, {"$set": {"credit": setcredit}})


async def refundcredit(user_id):
    get_user_info = usersdb.find_one({"id": user_id}, {"_id": 0})
    if "∞" in get_user_info["plan"]:
        return
    setcredit = int(get_user_info["credit"]) + 1
    usersdb.update_one({"id": user_id}, {"$set": {"credit": setcredit}})


async def check_negetive_credits(user_id):
    get_user_info = await getuserinfo(user_id)
    credits       = int(get_user_info["credit"])
    if credits < 0:
        credits += abs(credits) + 500
    else:
        credits = credits + 500
    await directcredit(user_id, credits)






async def csplan(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id}, {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id}, {"$set": {"plan": "Custom Plan ∞"}})
    getvalidity  = str(date.today() + timedelta(days=7)).split("-")
    yy , mm , dd = getvalidity[0], getvalidity[1], getvalidity[2]
    validity     = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id}, {"$set": {"expiry": validity}})






async def getplan1(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id}, {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id}, {"$set": {"plan": "Starter Plan 7$ ∞"}})
    getvalidity  = str(date.today() + timedelta(days=7)).split("-")
    yy , mm , dd = getvalidity[0], getvalidity[1], getvalidity[2]
    validity     = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id}, {"$set": {"expiry": validity}})


async def getplan2(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id}, {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id}, {"$set": {"plan": "Silver Plan 15$ ∞"}})
    getvalidity  = str(date.today() + timedelta(days=15)).split("-")
    yy , mm , dd = getvalidity[0], getvalidity[1], getvalidity[2]
    validity     = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id}, {"$set": {"expiry": validity}})


async def getplan3(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id}, {"$set": {"status": "PREMIUM"}})

    usersdb.update_one({"id": user_id}, {"$set": {"plan": "Gold Plan 25$ ∞"}})
    getvalidity  = str(date.today() + timedelta(days=30)).split("-")
    yy , mm , dd = getvalidity[0], getvalidity[1], getvalidity[2]
    validity     = f"{dd}-{mm}-{yy}"
    usersdb.update_one({"id": user_id}, {"$set": {"expiry": validity}})


async def get_lifetime_plan(user_id):
    await check_negetive_credits(user_id)
    get_user_info = await getuserinfo(user_id)
    if get_user_info["status"] == "FREE":
        usersdb.update_one({"id": user_id}, {"$set": {"status": "LIFETIME"}})

    usersdb.update_one({"id": user_id}, {
                       "$set": {"plan": "Lifetime 35$ ∞"}})
    























async def plan_expirychk(user_id):
    try:
        import urllib.parse, json, httpx

        today      = str(date.today())
        getuser    = usersdb.find_one({"id": user_id}, {"_id": 0})
        getexpiry  = getuser["expiry"].split("-")
        dd, mm, yy = getexpiry[0], getexpiry[1], getexpiry[2]
        expiry     = f"{yy}-{mm}-{dd}"
        if expiry != "N/A" and expiry < today:
            usersdb.update_one({"id": user_id}, {"$set": {"plan": "N/A"}})
            usersdb.update_one({"id": user_id}, {"$set": {"expiry": "N/A"}})
            resp = f"""<b>
Plan Expired ⚠️

Message: Your Current Plan is Expired . To Regain Access Purchase Again Our One Of Plan .

Type /buy To Purchase Plan
</b>"""
            resp = urllib.parse.quote_plus(resp)
            BOT_TOKEN = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["BOT_TOKEN"]
            session = httpx.AsyncClient()
            try:
                await session.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={user_id}&text={resp}&parse_mode=HTML")
            except:
                pass
            await session.aclose()

    except:
        pass
