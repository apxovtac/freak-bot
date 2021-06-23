import discord
from discord.ext import commands
from discord.ext.commands.core import Command

class SPEAK(commands.Cog, name= "Speak"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="lol")
    async def lol(self,ctx, *, text):
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")


def setup(bot):
    bot.add_cog(SPEAK(bot))
    print("SPEAK cog is loaded")
