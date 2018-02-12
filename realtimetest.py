#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2018 Richard Lock (lockrc@appstate.edu)
# GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>

import mysql.connector
from mysql.connector import errorcode
import time
import random

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

while(1):
    time.sleep(1)
    print "TICK"
    num = random.random()
    cursor.execute("TRUNCATE live")
    cursor.execute("INSERT INTO live VALUES(NOW(), " + str(num) + ")")
    reidb.commit()

reidb.close()
