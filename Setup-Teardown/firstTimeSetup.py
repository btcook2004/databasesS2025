import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mycursor = mydb.cursor()
fp = open("SQL_Setup.sql")
sqlString = fp.read()
sqlCommands = sqlString.split(';')
for command in sqlCommands:
    mycursor.execute(command)
    
fp.close()

