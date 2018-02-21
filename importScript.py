#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2018 Richard Lock (lockrc@appstate.edu)
# GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>

import csv
import mysql.connector
from mysql.connector import errorcode
import time

start = time.clock()
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

# Import csv File #
csv_data = csv.reader(file('SinceNov1 2.csv'))
for row in csv_data:
    if row[1] == "":
        row.remove("")
        row.append(0)
        cursor.execute("INSERT INTO mountarray "
                       "(datadatetime, powerproduction) "
                       "VALUES (%s,%s)", row)
    else:
        cursor.execute("INSERT INTO mountarray "
                       "(datadatetime, powerproduction) "
                       "VALUES (%s,%s)", row)
    reidb.commit()
end = time.clock()

print "Time Elapsed: "
print end-start

print "\nSuccess!"

time.sleep(10)
reidb.close()
