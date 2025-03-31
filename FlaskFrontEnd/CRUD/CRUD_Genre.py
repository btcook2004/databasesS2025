import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def CreateGenre(GenreName, AlbumId, ArtistName, SongId):
    # if album is not already in album table, fail
    mycursor.execute("SELECT * FROM ALBUM WHERE AlbumId = %s", (AlbumId,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot add Genre, Album not found")
        return

    # if artist is not already in artist table, fail
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot add Genre, Artist not found")
        return

    # if song is not already in song table, fail
    mycursor.execute("SELECT * FROM SONG WHERE SongId = %s", (SongId,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot add Genre, Song not found")
        return

    mycursor.execute("INSERT INTO Genre (GenreName, AlbumId, ArtistName, SongId) VALUES (%s, %s, %s, %s)", (GenreName, AlbumId, ArtistName, SongId))
    mydb.commit()


def ReadGenre():
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM GENRE")
        myresult = cursor.fetchall()
        return myresult


def UpdateGenre(GenreId, GenreName, AlbumId, ArtistName, SongId):
    #make sure albumId exists
    mycursor.execute("SELECT * FROM ALBUM WHERE AlbumId = %s", (AlbumId,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot change Genre, Album not found")
        return
    
    #make sure artistName exists
    mycursor.execute("SELECT * FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot change Genre, Artist not found")
        return

    #make sure songId exists
    mycursor.execute("SELECT * FROM SONG WHERE SongId = %s", (SongId,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot change Genre, Song not found")

    mycursor.execute("UPDATE Genre SET GenreName = %s, AlbumId = %s, ArtistName = %s, SongId = %s WHERE GenreId = %s", (GenreName, AlbumId, ArtistName, SongId, GenreId))
    mydb.commit()

def DeleteGenre(GenreId):
    mycursor.execute("DELETE FROM Genre WHERE GenreId = %s", (GenreId,))
    mydb.commit()