import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def CreateAlbum(AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime):
    # if artist is not already in artist table, insert it
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is None:
        print("Artist not found, adding to ARTIST table.")
        mycursor.execute("INSERT INTO ARTIST (ArtistName) VALUES (%s)", (ArtistName,))
        mydb.commit()

    mycursor.execute("INSERT INTO ALBUM (AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime) VALUES (%s, %s, %s, %s, %s, %s)", (AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime))
    mydb.commit()

def ReadAlbum():
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM ALBUM")
        myresult = cursor.fetchall()
        return myresult
    
def UpdateAlbum(AlbumId, AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime):
    #check if new artist exists, if not create it
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is None:
        print("Artist not found, adding to ARTIST table.")
        mycursor.execute("INSERT INTO ARTIST (ArtistName) VALUES (%s)", (ArtistName,))
        mydb.commit()

    mycursor.execute("UPDATE ALBUM SET AlbumName = %s, ArtistName = %s, NumSong = %s, Rating = %s, ReleaseYear = %s, PlayTime = %s WHERE AlbumId = %s", (AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime, AlbumId))
    mydb.commit()

def DeleteAlbum(AlbumId):
    #check for dependencies
    mycursor.execute("SELECT * FROM SONG WHERE AlbumId = %s", (AlbumId,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete album, it has songs associated with it.")
        return
    mycursor.execute("SELECT * FROM GENRE WHERE AlbumId = %s", (AlbumId,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete album, it has genres associated with it.")
        return

    mycursor.execute("DELETE FROM ALBUM WHERE AlbumId = %s", (AlbumId,))
    mydb.commit()