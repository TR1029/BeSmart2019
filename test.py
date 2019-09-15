import requests
import json
import sys
from subprocess import call
from collections import namedtuple
#r=requests.get("https://aaflightengine.herokuapp.com/flights?date=2019-09-06")
r=requests.get("https://ffewwe.herokuapp.com/flights?date=2019-08-30")
data = r.text
jj = json.loads(data)
print (jj[0])
print (jj[0].get('flightNumber'))
#for item in jj: 

#print(json.dumps(jj, sort_keys=False, indent=4))
 #flightStatement = INSERT INTO flights (flightNo, ori)
# Parse JSON into an object with attributes corresponding to dict keys.
#x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
#print (x)



