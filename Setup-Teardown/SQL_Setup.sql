CREATE TABLE Artist(
  ArtistName varchar(255),
  Rating int,
  PRIMARY KEY (ArtistName)
);

CREATE TABLE Album(
  AlbumId int AUTO_INCREMENT,
  AlbumName varchar(255),
  ArtistName varchar(255),
  NumSong int,
  Rating int,
  ReleaseYear int,
  PlayTime int,
  PRIMARY KEY (AlbumId),
  FOREIGN KEY(ArtistName) REFERENCES Artist(ArtistName)
);

CREATE TABLE Song(
  SongId int AUTO_INCREMENT,
  SongTitle varchar(255),
  ArtistName varchar(255),
  AlbumId int,
  FeaturedArtist varchar(255),
  Rating int,
  Time int,
  PRIMARY KEY(SongId),
  FOREIGN KEY(ArtistName) REFERENCES Artist(ArtistName),
  FOREIGN KEY(FeaturedArtist) REFERENCES Artist(ArtistName),
  FOREIGN KEY(AlbumId) REFERENCES Album(AlbumId)
);

CREATE TABLE Genre(
  GenreId int AUTO_INCREMENT,
  GenreName varchar(255),
  AlbumId int,
  ArtistName varchar(255),
  SongId int,
  PRIMARY KEY (GenreId),
  FOREIGN KEY(AlbumId) REFERENCES Album(AlbumId),
  FOREIGN KEY(ArtistName) REFERENCES Artist(ArtistName),
  FOREIGN KEY(SongId) REFERENCES Song(SongId)
);