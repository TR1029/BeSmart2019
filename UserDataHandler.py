
def getFName(aadvantageid):
	id ="aadvantageid='"+str(aadvantageid)+"'"
	from dbAccess import selectSQLGen 
	data = {
	'table' : ['users'],
	'values' : ['firstName'],
	'where' : [id]
	}
	statement = selectSQLGen(data)
	import teradatasql
	con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
	cur = con.cursor()
	cur.execute(statement)
	return cur.fetchall()

def getLName(aadvantageid):
	id ="aadvantageid='"+str(aadvantageid)+"'"
	from dbAccess import selectSQLGen 
	data = {
	'table' : ['users'],
	'values' : ['lastName'],
	'where' : [id]
	}
	statement = selectSQLGen(data)
	import teradatasql
	con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
	cur = con.cursor()
	cur.execute(statement)
	return cur.fetchall()

def getGender(aadvantageid):
	id ="aadvantageid='"+str(aadvantageid)+"'"
	from dbAccess import selectSQLGen 
	data = {
	'table' : ['users'],
	'values' : ['gender'],
	'where' : [id]
	}
	statement = selectSQLGen(data)
	import teradatasql
	con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
	cur = con.cursor()
	cur.execute(statement)
	return cur.fetchall()


#TESTS
# print(getFName(12345))
# print(getLName(12345))
# print(getGender(12345))