import csv
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
HA_RECORDS = os.getenv('HA_RECORDS')
HA_RECORDS_ARCHIVE = os.getenv('HA_RECORDS_ARCHIVE')
POLL_RECORDS = os.getenv('POLL_RECORDS')


def getHa(file):

    # Open the File and return an array of records.
    with open(file, "r") as haFile:
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

    # Open the File and write an array of records
    # or add records to existing ones.
    oldRecords = []

    if mode == 0:
        oldRecords = getHa(HA_RECORDS)
        oldRecords.append(record)
    elif mode == 2:
        oldRecords = getHa(HA_RECORDS_ARCHIVE)
        for rec in record:
            oldRecords.append(rec)
    else:
        oldRecords = record

    with open(file, mode='w+', newline='') as haFile:
        csv_writer = csv.writer(haFile, delimiter=",")

        for row in oldRecords:
            csv_writer.writerow(row)

def syncWithDate():
    # Get tomorrows Date
    today = datetime.datetime.today()
    # archive and remove all old entries that
    records = getHa(HA_RECORDS)
    updatedRecords = []
    oldRecords = []

    for record in records:
        dateOfRecord = datetime.datetime.strptime(record[2], '%d.%m.%Y')
        dateOfRecordCorrected = dateOfRecord + datetime.timedelta(days=1)
        if dateOfRecordCorrected > today:
            updatedRecords.append(record)
        if dateOfRecordCorrected <= today:
            oldRecords.append(record)

    putHa(updatedRecords, 1, HA_RECORDS)
    putHa(oldRecords, 2, HA_RECORDS_ARCHIVE)

    return "Ich habe alle Aufgaben mit abgelaufenen Abgabeterminen Entfernt"