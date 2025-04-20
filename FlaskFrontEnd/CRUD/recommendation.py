import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def getRecommendations(seconds):
    # use a sql statement to get songs with the same genre as the songs in the input list
    minutes = int(seconds) * 60
    sql = """
    SELECT SongId, SongTitle, ArtistName, Time 
    FROM Song
    WHERE Time <= %s
    ORDER BY Time DESC
    """
    val = (minutes, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    # Generate a playlist where the total time is as close as possible to the given minutes
    recommendations = []
    total_time = 0

    for song in myresult:
        if total_time + song[3] <= minutes:
            recommendations.append(song)
            total_time += song[3]
    # The second SQL execution and redundant loop are removed


    # Also return the total time of the playlist
    totalTime = round(sum([song[3] for song in recommendations]) / 60, 2)
    return recommendations, totalTime