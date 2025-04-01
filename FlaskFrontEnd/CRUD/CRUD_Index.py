import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "User1",
  password = "password",
  database = "Music"
)
mydb.autocommit = True
mycursor = mydb.cursor()

def SearchBySong(songTitle):
    sql = "SELECT * FROM Song WHERE SongTitle LIKE %s"
    val = ("%" + songTitle + "%",)
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

    # Open the file
    fp = open(file_path, "r")
    # fp = open("BigTable.sql", "r")
    sql = fp.read()
    fp.close()


    with mydb.cursor() as cursor:
        cursor.execute(sql)
        myresult = cursor.fetchall()
        return myresult
    # return [1, 2, 3, 4, 5]

def UpdateBig():
    pass

def DeleteBig():
    pass