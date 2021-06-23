
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



client =  commands.Bot(command_prefix=">", intents=intents)
client.remove_command("help")



 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="L O R D"))
    print('Im Ready')
    



@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()



'''
@client.command(name='dm')
async def DM(ctx, member: discord.Member, *, text):
    message = ctx.message
    await message.delete()
    await member.send(f"{text}")


@client.event
async def on_message(message: discord.Message):
    if message.content == "F" or message.content == "f":
        mention = message.author.mention
        await message.channel.send(f"{mention} has paid their respect")
    
    msg_dump_channel = 844099753549365288
    channel = client.get_channel(msg_dump_channel)
    if message.guild is None and not message.author.bot:
        # if the channel is public at all, make sure to sanitize this first
        naamid = message.author.display_name
        naam=message.author.id
        await channel.send(f"DM from: ***{naamid}***\nDM id: ***{naam}***\nMESSAGE: {message.content}")
    await client.process_commands(message)

'''
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






client.run(TOKEN)
