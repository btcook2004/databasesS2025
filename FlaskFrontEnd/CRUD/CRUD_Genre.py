import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def CreateGenre(GenreName, SongId):
    # if song is not already in song table, fail
    mycursor.execute("SELECT * FROM SONG WHERE SongId = %s", (SongId,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot add Genre, Song not found")
        return

    mycursor.execute("INSERT INTO Genre (GenreName, SongId) VALUES (%s, %s)", (GenreName, SongId))
    mydb.commit()


def ReadGenre():
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM GENRE")
        myresult = cursor.fetchall()
        return myresult


def UpdateGenre(GenreId, GenreName, SongId):
    #make sure songId exists
    mycursor.execute("SELECT * FROM SONG WHERE SongId = %s", (SongId,))
    result = mycursor.fetchone()
    if result is None:
        print("Cannot change Genre, Song not found")

    mycursor.execute("UPDATE Genre SET GenreName = %s, SongId = %s WHERE GenreId = %s", (GenreName, SongId, GenreId))
    mydb.commit()

def DeleteGenre(GenreId):
    mycursor.execute("DELETE FROM Genre WHERE GenreId = %s", (GenreId,))
    mydb.commit()