LICNECE = """
Copyright © 2021 Drillenissen#4268
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from colored import fg, attr
import requests
import time

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def token():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")

    print(f" {r2}[{b}+{r2}] Getting user information")
    time.sleep(.5)

    user = requests.get("https://discord.com/api/users/@me", headers = {'Authorization' : token})

    if user.status_code == 401:
        print(f" {r2}[{b}!{r2}] Invalid Token")
        return

    servers = requests.get("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
    relations = requests.get("https://discord.com/api/v8/users/@me/relationships", headers = {'Authorization' : token}).json()

    user = user.json()

    print(f"\n {r2}[{b}!{r2}] Valid Token")
    print(f" {r2}[{b}+{r2}] User: {user['username']}#{user['discriminator']} | Email: {user['email']}")
    print(f" {r2}[{b}+{r2}] Guilds: {len(servers)} | Friends: {len([i for i in relations if i['type'] == 1])}")

    inp = input(f"\n {r2}[{b}?{r2}] Do you want to download aditional data? (Y/n)")

    if "y" in inp.lower():
        # if user["premium_type"] == 0:
        #     nitro = "None"
        # elif user["premium_type"] == 1:
        #     nitro = "Nitro Classic"
        # elif user["premium_type"] == 2:
        #     nitro = "Normal Nitro"

        serversOT = ""
        for i in servers:
            serversOT += f"Name: {i['name']}\nId: {i['id']} Owner: {i['owner']}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"

        relationsOT = ""
        for i in relations:
            if i['type'] == 1:
                relationsOT += f"Friend: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"
            elif i['type'] == 2:
                relationsOT += f"Blocked: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"
            elif i['type'] == 3:
                relationsOT += f"Incomming: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"
            elif i['type'] == 4:
                relationsOT += f"Outgoing: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"

        if user['avatar'] is not None:
            avatar = f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png"
        else:
            avatar = "Not set"

        with open(f"TokenData {user['username']}#{user['discriminator']}.txt", "w", encoding = "utf-8") as file:
            file.write(
f"""~~~~~~~~~~~ USER INFORMATION ~~~~~~~~~~~
User: {user['username']}#{user['discriminator']}
Id: {user['id']}
Email: {user['email']}
Phone: {user['phone']}
Token: {token}
Avatar: {avatar}
2fA: {user['mfa_enabled']}
Languge: {user['locale']}

~~~~~~~~~~~ SERVER INFORMATOIN ~~~~~~~~~~~
{serversOT}
~~~~~~~~~~~ FRIEND INFORMATION ~~~~~~~~~~~
{relationsOT}""")

def webhook():
    webhook = input(f"\n {r2}[{b}?{r2}] Webhook Url: ")

    print(f" {r2}[{b}+{r2}] Webhook information")
    time.sleep(.5)

    responce = requests.get(
        webhook
    )

    if responce.status_code != 200:
        print(f" {r2}[{b}!{r2}] Invalid Webhook")
        return

    responce = responce.json()

    print(f"\n {r2}[{b}!{r2}] Valid Token")
    print(f" {r2}[{b}+{r2}] Name: {responce['name']} Id: {responce['id']}")
