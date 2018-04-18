#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2018 Richard Lock (lockrc@appstate.edu)
# GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>

import csv
import fnmatch
import os
import time
import mysql.connector
from datetime import datetime
import pytz
from mysql.connector import errorcode
import requests
import json
import untangle


def process():
    # Connect to the Database #
    try:
        reidb = mysql.connector.connect(user='root',
                                        password='reidb',
                                        host='localhost',
                                        database='rei')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    # Create database Cursor #
    cursor = reidb.cursor()

    # Process each file in the directory
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, 'mb-051*.csv'):
            processlibcirc(file, cursor)
            reidb.commit()
        if fnmatch.fnmatch(file, 'mb-004*.csv'):
            processwind(file, cursor)
            reidb.commit()
        if fnmatch.fnmatch(file, 'mb-017*.csv'):
            processST(file, "plemmons", cursor)
            reidb.commit()
        if fnmatch.fnmatch(file, 'mb-018*.csv'):
            processST(file, "varsitygym", cursor)
            reidb.commit()
        if fnmatch.fnmatch(file, 'mb-019*.csv'):
            processST(file, "summit", cursor)
            reidb.commit()
        if fnmatch.fnmatch(file, 'mb-021*.csv'):
            processST(file, "mountaineer", cursor)
            reidb.commit()
    processEnphase(cursor)
    processXML(cursor)
    reidb.commit()


def processlibcirc(filename, cursor):
    # Import csv File #
    csv_data = csv.reader(file(filename))
    rownum = 0
    for row in csv_data:
        if rownum == 0:
            rownum = rownum + 1
            continue
        format = "%Y-%m-%d %H:%M:%S"
        est = pytz.timezone('US/Eastern')
        utc = pytz.utc
        date = datetime.strptime(row[0], format)
        dt = utc.localize(date)
        dt = dt.astimezone(est)
        dtstr = dt.strftime(format)
        rows = cursor.execute("SELECT * FROM libcirc WHERE datadatetime = \"" + dtstr + "\"")
        cursor.fetchall()
        if cursor.rowcount == 0:
            if not (row[21] == ""):
                cursor.execute("INSERT INTO libcirc (datadatetime, powerproduction) "
                               "VALUES (\"" + dtstr + "\"," + str(float(row[21]) / 1000) + ")")


def processwind(filename, cursor):
    # Import csv File #
    csv_data = csv.reader(file(filename))
    rownum = 0
    for row in csv_data:
        if rownum == 0:
            rownum = rownum + 1
            continue
        format = "%Y-%m-%d %H:%M:%S"
        est = pytz.timezone('US/Eastern')
        utc = pytz.utc
        date = datetime.strptime(row[0], format)
        dt = utc.localize(date)
        dt = dt.astimezone(est)
        dtstr = dt.strftime(format)
        rows = cursor.execute("SELECT * FROM wind WHERE datadatetime = \"" + dtstr + "\"")
        cursor.fetchall()
        if cursor.rowcount == 0:
            if not (row[5] == ""):
                cursor.execute("INSERT INTO wind (datadatetime, powerproduction) "
                               "VALUES (\"" + dtstr + "\"," + row[5] + ")")


def processST(filename, table, cursor):
    # Import csv File #
    csv_data = csv.reader(file(filename))
    rownum = 0
    for row in csv_data:
        if rownum == 0:
            rownum = rownum + 1
            continue
        format = "%Y-%m-%d %H:%M:%S"
        est = pytz.timezone('US/Eastern')
        utc = pytz.utc
        date = datetime.strptime(row[0], format)
        dt = utc.localize(date)
        dt = dt.astimezone(est)
        dtstr = dt.strftime(format)
        rows = cursor.execute("SELECT * FROM " + table + " WHERE datadatetime = \"" + dtstr + "\"")
        cursor.fetchall()
        if cursor.rowcount == 0:
            if not (row[4] == ""):
                cursor.execute("INSERT INTO " + table + " (datadatetime, powerproduction) "
                               "VALUES (\"" + dtstr + "\"," + row[4] + ")")


def processEnphase(cursor):
    r = requests.get('https://api.enphaseenergy.com/api/v2/systems/664018/summary?key=67551e09a7f4aa3609816466b9c4a757&user_id=4e6a4d344d7a45790a')
    parsed_json = json.loads(r.text)
    format = "%Y-%m-%d %H:%M:%S"
    dtstr = time.strftime(format, time.localtime(parsed_json[u'last_interval_end_at']))
    rows = cursor.execute("SELECT * FROM legends WHERE datadatetime = \"" + dtstr + "\"")
    cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.execute("INSERT INTO legends (datadatetime, powerproduction) "
                       "VALUES (\"" + dtstr + "\"," + str(float(parsed_json[u'current_power']) / 1000) + ")")
