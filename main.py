from asyncio.windows_events import INFINITE
import discord
from discord.ext import commands
import os
import random
import asyncio
import sys
from discord import Intents
import traceback
from discord.flags import Intents
intents = Intents.default()
intents.members= True



client =  commands.Bot(command_prefix="?", intents=intents)
client.remove_command("help")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        msg1 = await ctx.send("You can't do that")
        await asyncio.sleep(2)
        await ctx.message.delete()
        await asyncio.sleep(4)
        await msg1.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        msg2 = await ctx.send("Please include all required fields")
        await asyncio.sleep(2)
        await ctx.message.delete()
        await asyncio.sleep(4)
        await msg2.delete()


extensions=['cogs.speak','cogs.helpCommands','cogs.information','cogs.dmbot','cogs.moderation','cogs.welcome']

if __name__ =='__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Error loading {extension}',file=sys.stderr)
            traceback.print_exc()



client.run(token)
