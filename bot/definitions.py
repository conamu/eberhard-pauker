from csvHandler import *

def hausaufgaben():

    # First sync list with date to to archive old Assignments.
    syncWithDate()

    # Get List of Assignments and display them.
    records = getHa(HA_RECORDS)
    recordArray = []
    lineNumber = 1

    for record in records:
        rowString = f"{lineNumber}. " + " | ".join(record)
        recordArray.append(rowString)
        lineNumber += 1

    return "Hier geht es zu unserem Moodle: https://moodle.oszimt.de/ \nFolgende Aufgaben sind noch zu erledigen\n" + "\n".join(recordArray)

def showArchive():

    # Sync with date to archive old assignments.
    syncWithDate()

    # Show list of archived assignments
    records = getHa(HA_RECORDS_ARCHIVE)
    recordArray = []
    lineNumber = 1

    for record in records:
        rowString = f"{lineNumber}. " + " | ".join(record)
        recordArray.append(rowString)
        lineNumber += 1

    return "Folgende Aufgaben sind bereits Abgelaufen: \n" + "\n".join(recordArray)


def eintr(fach, link, termin):
    putHa([fach, link, termin], 0, HA_RECORDS)


def abstimmen(*args):

    return


def loesch(line):

    # Sync with date to archive old assignments.
    syncWithDate()

    # Get current assignment list and put every entry back but the selected one.
    currentRecords = getHa(HA_RECORDS)
    currentLine = 1
    lineToDelete = int(line)
    updatedRecords = []

    for row in currentRecords:
        if currentLine != lineToDelete:
            updatedRecords.append(row)
        currentLine += 1

    putHa(updatedRecords, 1, HA_RECORDS)

    return f"Ich habe den eintrag Nr.{line} gelöscht!"