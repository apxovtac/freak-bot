import discord
from discord.ext import commands
from discord.ext import commands
import os
import random
import asyncio
import datetime
import sys
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


class INFO(commands.Cog, name= "Information"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='about')
    async def about(self,context):
        

        myEmbed = discord.Embed(title= "about Aau Maya Garam", description = "Welcome to AMG (aau maya garam) a community server created to hang out and chill with friends", color= 0x494BF5)
        myEmbed.set_footer(text="AMG")
        await context.message.channel.send(embed=myEmbed)

    @commands.command(name='owner')
    async def owner(self,context):
        myEmbed = discord.Embed(title= "Owner of 11/11", description = "The Owner of 11/11 is \n ***lordRagnvald(LORD)***", color= 0x494BF5)
        myEmbed.set_footer(text="AMG")
        await context.message.channel.send(embed=myEmbed)



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def userinfo(self,ctx,member: discord.Member = None):
      if member == None:
        member = ctx.author
      try:
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
        color = discord.Color(0xff3400),
        title = f"{ctx.author}")
        embed.add_field(name="**•ID•**", value=f"{member.id}", inline=True)
        embed.add_field(name="**•Status•**", value=str(member.status).replace("dnd", "Do Not Disturb"), inline=True)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"**•Roles• ({len(ctx.author.roles) - 1})**", value='• '.join([role.mention for role in roles]), inline=False)
        embed.add_field(name="**•Account Created At•**", value=f"{member.created_at.date()}".replace("-", "/"), inline=True)
        embed.add_field(name="**•Joined Server At•**", value=f"{member.joined_at.date()}".replace("-", "/"), inline = True)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.message.channel.send(embed=embed)
      except:
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(
        color = discord.Color(0xff3400),
        title = f"{member}")
        embed.add_field(name="**•ID•**", value=f"{member.id}", inline=True)
        embed.add_field(name="**•Status•**", value=str(member.status).replace("dnd", "Do Not Disturb") , inline=True)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name=f"**•Roles• (0)**", value="No roles", inline=False)
        embed.add_field(name="**•Account Created At•**", value=f"{member.created_at.date()}".replace("-", "/"), inline=True)
        embed.add_field(name="**•Joined Server At•**", value=f"{member.joined_at.date()}".replace("-", "/"), inline = True)
        embed.set_footer(icon_url = f"{ctx.author.avatar_url}", text = f"Requested by {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.message.channel.send(embed=embed)



    
   

    @commands.command(name='serverinfo')
    @commands.guild_only()
    async def serverinfo(self,ctx):
        embed = discord.Embed(
            color = discord.Color(0xff3400)
        )
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        embed.set_thumbnail(url = str(ctx.guild.icon_url))
        embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
        await ctx.message.channel.send(embed=embed)



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self,ctx, *, question=None):
        if question == None:
            await ctx.send("Please write a poll!")
        else:
          icon_url = ctx.author.avatar_url 

          pollEmbed = discord.Embed(title = "New Poll!", description = f"{question}")

          pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)

          pollEmbed.timestamp = ctx.message.created_at 

          await ctx.message.delete()

          poll_msg = await ctx.message.channel.send(embed = pollEmbed)

          await poll_msg.add_reaction("⬆️")
          await poll_msg.add_reaction("⬇️")



def setup(bot):
    bot.add_cog(INFO(bot))
    print("info cog is loaded")
