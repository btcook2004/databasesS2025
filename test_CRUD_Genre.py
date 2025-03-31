import FlaskFrontEnd.CRUD.CRUD_Genre as CRUD_Genre

option = 'Z'
print("GENRE - CRUD TEST")
print("C - Create")
print("R - Read")
print("U - Update")
print("D - Delete")
print("Q - Quit")

while option != 'Q':
  option = input("----------Choose an option: ").upper()
  
  if option == 'C':
      GenreName = input("Enter the name of the genre: ")
      AlbumId = input("Enter the id of the album: ")
      ArtistName = input("Enter the name of the artist: ")
      SongId = input("Enter the id of the song: ")
      CRUD_Genre.CreateGenre(GenreName, AlbumId, ArtistName, SongId)
  
  elif option == 'R':
      for row in CRUD_Genre.ReadGenre():
          print(row)
  
  elif option == 'U':
      GenreId = input("Enter the Id of the genre to update: ")
      GenreName = input("Enter the NEW name of the genre: ")
      AlbumId = input("Enter the NEW id of the album: ")
      ArtistName = input("Enter the NEW name of the artist: ")
      SongId = input("Enter the NEW id of the song: ")

      CRUD_Genre.UpdateGenre(GenreId, GenreName, AlbumId, ArtistName, SongId)
  
  elif option == 'D':
      GenreId = input("Enter the Id of the Genre to delete: ")
      CRUD_Genre.DeleteGenre(GenreId)
  
  elif (option == 'Q'):
      print("Exiting the program.")
  
  else:
      print("Invalid option. Please try again.")