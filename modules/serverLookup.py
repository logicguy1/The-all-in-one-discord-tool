LICENSE = """
Copyright © 2021 Drillenissen#0666
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from colored import fg
import requests
import time
import sys

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def fetch_data():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {w}[{b}?{w}] Token: ")
    }

    guildId = input(f" {w}[{b}?{w}] Guild ID: ")

    response = requests.get(
        f"https://discord.com/api/guilds/{guildId}",
        headers = headers,
        params = {"with_counts" : True}
    ).json()

    owner = requests.get(
        f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
        headers = headers,
        params = {"with_counts" : True}
    ).json()

    print(f"""
Server Name: {response['name']} ~ {response['id']}
Icon URL: https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
Approximate Member Count: {response['approximate_member_count']}
Owner: {owner['user']['username']}#{owner['user']['discriminator']} ~ {response['owner_id']}
Region: {response['region']}
Vanity Invite: {response['vanity_url_code']}
""")

if __name__ == '__main__':
    fetch_data()
