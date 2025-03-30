import CRUD.CRUD_Artist as CRUD_Artist

option = 'Z'
print("ARTIST - CRUD TEST")
print("C - Create")
print("R - Read")
print("U - Update")
print("D - Delete")
print("Q - Quit")

while option != 'Q':
    option = input("----------Choose an option: ").upper()
    if option == 'C':
        ArtistName = input("Enter the name of the artist: ")
        ArtistRating = input("Enter the rating of the artist: ")
        CRUD_Artist.CreateArtist(ArtistName, ArtistRating)
    
    elif option == 'R':
        for row in CRUD_Artist.ReadArtist():
            print(row)
    
    elif option == 'U':
        ArtistName = input("Enter the name of the artist to update: ")
        ArtistRating = input("Enter the new rating of the artist: ")
        CRUD_Artist.UpdateArtist(ArtistName, ArtistRating)
    
    elif option == 'D':
        ArtistName = input("Enter the name of the artist to delete: ")
        CRUD_Artist.DeleteArtist(ArtistName)
    
    elif (option == 'Q'):
        print("Exiting the program.")
    
    else:
        print("Invalid option. Please try again.")