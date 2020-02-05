import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="emp"
)
mycursor = mydb.cursor()
mycursor.execute("select * from customers")
result = mycursor.fetchall()
for x in result:
    print(x)
# print(dir(mysql))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__path__', '__spec__']
#
# import mysql.connector
#
# print(dir(mysql))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__path__', '__spec__', 'connector']
