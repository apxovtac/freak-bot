import discord
from discord.ext import commands
from discord.ext.commands.core import Command

class HCOM(commands.Cog, name= "helpcoammands"):

    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        helpembeds= discord.Embed(title= "HELP", description = "Use #help <commands> for extended information", color= 0x494BF5)
        helpembeds.add_field(name="Moderation", value="kick,ban,mute")
        helpembeds.add_field(name="INFO", value="about,owner")

        await ctx.message.channel.send(embed=helpembeds)


    @help.command()
    async def about(self,ctx):
        aboutem = discord.Embed(title="about", description ="Gives info about the server", color= 0x494BF5)
        aboutem.add_field(name="***Syntax***", value="#about")
        await ctx.message.channel.send(embed=aboutem)

    @help.command()
    async def owner(self,ctx):
        ownerem = discord.Embed(title="owner",description ="Gives names of the owners of the server ", color= 0x494BF5)
        ownerem.add_field(name="***Syntax***", value="#owner")
        await ctx.message.channel.send(embed=ownerem)

def setup(bot):
    bot.add_cog(HCOM(bot))
    print("helpmod cog is loaded")
