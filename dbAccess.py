
#Generates a select statement from a dictionary where the keys should be 
def selectSQLGen(data):
	statement ='SELECT '
	if('table' in data.keys() and 'values' in data.keys()):
		for index in range(0,len(data.get('values'))):
			if(index != 0):
				statement = statement + ", "+ str(data.get('values')[index])
			else:
				statement = statement + str(data.get('values')[index])
		statement += " FROM be_tuskegee." + data.get('table')[0] 
		if('where' in data.keys()):
			statement+= " WHERE " +  data.get('where')[0]
		return statement
	else:
		return 0;
	


#Generates a update statement from a dictionary where the keys should be 
def updateSQLGen(data):
	statement ='UPDATE '
	if('table' in data.keys() and 'values' in data.keys() and 'where' in data.keys()):
		statement += str(data.get('table')[0]) + " SET "
		for index in range(0,len(data.get('values'))):
			if(index != 0):
				statement = statement + ", "+ str(data.get('values')[index])
			else:
				statement = statement + str(data.get('values')[index])
		statement+= " WHERE " +  data.get('where')[0]
		return statement
	else:
		return 0;


#Generates a delete statement from a dictionary where the keys should be 
def deleteSQLGen(data):
	statement ='DELETE '
	if('table' in data.keys() and 'values' in data.keys()):
		for index in range(0,len(data.get('values'))):
			if(index != 0):
				statement = statement + ", "+ str(data.get('values')[index])
			else:
				statement = statement + str(data.get('values')[index])
		statement += " FROM be_tuskegee." + data.get('table')[0] 
		if('where' in data.keys()):
			statement+= " WHERE " +  data.get('where')[0]
		return statement
	else:
		return 0;

#Generates a update statement from a dictionary where the keys should be 
def insertSQLGen(data):
	statement ='INSERT INTO '
	if('table' in data.keys() and 'cols' in data.keys() and 'values' in data.keys()):
		statement += str(data.get('table')[0]) + "("
		for index in range(0,len(data.get('cols'))):
			if(index != 0):
				statement = statement + ", "+ str(data.get('cols')[index])
			else:
				statement = statement + str(data.get('cols')[index])
		statement+= ") VALUES (" 
		for index in range(0,len(data.get('values'))):
			if(index != 0):
				statement = statement + ", '"+ str(data.get('values')[index])+"'"
			else:
				statement = statement + "'"+ str(data.get('values')[index])+"'"
		statement += ")"
		return statement
	else:
		return 0;



#TESTS
# s = {
# 'values':['phoneNO', 'fName', 'lname'],
# 'table':['users'],
# 'where':["fname = 'Toby'"]

# }

# u = {
# 'values':["phoneNO = '+14439292124'", "'fName='Taiwo'", "lname='Raji'"],
# 'table':['users'],
# 'where':["fname = 'Tai'"]

# }

# d = {
# 'values':['phoneNO', 'fName', 'lname'],
# 'table':['users'],
# 'where':["fname = 'Toby'"]
# }


# i = {
# 'cols':['phoneNO', 'fName', 'lname'],
# 'table':['users'],
# 'values':['+12342342345' ,'Toby','someone']

# }

# print (selectSQLGen(s))
# print (updateSQLGen(u))
# print (deleteSQLGen(d))
# print (insertSQLGen(i))