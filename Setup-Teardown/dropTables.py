import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS album, artist, genre, song")