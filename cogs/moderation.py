import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.core import Command
snipe_message_author = {}
snipe_message_content = {}

class MOD(commands.Cog, name= "Moderation"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount=2):
        await ctx.channel.purge(limit= amount)


    @commands.command(name='kick')
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx,member : discord.Member,*,reason= "No reason Provided"):
        kickEmbed = discord.Embed(title= "Kicked", description = member.name+f" has been kicked from {self.ctx.member.guild.name},Because:"+reason, color= 0x494BF5)
        kickEmbed.set_footer(text="AMG")
        await ctx.message.channel.send(embed=kickEmbed)
        await member.kick(reason=reason)


    @commands.command(name='ban')
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx,member : discord.Member,*,reason= "No reason Provided"):
        banEmbed = discord.Embed(title= "Banned", description = member.name+f" has been banned from {self.ctx.member.guild.name}, Because:"+reason, color= 0x494BF5)
        banEmbed.set_footer(text=f"{self.ctx.member.guild.name}")
        await ctx.message.channel.send(embed=banEmbed)
        await member.ban(reason=reason)
    '''
    @commands.command(name='mute')
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        await member.add_roles(mutedRole, reason=reason)
        

        discordmembers = discord.utils.get(ctx.guild.roles, name="Discord Members")

        await member.remove_roles(discordmembers)

        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"You were muted in the server {guild.name} for {reason}")
    '''

    @commands.command(name="unmute")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx, member: discord.Member):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)

        discordmembers = discord.utils.get(ctx.guild.roles, name="Discord Members")
        await member.add_roles(discordmembers)

        await ctx.send(f"Unmuted {member.mention}")
        await member.send(f"You were unmuted in the server {ctx.guild.name}")

    @commands.command(name='mute')
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx,member: discord.Member,time=None,*,reason=None):
        if time== None:
            return await ctx.send('Please include time')
        
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        await member.add_roles(mutedRole, reason=reason)
        

        discordmembers = discord.utils.get(ctx.guild.roles, name="Discord Members")

        await member.remove_roles(discordmembers)
        smEmbed = discord.Embed(title= "Muted", description = f"Muted {member.mention} for {time} because reason {reason}",color= 0xFF0101)
        smEmbed.set_footer(text="11/11")
        await ctx.message.channel.send(embed=smEmbed)

        time_convert= {"s":1, "m":60,"h":3600,"d":86400}
        delay= int(time[:-1])* time_convert[time[-1]]
        await asyncio.sleep(delay)

        await member.remove_roles(mutedRole)
        await member.add_roles(discordmembers)
        smEmbed = discord.Embed(title= "Muted", description = f"Unmuted {member.mention}",color= 0xFF0101)
        smEmbed.set_footer(text="11/11")
        await ctx.message.channel.send(embed=smEmbed)

    @commands.command(name='slowmode')
    @commands.has_permissions(manage_messages=True)
    async def setdelay(self,ctx, time=None):
        if time== None:
            return await ctx.send('Please include time')
        time_convert= {"s":1, "m":60,"h":3600,"d":86400}
        delay= int(time[:-1])* time_convert[time[-1]]
        await ctx.channel.edit(slowmode_delay=delay)
        smEmbed = discord.Embed(title= "Slowmode", description = f"``Set the slowmode delay in this channel to {time} seconds!``",color= 0xFF0101)
        smEmbed.set_footer(text="11/11")
        await ctx.message.channel.send(embed=smEmbed)


    

  
    @commands.Cog.listener()
    async def on_message_delete(self,message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        await asyncio.sleep(60)
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]


    @commands.command()
    async def snipe(self,ctx):
        channel = ctx.channel 
        try:
            snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
            snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
            await ctx.message.channel.send(embed = snipeEmbed)
        except:
            await ctx.message.channel.send(f"There are no deleted messages in #{channel.name}")


def setup(bot):
    bot.add_cog(MOD(bot))
    print("mod cog is loaded")
