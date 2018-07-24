#Admin Bot By Jacob Dean (1st Bot)

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk


bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("BOT READY")
    print("I am running on: "+bot.user.name)
    print("My user ID is: "+bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")
    await bot.say("That wasn't very helpful was it...")
    print("User has been pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find: ", color=0x0000ff)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print("All available info about the stated individual have been shown in an embed.")


@bot.command(pass_context=True)
async def kys(ctx, user: discord.Member):
    await bot.say("Shut the fuck up, {}".format(user.name))
    print("The user has been told to STFU")

@bot.command(pass_context=True)
@commands.has_role("King Of Tertorlia")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: {} Has been kicked from the server.".format(user.name))
    await bot.kick(user)
    print("The user stated has been kicked from the server")

@bot.command(pass_context=True)
async def offend(ctx, user: discord.Member):
    embed = discord.Embed(title="Ur Mum Is Gay", description="{}'s Mum Is Very Gay".format(user.name), color=0x00ff00)
    embed.set_footer(text="I Hope You Die Of Cancer")
    embed.set_author(name="AdminBot")
    embed.add_field(name="Die In A Car Fire", value="Nobody Loves You", inline=True)
    await bot.say(embed=embed)
    print("The user stated has been offended")

@bot.command(pass_context=True)
async def shrek(ctx):
    await bot.say("Shrek is love, Shrek is life...")
    print("Printed the Shrek command")

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print("All relevant server info has been shown")





bot.run("NDcxMjMyODg4MTc2OTAyMTY1.Djh7jQ.c3HJRq_n5FT0OCrL9xekNyDHO0A")

