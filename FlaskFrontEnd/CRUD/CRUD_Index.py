import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def SearchBySong(songTitle, artistName):
    # HEY!!! join the genre and album info
    sql = "SELECT * FROM Song WHERE SongTitle LIKE %s AND ArtistName LIKE %s"
    val = ("%" + songTitle + "%", "%" + artistName + "%")
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult

def CreateBig():
    pass

def ReadBig():
    import os

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to BigTable.sql
    file_path = os.path.join(script_dir, "BigTable.sql")
    # print(file_path)

    fp = open(file_path, "r")
    sql = fp.read()
    fp.close()


    with mydb.cursor() as cursor:
        cursor.execute(sql)
        myresult = cursor.fetchall()
        return myresult


def getAverageSong():
    #get the average song length from the database
    sql = "SELECT AVG(Time) FROM Song"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][0]

def UpdateBig():
    pass

def DeleteBig():
    pass

def getAverageRating():
    #get the average rating from the database
    sql = """   
    SELECT Album.AlbumName, Album.ArtistName, AVG(Song.Rating) AS AverageRating
    FROM Song
    INNER JOIN Album ON Song.AlbumId = Album.AlbumId
    GROUP BY Album.AlbumName, Album.ArtistName
    HAVING AVG(Song.Rating) > 1
    ORDER BY AverageRating DESC
    LIMIT 5;
    """
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def artistWithHighestSongAverage():
    sql = """
        SELECT
            ArtistName,
            AVG(Rating) AS AverageSongRating
        FROM
            Song
        GROUP BY
            ArtistName
        ORDER BY
            AverageSongRating DESC
        LIMIT 1;
    """
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult