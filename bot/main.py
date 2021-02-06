from definitions import *
from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='/', help_command=None)

ha_records = open(HA_RECORDS, "w+")
ha_records_archive = open(HA_RECORDS_ARCHIVE, "w+")


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


@bot.command()
async def hilfe(ctx):
    # Display Help Menu as embed.
    await ctx.send(
        embed=discord.Embed(title="Dr.Dr.Prof. Eberhard Pauker | Hilfe", description="", color=0x00ff00)
        .add_field(name="#eintragen 'FACH' 'Link zur Aufgabe' 'Abgabetermin'", value="Abgelaufene Abgabetermine werden automatisch Archiviert.", inline=True)
        .add_field(name="#ha", value="Eine numerierte Liste der noch Anstehenden Hausaufgaben.", inline=True)
        .add_field(name="#löschen 'Nummer'", value="Lösche den Eintrag an der gewünschten Stelle.", inline=True)
        .add_field(name="#archiv", value="Eine Liste aus allen bisherigen, abgelaufenen Aufgaben.", inline=True)
        .add_field(name="#abstimmung 'Mehrere Themen/Stichpunkte'", value="Erstelle eine Abstimmung. "
                                                                          "Mit einem Thema ist es eine Ja/Nein Abstimmung,"
                                                                          "mehr Themen ergeben eine klassische Abstimmung (Noch nicht implementiert)", inline=True)
        .set_footer(text="Hilfemenü für Dr. Dr. Prof. Eberhard Pauker", icon_url="")
        .set_author(name="conamu | https://gitlab.ho-me.zone/conamu/eberhard-pauker", url="https://gitlab.ho-me.zone/conamu", icon_url=""))

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
