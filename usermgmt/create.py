import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

# print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("create database emp")
mycursor.execute("show database")
for x in mycursor:
    print(x)
