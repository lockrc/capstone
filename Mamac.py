#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2018 Richard Lock (lockrc@appstate.edu)
# GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>

import mysql.connector
import untangle
import time

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

now = time.mktime(time.localtime()) % 900
total = 0
while True:
    obj = untangle.parse('http://152.10.10.162/sm101.xml')
    total = total + float(obj.Maverick.Minute.PreviousMinute.cdata)
    prevtime = now
    now = time.mktime(time.localtime()) % 900
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if(prevtime > now):
        prevtime = now
        total = total / 250
        print "15 minute generation: " + str(total)
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cursor.execute("INSERT INTO mountarray (datadatetime, powerproduction) "
                       "VALUES (\"" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\"," + str(total) + ")")
        reidb.commit()
        total = 0
    time.sleep(60 - (time.mktime(time.localtime()) % 60))
