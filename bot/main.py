import os
from dotenv import load_dotenv

from definitions import *
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='#')


@bot.command()
async def eintragen(ctx, fach, link, termin):
    eintr(fach, link, termin)
    await ctx.send("Ich habe die Hausaufgabe erfolgreich abgespeichert!  :notebook_with_decorative_cover:")

@bot.command()
async def HA(ctx):
    await ctx.send(hausaufgaben())

@bot.command()
async def löschen(ctx, line):
    await ctx.send(loesch(line))

@bot.command()
async def abstimmung(ctx, *args):
    await ctx.send(abstimmen(*args))

@bot.command()
async def archiv(ctx):
    await ctx.send(showArchive())


@bot.event
async def on_ready():
    for server in bot.guilds:
        if server.name == SERVER:
            break

    print(
        f'{bot.user} is connected to the following servers:\n'
        f'{server.name}(id: {server.id})'
    )
bot.run(TOKEN)
