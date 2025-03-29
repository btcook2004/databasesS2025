import mysql.connector
import csv

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mycursor = mydb.cursor()

#insert a row of csv into song table
fp = open("test_song_data.csv")
newData = fp.read()
title = ""

#Read the CSV file
with open("test_artist_data.csv", newline='') as csvfile:
  csvreader = csv.reader(csvfile)
  # next(csvreader)  # Skip the header row if it exists

  # # Insert each row into the artists table
  # for row in csvreader:
  #   artist_name, rating = row
  #   sql = """
  #   INSERT INTO Artist (ArtistName, Rating)
  #   VALUES (%s, %s)
  #   """
  #   mycursor.execute(sql, (artist_name, rating))


# # Read the CSV file
# with open("test_song_data.csv", newline='') as csvfile:
#   csvreader = csv.reader(csvfile)
#   # next(csvreader)  # Skip the header row if it exists

#   # Insert each row into the songs table
#   for row in csvreader:
#     song_title, artist_name, album_title, featured_artist, rating, time = row
#     sql = """
#     INSERT INTO Song (SongTitle, ArtistName, AlbumTitle, FeaturedArtist, Rating, Time)
#     VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     mycursor.execute(sql, (song_title, artist_name, album_title, featured_artist, rating, time))

# # Commit the transaction
# mydb.commit()


# fp = open("test_song_data.csv")
# sqlString = fp.read()
# sqlCommands = sqlString.split(';')
# for command in sqlCommands:
#   mycursor.execute(command)
for x in mycursor:
  print(x)

# print(mydb)
# print("No Errors")