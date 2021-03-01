from discord.ext import tasks, commands
import discord
import time

bot = commands.Bot(command_prefix = '>> ', self_bot = True)
token = "ODAyOTgxOTE4MTU2NzgzNjg2.YCk31w.KvFiwXkjUGxlRG5f3fbFtctnVsE"

@bot.command()
async def run(ctx):
    if ctx.author == bot.user:
        channel = ctx.channel

        async for message in channel.history(limit=9000):
            if message.author.id == bot.user.id:
                try:
                    print(f"Deleting message: {message.content}")
                    await message.delete()
                except:
                    print("Failed to delete message")

@bot.event
async def on_guild_join(guild):
    await guild.leave()
    print(f"Leaving {guild.name}")


bot.run(token, bot = False, reconnect = True)
