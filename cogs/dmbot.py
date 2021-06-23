import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import Command

class DMBOT(commands.Cog, name= "Dmbot"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='dm')
    async def DM(self,ctx, member: discord.Member, *, text):
        message = ctx.message
        await message.delete()
        await member.send(f"{text}")

    
    # @commands.Cog.listener()
    # async def on_message(self,message: discord.Message):
    #     msg_dump_channel = 844099753549365288
    #     channel = self.bot.get_channel(msg_dump_channel)
    #     if message.guild is None and not message.author.bot:
    #         # if the channel is public at all, make sure to sanitize this first
    #         naamid = message.author.display_name
    #         naam=message.author.id
    #         await channel.send(f"DM from: ***{naam}***,\nDM id: {naamid}\nMESSAGE: {message.content}")
    #     await bot.process_commands(message)



    # @commands.Cog.listener()
    # async def on_message(self,message: discord.Message):
    #     if message.content == "F" or message.content == "f":
    #         mention = message.author.mention
    #         await message.channel.send(f"{mention} has paid their respect")
    #     #await self.bot.process_commands(message)
        
    #     msg_dump_channel = 844099753549365288
    #     channel = self.bot.get_channel(msg_dump_channel)
    #     if message.guild is None and not message.author.bot:
    #         # if the channel is public at all, make sure to sanitize this first
    #         naamid = message.author.display_name
    #         naam=message.author.id
    #         await channel.send(f"DM from: ***{naamid}***\nDM id: ***{naam}***\nMESSAGE: {message.content}")
    #     await self.bot.process_commands(message)
        

    @commands.Cog.listener("on_message")
    async def dmdump(self,message):
        msg_dump_channel = 844099753549365288
        channel = self.bot.get_channel(msg_dump_channel)
        if message.guild is None and not message.author.bot:
            # if the channel is public at all, make sure to sanitize this first
            naamid = message.author.display_name
            naam=message.author.id
            await channel.send(f"DM from: ***{naamid}***\nDM id: ***{naam}***\nMESSAGE: {message.content}")
        #await self.bot.process_commands(message)
    
    # @commands.Cog.listener("on_message")
    # async def greet(self,message):
    #     Cheers= ["Hi", "hi", "Hello", "hello"]
    #     if message.content in Cheers:
    #         await message.channel.send('Hello again')
    #         await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(DMBOT(bot))
    print("dmbot cog is loaded")
