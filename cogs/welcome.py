import discord
from discord import embeds
from discord import channel
from discord.ext import commands
from discord import Intents

class WELCOME(commands.Cog, name= "Welcome"):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel= self.bot.get_channel(843118605511163906)
        emwel= discord.Embed(description=f'Hi {member.mention} welcome to the {self.member.guild.name}')
        await channel.send(embed= emwel)


def setup(bot):
    bot.add_cog(WELCOME(bot))
    print("welcome cog is loaded")

