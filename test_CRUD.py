import CRUD_Artist

option = 'Z'
while option != 'Q':
    print("CRUD TEST")
    print("C - Create")
    print("R - Read")
    print("U - Update")
    print("D - Delete")
    print("Q - Quit")
    option = input("Choose an option: ").upper()
    if option == 'C':
        CRUD_Artist.CreateArtist()
    elif option == 'R':
        CRUD_Artist.ReadArtist()
    elif option == 'U':
        CRUD_Artist.UpdateArtist()
    elif option == 'D':
        CRUD_Artist.DeleteArtist()
    elif option == 'Q':
        print("Exiting the program.")
    else:
        print("Invalid option. Please try again.")