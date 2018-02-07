#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2018 Richard Lock (lockrc@appstate.edu)
# GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>

import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='reidb',
    host='localhost',
    database='rei')
cnx.close()
