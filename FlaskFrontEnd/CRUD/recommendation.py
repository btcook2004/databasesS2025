import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def getRecommendations(id1, id2, id3, id4, id5):
    # use a sql statement to get songs with the same genre as the songs in the input list
    sql = """
    SELECT
        Song.SongId, Song.SongTitle, Song.ArtistName, Album.AlbumName, Genre.GenreName
    FROM
        Song
    JOIN
        Album ON Song.AlbumId = Album.AlbumId
    JOIN
        Genre ON Song.SongId = Genre.SongId
    WHERE
        Genre.GenreName IN (
            SELECT GenreName
            FROM Genre
            WHERE SongId IN (%s, %s)
        )
    """
    val = (id1, id2)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    recommendations = []
    for x in myresult:
        recommendations.append(x)
    return recommendations