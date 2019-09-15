import requests 
import teradatasql
import random
#statement = "INSERT INTO be_tuskegee.flights(flightNo, origin, destination, distance, duration) VALUES ('1234','BRO','NME','12345','120');" 
statement2 = "DELETE FROM be_tuskegee.flights"
#endpoint = 'https://hackwarstdrest.aa.engagetom.com:1443/systems/hackwarwarsdb/queries'
#statement={'query':'INSERT INTO be_tuskegee.flights(flightNo, origin, destination, distance, duration) VALUES ("1234","BRO","NME",12345,120);'}

#r = requests.post(endpoint, data=statement, verify=False, auth=('tuskegee_user','tuskegee_user'))
#print(r.status_code)

#open connec 
con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
cur = con.cursor()
#cur.execute(statement)
cur.execute(statement2)
#rows=cur.fetchall()
#print(rows)
from pymongo import MongoClient
client = MongoClient("mongodb://heroku_2bw59nbr:m1umeaeb00dtjrkapkaisc2pav@ds031968.mlab.com:31968/heroku_2bw59nbr")
#cur.execute(statement2)
db = client['heroku_2bw59nbr']
models=['757','321','738']
for item in list(db.flight.find({})):
	print (item)
	flightNo=item.get('code')
	origin=item.get('originCode')
	destination=item.get('destinationCode')
	model = models[random.randint(0,2)]
	sdt = item.get('scheduledDepartureTime')
	sat = item.get('scheduledArrivalTime')
	edt = item.get('estimatedDepartureTime')
	eat = item.get('estimatedArrivalTime')
	duration = random.randint(60,140)
	distance = random.randint(90,120)

	#latitude=item.get('latitude')
	statement = "INSERT INTO be_tuskegee.flights(flightNo, origin, destination, model, duration, distance, scheduledDepartureTime, scheduledArrivalTime, estimatedDepartureTime, estimatedArrivalTime) " 
	statement += "VALUES ('"+str(flightNo)+"','"+str(origin)+"','"+str(destination)+"','"+str(model)+"','"+str(duration)+"','"+str(distance)+"','"+str(sdt)+"','"+str(sat)+"','"+str(edt)+"','"+str(eat)+"');" 
	#statement2 = "ALTER TABLE be_tuskegee.flights DROP scheduledArrivalTime, DROP scheduledDepartureTime, DROP estimatedArrivalTime, DROP estimatedDepartureTime;"
	#cur.execute(statement2)
	#statement2 = "ALTER TABLE be_tuskegee.flights ADD scheduledArrivalTime TIMESTAMP,ADD scheduledDepartureTime TIMESTAMP,ADD estimatedArrivalTime TIMESTAMP,ADD estimatedDepartureTime TIMESTAMP"
	#print (statement)
	cur.execute(statement)
