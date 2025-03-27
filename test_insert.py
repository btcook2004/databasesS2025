import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mycursor = mydb.cursor()
fp = open("test_song_data.csv")
sqlString = fp.read()
sqlCommands = sqlString.split(';')
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# print(mydb)
# print("No Errors")