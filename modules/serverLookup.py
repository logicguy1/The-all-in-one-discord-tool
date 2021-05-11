from colored import fg, attr
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

    guildId = input(f" {w}[{b}?{w}] Guild Id: ")

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
Server name: {response['name']} ~ {response['id']}
Icon URL: https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
Approxomate member count: {response['approximate_member_count']}
Owner: {owner['user']['username']}#{owner['user']['discriminator']} ~ {response['owner_id']}
Region: {response['region']}
Valnaty invite: {response['vanity_url_code']}
""")

if __name__ == '__main__':
    fetch_data()
