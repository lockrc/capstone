import untangle
import json
import requests
import time

obj = untangle.parse('http://152.10.10.162/sm101.xml')
print obj.Maverick.GlobalCount.cdata
print obj.Maverick.CurrentDate.cdata + " " + obj.Maverick.CurrentTime.cdata
format = "%B %d, %Y %H:%M:%S"
dt = time.strptime(obj.Maverick.CurrentDate.cdata + " " + obj.Maverick.CurrentTime.cdata, format)
format = "%Y-%m-%d %H:%M:%S"
dtstr = time.strftime(format, dt)
print dtstr
