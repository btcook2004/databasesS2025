SELECT
    Song.SongId,
    Song.SoongTitle,
    Song.ArtistName,
    Album.AlbumName,
    Genre.GenreName
FROM
    Song
JOIN
    Album ON Song.AlbumId = Album.AlbumId
JOIN
    Genre ON Song.SongId = Genre.SongId


