import json
import os
import multiprocessing
import platform
import speedtest
import psutil
from pyrogram import Client, filters
from FUNC.defs import *

async def get_ip_info(ip_address):
    try:
        import httpx
        session  = httpx.AsyncClient()
        response = await session.get(f"https://ipapi.co/{ip_address}/json/")
        response = response.json()
        city     = response["city"]
        country  = response["country_name"]
        org      = response["org"]
        await session.aclose()
        return city, country, org
    except:
        city    = "Not Found"
        country = "Not Found"
        org     = "Not Found"
        return city, country, org

async def get_current_script_cpu_usage():
    pid      = os.getpid()
    py       = psutil.Process(pid)
    cpuUsage = py.cpu_percent()
    return cpuUsage


async def get_current_script_ram_usage():
    pid       = os.getpid()
    py        = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2.0**30 
    return f"{memoryUse:.2f} GB"


async def get_global_network_usage():
    net_info = psutil.net_io_counters()
    sent     = net_info.bytes_sent / (1024**2) / 8
    received = net_info.bytes_recv / (1024**2) / 8
    return f"Sent: {sent:.2f} MB, Received: {received:.2f} MB"


async def get_internet_speed():
    sp             = speedtest.Speedtest()
    download_speed = int(sp.download()) / 8 / 100000
    upload_speed   = int(sp.upload()) / 8 / 100000
    return f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps"


async def get_server_stats():
    server_os          = platform.system()
    server_ip          = os.popen("curl https://api.ipify.org/").read().strip()
    city, country, org = await get_ip_info(server_ip)

    if server_os == "Windows":
        server_ram = os.popen('powershell "Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty TotalPhysicalMemory"').read()
        server_ram = f"{int(server_ram) / (1024 ** 3):.2f} GB"
        try:
            server_storage = os.popen("powershell \"(Get-WmiObject Win32_LogicalDisk | Where-Object {$_.DeviceID -eq 'C:'}).Size\"").read()
            server_storage = f"{int(server_storage) / (1024 ** 3):.2f} GB"
        except ValueError:
            server_storage = "N/A"
        server_core = multiprocessing.cpu_count()
        cpu_usage   = f"{psutil.cpu_percent()}%"

    else:
        server_ram = os.popen("free -h | grep -i Mem | awk '{print $2}'").read().strip()
        try:
            server_storage = (os.popen("df -h | grep -i /$ | awk '{print $2}'").read().strip())
        except ValueError:
            server_storage = "N/A"
        server_core = os.popen("nproc").read().strip()
        cpu_usage   = f"{psutil.cpu_percent()}%"

    server_internet_speed = await get_internet_speed()
    script_cpu_usage      = await get_current_script_cpu_usage()
    script_ram_usage      = await get_current_script_ram_usage()
    global_network_usage  = await get_global_network_usage()

    done = f"""<b>
MASTER Checker ⚡ Hosting Info Retrieved Successfully ✅
━━━━━━━━━━━━━━ 
Server Details:
Server OS : {server_os}
Server IP : {server_ip}
Server ISP : {org}
Server Location : {city} , {country}
Server Ram : {server_ram}
Server Storage : {server_storage}
Server Core : {server_core} 
Server CPU Usage : {cpu_usage}
Server Internet Speed : {server_internet_speed}

Application Details:
Application Name : MASTER Checker ⚡️
Application CPU Usage : {script_cpu_usage}
Application Ram Usage : {script_ram_usage}
Application Network Usage : {global_network_usage}
Application Uptime : 06 Hours 10 Min


Status : Running
    </b> """
    return done


@Client.on_message(filters.command("serverstats", [".", "/"]))
async def stats(Client, message):
    try:
        user_id     = str(message.from_user.id)
        OWNER_ID    = json.loads(open("FILES/config.json", "r" , encoding="utf-8").read())["OWNER_ID"]
        if user_id not in OWNER_ID:
            resp = """<b>You Don't Have Permission To Use This Command.    
Contact Bot Owner @FNxELECTRA !</b>"""
            await message.reply_text(resp, message.id)
            return

        delete = await message.reply_text("<b>Getting Server Stats...</b>", message.id) 
        done   = await get_server_stats()
        await Client.delete_messages(message.chat.id, delete.id)

        await message.reply_text(done, message.id)

    except:
        import traceback
        await error_log(traceback.format_exc())
