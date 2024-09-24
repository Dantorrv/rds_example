import pymysql

endpoint = "rds-primerentrega.cvq0gu80k5jn.us-east-1.rds.amazonaws.com"
userdb = 'admin'
passworddb = 'basededatos123' 

def connect2SQL():

    try:
        print("Connection was successful")
        obj_connect = pymysql.connect(
            host = endpoint,
            user = userdb,
            password = passworddb
        )
        return obj_connect

        

    except Exception as err:
        print("error:", err)
        obj_connect = None
        return obj_connect

def add_user(id,first_name,last_name,birthday):
    instruction_sql = "INSERT INTO db_users.Users (id, first_name, last_name, birthday) VALUES("+id+",'"+first_name+"','"+last_name+"','"+birthday+"')"
    obj_connect = connect2SQL()
    obj_connect.cursor().execute(instruction_sql)
    obj_connect.commit()
    print("user added")    