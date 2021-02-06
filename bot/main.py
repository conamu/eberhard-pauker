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
    # Command to insert a Homework entry.
    eintr(fach, link, termin)
    await ctx.send("Ich habe die Hausaufgabe erfolgreich abgespeichert!  :notebook_with_decorative_cover:")

@bot.command()
async def ha(ctx):
    # Command to get all pending Homework assignments.
    await ctx.send(hausaufgaben())

@bot.command()
async def löschen(ctx, line):
    # Command to delete a Homework assignment from the List.
    await ctx.send(loesch(line))

@bot.command()
async def abstimmung(ctx, *args):
    # Command to create a poll.
    await ctx.send(abstimmen(*args))

@bot.command()
async def archiv(ctx):
    # Comman to view the Archive of old Assignments.
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
