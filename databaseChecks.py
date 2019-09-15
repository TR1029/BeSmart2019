import teradatasql
import random
import string
con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
cur = con.cursor()
# statement2= "ALTER TABLE be_tuskegee.reservations ADD groups VARCHAR(1)"
# cur.execute(statement2)
# statement2= "ALTER TABLE be_tuskegee.aircrafts ADD pitch FLOAT"
# cur.execute(statement2)
# statement2= "UPDATE be_tuskegee.aircrafts SET pitch='32' WHERE modelNO = '321'" 
# cur.execute(statement2)
# statement2= "UPDATE be_tuskegee.aircrafts SET pitch='32' WHERE modelNO = '757'"
# cur.execute(statement2)
# statement2= "UPDATE be_tuskegee.aircrafts SET pitch='31' WHERE modelNO = '738'"
# con.commit()


# from random import randint
# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)

# for tciNymbers in range(0,50000):
# 	print('0912'+str(random_with_N_digits(7)))
rand = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(6)])
group = random.randint(1,8)
# statement ="INSERT INTO be_tuskegee.reservations(userid,flightids,groups) VALUES ('"+rand+"',NEW arrayVec('123436', '345645', '5679:97'),'"+str(group)+"')"
statement = "ALTER TABLE be_tuskegee.aircrafts ADD seatplan ARRAYVEC"
print (statement)
cur.execute(statement)
print(cur.fetchall())
