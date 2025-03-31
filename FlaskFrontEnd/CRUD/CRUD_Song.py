import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

# Pass in AlbumId if it exists, otherwise it creates an album with AlbumName
def CreateSong(SongTitle, ArtistName, AlbumId, AlbumName, FeaturedArtist, Rating, Time):
    # if artist is not already in artist table, insert it
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is None:
        print("Artist not found")
        mycursor.execute("INSERT INTO ARTIST (ArtistName) VALUES (%s)", (ArtistName,))
        mydb.commit()

    # if featured artist is not already in artist table, insert it
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (FeaturedArtist,))
    result = mycursor.fetchone()
    if result is None:
        print("Featured artist not found")
        mycursor.execute("INSERT INTO ARTIST (ArtistName) VALUES (%s)", (FeaturedArtist,))
        mydb.commit()

    # if album is not already in album table, insert it
    mycursor.execute("SELECT * FROM ALBUM WHERE AlbumId = %s", (AlbumId,))
    result = mycursor.fetchone()
    if result is None:
        print("Album not found, creating new album")
        mycursor.execute("INSERT INTO ALBUM (AlbumName, ArtistName) VALUES (%s, %s)", (AlbumName,ArtistName))
        #get the new album ID by album name and artist name
        mycursor.execute("SELECT AlbumId FROM ALBUM WHERE AlbumName = %s AND ArtistName = %s", (AlbumName, ArtistName))
        result = mycursor.fetchone()
        AlbumId = result[0]
        mydb.commit()

    mycursor.execute("INSERT INTO SONG (SongTitle, ArtistName, AlbumId, FeaturedArtist, Rating, Time) VALUES (%s, %s, %s, %s, %s, %s)", (SongTitle, ArtistName, AlbumId, FeaturedArtist, Rating, Time))
    mydb.commit()
    
# def ReadSong():
#     mycursor.execute("SELECT * FROM SONG")
#     myresult = mycursor.fetchall()
#     return myresult
def ReadSong():
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM SONG")
        myresult = cursor.fetchall()
        return myresult

def UpdateSong(SongId, SongTitle, ArtistName, AlbumId, FeaturedArtist, Rating, Time):
    #check if new albumId exists, if not create it
    mycursor.execute("SELECT * FROM ALBUM WHERE AlbumId = %s", (AlbumId,))
    result = mycursor.fetchone()
    if result is None:
        print("Album not found")
        return
    #check if new artist exists, if not creat it
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is None:
        print("Artist not found")
        mycursor.execute("INSERT INTO ARTIST (ArtistName) VALUES (%s)", (ArtistName,))
        mydb.commit()

    #check if new featured artist exists, if not creat it
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (FeaturedArtist,))
    result = mycursor.fetchone()
    if result is None:
        print("Featured artist not found") 
        mycursor.execute("INSERT INTO ARTIST (ArtistName) VALUES (%s)", (FeaturedArtist))
        mydb.commit()

    mycursor.execute("UPDATE SONG SET SongTitle = %s, ArtistName = %s, AlbumId = %s, FeaturedArtist = %s, Rating = %s, Time = %s WHERE SongId = %s", (SongTitle, ArtistName, AlbumId, FeaturedArtist, Rating, Time, SongId))
    mydb.commit()

def DeleteSong(SongId):
    #add in check for dependencies
    mycursor.execute("SELECT * FROM Genre WHERE SongId = %s", (SongId,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete song, it has genres associated with it.")
        return

    mycursor.execute("DELETE FROM SONG WHERE SongId = %s", (SongId,))
    mydb.commit()
