#File AAcares.py 

#Establish Database Connection
import teradatasql
con = teradatasql.connect('{"host":"168.61.186.29","user":"tuskegee_user","password":"tuskegee_user","dbs_port":"1025"}')
cur = con.cursor()
