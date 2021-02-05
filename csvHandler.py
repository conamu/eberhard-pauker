import csv
import datetime


def getHa(file):
    with open(file) as haFile:
        csv_reader = csv.reader(haFile, delimiter=',')
        records = []
        elementCounter = 0
        for row in csv_reader:
            for element in row:
                if len(element) != 0:
                    elementCounter += 1
            if elementCounter == 3:
                records.append(row)
            elementCounter = 0
        return records


def putHa(record, mode, file):

    oldRecords = []

    if mode == 0:
        oldRecords = getHa('ha_records.csv')
        oldRecords.append(record)
    elif mode == 2:
        oldRecords = getHa('ha_archive.csv')
        for rec in record:
            oldRecords.append(rec)

    else:
        oldRecords = record

    with open(file, mode='w', newline='') as haFile:
        csv_writer = csv.writer(haFile, delimiter=",")

        for row in oldRecords:
            csv_writer.writerow(row)

def synchWithDate():

    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

    records = getHa('ha_records.csv')
    updatedRecords = []
    oldRecords = []

    for record in records:
        dateOfRecord = datetime.datetime.strptime(record[2], '%d.%m.%Y')
        if dateOfRecord >= tomorrow:
            updatedRecords.append(record)
        if dateOfRecord < tomorrow:
            oldRecords.append(record)

    putHa(updatedRecords, 1, 'ha_records.csv')
    putHa(oldRecords, 2, 'ha_archive.csv')

    return "Ich habe alle Aufgaben mit abgelaufenen Abgabeterminen Entfernt"