#Admin Bot By Jacob Dean (1st Bot)

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("BOT READY")
    print("AUTOBOTS, ROLL OUT!")
    print("I am running on: "+bot.user.name)
    print("My user ID is: "+bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")
    await bot.say("That wasn't very helpful was it...")
    print("User has been pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The user's name is: {}".format(user.name))
    await bot.say("The user's ID is: {}".format(user.id))
    await bot.say("The user's status is: {}".format(user.status))
    await bot.say("The user's highest role is: {}".format(user.top_role))
    await bot.say("The user joined the server at: {}".format(user.joined_at))


@bot.command(pass_context=True)
async def kys(ctx, user: discord.Member):
    await bot.say("Shut the fuck up, {}".format(user.name))





bot.run("NDcxMjMyODg4MTc2OTAyMTY1.Djh7jQ.c3HJRq_n5FT0OCrL9xekNyDHO0A")

