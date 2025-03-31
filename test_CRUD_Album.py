import FlaskFrontEnd.CRUD.CRUD_Album as CRUD_Album

option = 'Z'
print("ALBUM - CRUD TEST")
print("C - Create")
print("R - Read")
print("U - Update")
print("D - Delete")
print("Q - Quit")

while option != 'Q':
    option = input("----------Choose an option: ").upper()

    if option == 'C':
        AlbumName = input("Enter the title of the album: ")
        ArtistName = input("Enter the name of the artist: ")
        NumSong = input("Enter the number of songs in the album: ")
        Rating = input("Enter the rating of the album: ")
        ReleaseYear = input("Enter the release year of the album: ")
        PlayTime = input("Enter the play time of the album: ")
        CRUD_Album.CreateAlbum(AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime)
    
    elif option == 'R':
        for row in CRUD_Album.ReadAlbum():
          print(row)
    
    elif option == 'U':
        AlbumId = input("Enter the ID of the album to update: ")
        AlbumName = input("Enter the NEW title of the album: ")
        ArtistName = input("Enter the NEW name of the artist: ")
        NumSong = input("Enter the NEW number of songs in the album: ")
        Rating = input("Enter the NEW rating of the album: ")
        ReleaseYear = input("Enter the NEW release year of the album: ")
        PlayTime = input("Enter the NEW play time of the album: ")
        CRUD_Album.UpdateAlbum(AlbumId, AlbumName, ArtistName, NumSong, Rating, ReleaseYear, PlayTime)
    
    elif option == 'D':
        AlbumId = input("Enter Album Id to delete: ")
        CRUD_Album.DeleteAlbum(AlbumId)
    
    elif (option == 'Q'):
        print("Exiting the program.")
    
    else:
        print("Invalid option. Please try again.")