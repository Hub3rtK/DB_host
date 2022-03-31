import mysql.connector

connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="strava2gl",
        auth_plugin ="mysql_native_password"
        )

current = connection.cursor()

current.execute("select * from statistics order by miles desc")
for i in current:
    print(i)

connection.close()
