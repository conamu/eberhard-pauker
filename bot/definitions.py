from csvHandler import *


def hausaufgaben():

    synchWithDate()
    records = getHa('ha_records.csv')
    recordArray = []
    lineNumber = 1

    for record in records:
        rowString = f"{lineNumber}. " + " | ".join(record)
        recordArray.append(rowString)
        lineNumber += 1

    return "Hier geht es zu unserem Moodle: https://moodle.oszimt.de/ \nFolgende Aufgaben sind noch zu erledigen\n" + "\n".join(recordArray)

def showArchive():

    synchWithDate()
    records = getHa('ha_archive.csv')
    recordArray = []
    lineNumber = 1

    for record in records:
        rowString = f"{lineNumber}. " + " | ".join(record)
        recordArray.append(rowString)
        lineNumber += 1

    return "Folgende Aufgaben sind bereits Abgelaufen: \n" + "\n".join(recordArray)


def eintr(fach, link, termin):
    putHa([fach, link, termin], 0, 'ha_records.csv')


def abstimmen(*args):
    return args


def loesch(line):

    currentRecords = getHa('ha_records.csv')
    currentLine = 1
    lineToDelete = int(line)
    updatedRecords = []

    for row in currentRecords:
        if currentLine != lineToDelete:
            updatedRecords.append(row)
        currentLine += 1

    putHa(updatedRecords, 1, 'ha_records.csv')

    return "Ich habe den ausgewählten Eintrag entfernt."


def help():
    # embeddedHelp = discord.Embed()
    # embeddedHelp.color('#E96A00')
    # embeddedHelp.title('Hilfeseite für Dr. Dr. Prof. Eberhard Pauker')
    # embeddedHelp.add_field(name='', value='', inline=True)
    # embeddedHelp.add_field(name='test', value='test', inline=True)

    return "Das sind meine Kompetenzen: \n" \
           "#hilfe => Dieses Hilfe Menü. \n" \
           "#HA => Eingetragene :notebook_with_decorative_cover: Hausaufgaben abrufen und zugehörige Abgabetermine \n" \
           "#löschen => Versehentlich Falsch eingetragene Hausaufgaben löschen. \n" \
           "#eintragen => Neuen Hausaufgaben eintrag erstellen. \n" \
           "    Folgendens Format muss beachtet werden: \n" \
           "    #eintragen <Fach> <link zur aufgabe> <Abgabetermin in DD.MM.JJJJ> \n" \
           "#abstimmung => Erstelle eine Abstimmung."
