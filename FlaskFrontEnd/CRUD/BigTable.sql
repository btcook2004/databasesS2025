SELECT 
    Song.SongTitle,
    Album.AlbumName,
    Artist.ArtistName,
    Song.FeaturedArtist,
    Song.Rating,
    Song.Time
FROM 
    Song
JOIN 
    Album ON Song.AlbumId = Album.AlbumId
JOIN 
    Artist ON Album.ArtistName = Artist.ArtistName;