import pandas as pd

import mysql.connector

# Database connection setup
db_config = {
  'user': 'User1',
  'password': 'password',
  'host': 'localhost',
  'database': 'Music'
}

# Read the CSV file
artist_csv = 'data/Artists.csv'
artists_data = pd.read_csv(artist_csv)
album_csv = "data/Albums.csv"
albums_data = pd.read_csv(album_csv)
song_csv = "data/Songs.csv"
songs_data = pd.read_csv(song_csv)

# Connect to the database
try:
  connection = mysql.connector.connect(**db_config)
  cursor = connection.cursor()

  # Insert data into the artists table
  insert_query = """
  INSERT INTO Artist 
  VALUES (%s, %s)
  """
  for _, row in artists_data.iterrows():
    cursor.execute(insert_query, tuple(row))

  # Commit the transaction
  connection.commit()

  # insert albums_data into the albums table
  insert_query = """
  INSERT INTO album (AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime)
  VALUES (%s, %s, %s, %s, %s, %s)
  """

  # commit the transaction
  for _, row in albums_data.iterrows():
    cursor.execute(insert_query, tuple(row))
  connection.commit()


  # insert data into the songs table
  # The song table is SongTitle, ArtistName, AlbumId, FeaturedArtist, Rating, and Time
  # find the AlbumId from the album table
  # the csv does not have FeaturedArist, so we will set it to null
  # user the AlbumName to find the AlbumId
  insert_query = """
  INSERT INTO song (SongTitle, ArtistName, AlbumId, Time, Rating)
  VALUES (%s, %s, (SELECT AlbumId FROM Album WHERE AlbumName = %s), %s, %s)
  """
  for _, row in songs_data.iterrows():
    print("run")
    print(row)
    cursor.execute(insert_query, (row['SongTitle'], row['ArtistName'], row['AlbumName'], row['Time'], row['Rating']))
  connection.commit()

except mysql.connector.Error as err:
  print(f"Error: {err}")
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()