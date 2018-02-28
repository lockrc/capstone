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
        cursor.execute("SELECT * FROM %s WHERE datadatetime = %s", location, row[0])
        row_count = cursor.rowcount
        print row_count
        if row_count == 0:
            print row[0]
        # cursor.execute("INSERT INTO %s (datadatetime, powerproduction) "
        #               "VALUES (%s,%s)", location, row[0], row[21])
