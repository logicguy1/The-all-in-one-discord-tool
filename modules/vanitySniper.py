LICNECE = """
Copyright © 2021 Drillenissen#0666
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import datetime
import time

import requests
from colored import fg

r = fg(241)  # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)


def changeVanity(code, server, token):
    response = requests.patch(
        f"https://discord.com/api/v9/guilds/{server}/vanity-url",
        headers={"authorization": token},
        json={"code": code},
    )
    if response.status_code == 200:
        print(
            f" {r2}[{b}!{r2}] Updated invite successfully, your server can now be accessed by 'discord.gg/{code}'."
        )
        return True
    else:
        print(f" {r2}[{b}!{r2}] Failed to update vanity url.")
        return False


def checkVanity(url):
    response = requests.get(f"https://discord.com/api/v9/invites/{url}")
    if response.status_code == 404:
        return True
    return False


def snipe():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")
    code = input(f" {r2}[{b}?{r2}] Vanity code to snipe: ")
    serverId = input(f" {r2}[{b}?{r2}] Server to apply vanity to: ")
    delay = int(input(f" {r2}[{b}?{r2}] Delay between checks (seconds): "))

    try:
        success = False
        while not success:
            time.sleep(delay)
            success = checkVanity(code)

            curTime = datetime.datetime.now().strftime("%X")
            print(f" {r2}[{b}+{r2}] Last updated {curTime} \r", end="", flush=True)

        changeVanity(code, serverId, token)

    except KeyboardInterrupt:
        pass
