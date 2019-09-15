import teradatasql


con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
cur = con.cursor()

from pymongo import MongoClient
client = MongoClient("mongodb://heroku_2bw59nbr:m1umeaeb00dtjrkapkaisc2pav@ds031968.mlab.com:31968/heroku_2bw59nbr")
statement2 = "DELETE FROM be_tuskegee.users"
cur.execute(statement2)
db = client['heroku_2bw59nbr']
flights = db.collection_names()
from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
for item in list(db.user.find({})):
	firstName=item.get('firstName')
	lastName=item.get('lastName')
	email=item.get('email')
	aadvantageid=item.get('aadvantageId')
	gender=item.get('gender')
	phoneNo = "+1"+'443'+str(random_with_N_digits(7))
	statement = "INSERT INTO be_tuskegee.users(firstName, lastName, email, aadvantageid, gender, phoneNo) " 
	statement += "VALUES ('"+str(firstName).replace("'"," ")+"','"+str(lastName).replace("'"," ")+"','"+str(email)+"','"+str(aadvantageid)+"','"+str(gender)+"','"+str(phoneNo)+"');" 
	cur.execute(statement)
