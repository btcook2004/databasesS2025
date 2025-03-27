CREATE TABLE Artist(
  ArtistName varchar(255),
  Rating int,
  PRIMARY KEY (ArtistName)
);

CREATE TABLE Song(
  SongId int AUTO_INCREMENT,
  SongTitle varchar(255),
  ArtistName varchar(255),
  AlbumTitle varchar(255),
  FeaturedArtist varchar(255),
  Rating int,
  Time int,
  PRIMARY KEY(SongId),
  FOREIGN KEY(ArtistName) REFERENCES Artist(ArtistName)
);

CREATE TABLE Album(
  AlbumName varchar(255),
  ArtistName varchar(255),
  NumSong int,
  Rating int,
  ReleaseYear int,
  PlayTime int,
  PRIMARY KEY (AlbumName),
  FOREIGN KEY(ArtistName) REFERENCES Artist(ArtistName)
);

CREATE TABLE Genre(
  GenreId int,
  GenreName varchar(255),
  AlbumName varchar(255),
  ArtistName varchar(255),
  SongId int,
  PRIMARY KEY (GenreId),
  FOREIGN KEY(AlbumName) REFERENCES Album(AlbumName),
  FOREIGN KEY(ArtistName) REFERENCES Artist(ArtistName),
  FOREIGN KEY(SongId) REFERENCES Song(SongId)
);