import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mycursor = mydb.cursor()

def CreateArtist():
    print("Create a new record in the ARTIST table:")
    ArtistName = input("Enter the name of the artist: ")
    ArtistRating = input("Enter the rating of the artist: ")

    mycursor.execute("INSERT INTO ARTIST (ArtistName, Rating) VALUES (%s, %s)", (ArtistName, ArtistRating))
    mydb.commit()
    
def ReadArtist():
    print("Read an existing record:")
    mycursor.execute("SELECT * FROM ARTIST")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)

def UpdateArtist():
    print("Update an existing record")
    ArtistName = input("Enter the name of the artist to update: ")
    ArtistRating = input("Enter the new rating of the artist: ")
    mycursor.execute("UPDATE ARTIST SET Rating = %s WHERE ArtistName = %s", (ArtistRating, ArtistName))
    mydb.commit()

def DeleteArtist():
    print("Delete a record")
    ArtistName = input("Enter the name of the artist to delete: ")
    mycursor.execute("DELETE FROM ARTIST WHERE ArtistName = %s", (ArtistName,))
    mydb.commit()
