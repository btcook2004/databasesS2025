import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def CreateArtist(ArtistName, Rating):
    mycursor.execute("INSERT INTO ARTIST (ArtistName, Rating) VALUES (%s, %s)", (ArtistName, Rating))
    # mydb.commit()
    
def ReadArtist():
    with mydb.cursor() as cursor:
        cursor.execute("SELECT * FROM ARTIST")
        myresult = cursor.fetchall()
        return myresult

def UpdateArtist(ArtistName, Rating):
    mycursor.execute("UPDATE ARTIST SET Rating = %s WHERE ArtistName = %s", (Rating, ArtistName))
    # mydb.commit()

def DeleteArtist(ArtistName):
    # Check for dependencies
    mycursor.execute("SELECT * FROM SONG WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete artist, they have songs associated with them as a main artist.")
        return
    mycursor.execute("SELECT * FROM SONG WHERE FeaturedArtist = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete artist, they have songs associated with them as a featured artist.")
        return
    mycursor.execute("SELECT * FROM Album WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete artist, they have albums associated with them.")
        return 
    mycursor.execute("SELECT * FROM Genre WHERE ArtistName = %s", (ArtistName,))
    result = mycursor.fetchone()
    if result is not None:
        print("Cannot delete artist, they have genres associated with them.")
        return
    
    mycursor.execute("DELETE FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    # mydb.commit()
