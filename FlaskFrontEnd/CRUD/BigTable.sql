SELECT 
    Song.SongTitle,
    Artist.ArtistName,
    Album.AlbumName,
    Genre.GenreName
FROM 
    Song
JOIN 
    Album ON Song.AlbumId = Album.AlbumId
JOIN 
    Artist ON Album.ArtistName = Artist.ArtistName
JOIN
    Genre ON Song.SongId = Genre.SongId
GROUP BY
    Song.SongTitle,
    Artist.ArtistName,
    Album.AlbumName,
    Genre.GenreName
ORDER BY
    Song.SongTitle ASC;