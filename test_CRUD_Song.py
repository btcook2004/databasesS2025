import CRUD.CRUD_Song as CRUD_Song

option = 'Z'
print("SONG - CRUD TEST")
print("C - Create")
print("R - Read")
print("U - Update")
print("D - Delete")
print("Q - Quit")

while option != 'Q':
    option = input("----------Choose an option: ").upper()
    
    if option == 'C':
        SongTitle = input("Enter the title of the song: ")
        ArtistName = input("Enter the name of the artist: ")
        AlbumId = input("Enter the ID of the album or -1 if doesn't exist: ")
        AlbumName = input("Enter the title of the album: ")
        FeaturedArtist = input("Enter the name of the featured artist: ")
        Rating = input("Enter the rating of the song: ")
        Time  = input("Enter the time of the song: ")
        CRUD_Song.CreateSong(SongTitle, ArtistName, AlbumId, AlbumName, FeaturedArtist, Rating, Time)
    
    elif option == 'R':
        for row in CRUD_Song.ReadSong():
            print(row)
    
    elif option == 'U':
        SongId = input("Enter the ID of the song to update: ")
        SongTitle = input("Enter the NEW title of the song: ")
        ArtistName = input("Enter the NEW name of the artist: ")
        AlbumName = input("Enter the NEW title of the album: ")
        FeaturedArtist = input("Enter the NEW name of the featured artist: ")
        Rating = input("Enter the NEW rating of the song: ")
        Time  = input("Enter the NEW time of the song: ")

        CRUD_Song.UpdateSong(SongId, SongTitle, ArtistName, AlbumName, FeaturedArtist, Rating, Time)
    
    elif option == 'D':
        SongId = input("Enter the Id of the Song to delete: ")
        CRUD_Song.DeleteSong(SongId)
    
    elif (option == 'Q'):
        print("Exiting the program.")
    
    else:
        print("Invalid option. Please try again.")