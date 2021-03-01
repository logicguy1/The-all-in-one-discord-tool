from discord.ext import tasks, commands
import discord

from datetime import datetime
import requests
import asyncio
import random
import json
import time
import re
import os

if __name__ != '__main__': # If the file is imported we need a bit of extra information
    with open("dataPass", "r") as file: # Open the data passing file in read mode
        data = json.load(file) # Load the file and convert it to a dict
        bumpServers = data["bumpServers"] # Get the list of servers to bump
        snipeToken = data["snipeToken"] # Get the users token

bot = commands.Bot(command_prefix = '>> ', self_bot = True) # Setup the bot object

@bot.event
async def on_ready(): # Tell the user when the bot comes online
    global bumpServers
    global snipeToken
    
    print(f" [{datetime.now()}] Logged in as: {bot.user}\n") # Say who its logged in as

    with open("dataPass", "r") as file: # Open the data passing file in read mode
        data = json.load(file) # Load the file and convert it to a dict
        bumpServers = data["bumpServers"] # Get the list of servers to bump
        snipeToken = data["snipeToken"] # Get the users token

    if bumpServers is not None: # If there are any bumpServers we can start the bumper
        auto_bump.start() # Start the loop

@bot.event
async def on_message(message):
    if "discord.gift/" in message.content and message.author.id != bot.user.id: # Check there is discord.gift in the message and that the author of the code is not the user running the bot
        code = re.search(r"discord.gift/([a-zA-Z0-9]+)", message.content) # Find the discord gift code using regrex

        responce = requests.post( # Attepmt to claim the code using the discord api
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{code.group(1)}/redeem',
            headers = {"Authorization" : snipeToken}
        )

        # If there is not a guild the code was sent in a dm
        guildName = message.guild.name if message.guild is not None else f"{message.author.name}'s DM"

        if responce.status_code == 400: # Check if the code was valid
            print(f" [{datetime.now()}] Nitro Code Already Claimed or Invalid | Server: {guildName} | Author: {message.author} | Code: {code.group(1)}") # Tell the user its invalid
        else: # If it is not a responce code 400 the code is valid
            print(f" [{datetime.now()}] Nitro Code Successfully Sniped | Server: {guildName} | Author: {message.author} | Code: {code.group(1)}") # Tell the user its a valid code

    if "giveaway" in message.content.lower() and message.author.bot: # If the message has giveaway in it and is sent by a bot
        await asyncio.sleep(2) # Wait a bit

        if len(message.reactions) == 0: # If the message has 0 reactions
            return # End the script

        try:
            await asyncio.sleep( random.randint(300, 1200) ) # Wait between 5 to 20 minutes
            await message.add_reaction(message.reactions[0]) # Add the first reaction thats on the message
        except discord.errors.Forbidden: # If the reaction was removed during the wait time this will be called
            print(f" [{datetime.now()}] Unable to snipe giveaway in {message.guild.name} \n {message.jump_url}") # Tell the user the giveaway was not able to be sniped
        else: # If there was no errors
            print(f" [{datetime.now()}] Sniped giveaway in {message.guild.name} \n [{datetime.now()}] {message.jump_url}") # Tell the user the giveaway was sniped

@tasks.loop(minutes = 121) # The amount between each bump can be set here
async def auto_bump(): # Bump discord servers every two hours
    for i in bumpServers: # Loop over all the servers to bump
        try: # We need a try incase a bump channel gets removed or the bot gets banned from a server
            guild = bot.get_guild(i["guildId"]) # Get the guild
            channel = guild.get_channel(i["channelId"]) # Get the channel

            await channel.send("!d bump") # Bump the channel
        except: # If the server or channel cant be found
            pass # Do nothing

if __name__ == '__main__': # If the file is getting ran directly
    bot.run( # Run the bot
        "TOKEN",
        bot = False,
        reconnect = True
    )
