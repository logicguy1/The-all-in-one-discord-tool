from discord.ext import tasks, commands
import discord

from datetime import datetime
from colored import fg, attr
import requests
import re

RED = fg(1)
RESET = attr(0)

bot = commands.Bot(command_prefix = '>> ', self_bot = True)
token = "MzkxMjE5NzA5Mzk3NDM0Mzk5.X_gIng._Iwtpo4yld4CUeyDt56_2lp_qx8"

@bot.event
async def on_ready():
    print(f"{datetime.now()} {RED}|{RESET} Logged in as: {bot.user}\n")

@bot.event
async def on_message(message):
    if "discord.gift/" in message.content: # and message.user.id != bot.user.id
        m = re.search(r"discord.gift/([a-zA-Z0-9]+)", message.content)

        responce = requests.post(
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{m.group(1)}/redeem',
            headers = {"Authorization" : token})

        if responce.status_code == 404:
            error = responce.json()["message"]
            print(RED + "{" + RESET + m.group(1) + RED + "}" + RESET + f" Nitro code found\n Code {RED}INVALID{RESET} ({error})")

bot.run(token, bot = False, reconnect = True)
