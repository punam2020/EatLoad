import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="emp"
)
mycursor = mydb.cursor()
sql = "insert into customers(name,address) values(%s,%s)"
val = [("punam", "bangalore"), ("sunam", "bmp"), ("kedar", "bbsr")]
# mycursor.execute(sql, val)
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")
print(mycursor.lastrowid)
