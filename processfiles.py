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

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, 'mb-051*.csv'):
            processphotovoltaic(file, "libcirc", cursor)
            reidb.commit()


def processphotovoltaic(filename, location, cursor):
    # Import csv File #
    csv_data = csv.reader(file(filename))
    rownum = 0
    for row in csv_data:
        if rownum == 0:
            rownum = rownum + 1
            continue
        rows = cursor.execute("SELECT * FROM " + location + " WHERE datadatetime = \"" + row[0] + "\"")
        cursor.fetchall()
        format = "%Y-%m-%d %H:%M:%S"
        if cursor.rowcount == 0:
            print "Datetime: " + row[0] + "   Voltage: " + row[21]
            date = datetime.strptime(row[0], format)
            print date.tzname()
            est = pytz.timezone('America/New_York')
            dt = est.localize(date)
            dt = dt.strftime(format)
            print "Datetime: " + dt + "   Voltage: " + row[21]
            time.sleep(1)
            # cursor.execute("INSERT INTO " + location + " (datadatetime, powerproduction) "
            #               "VALUES (" + row[0] + "," + row[21] + ")")