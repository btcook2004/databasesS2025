from flask import Flask, redirect, render_template, request
import CRUD.CRUD_Song as CRUD_Song
import CRUD.CRUD_Album as CRUD_Album
import CRUD.CRUD_Artist as CRUD_Artist
import CRUD.CRUD_Genre as CRUD_Genre
import CRUD.CRUD_Index as CRUD_Index
import app.clearTables as CT
import CRUD.recommendation as recom
app = Flask(__name__)
searchResults = []
recommendationResults = []


@app.route('/')
def index():
   # do everything needed to insert a song with album, artist, genre, etc.
   BigTable = CRUD_Index.ReadBig();
   averageSongLength = CRUD_Index.getAverageSong()
   AverageRating = CRUD_Index.getAverageRating()
   BestArtistSongs = CRUD_Index.artistWithHighestSongAverage()
   # print(AverageRating)
   return render_template('index.html', bigTable=BigTable, averageSongLength=averageSongLength, albumsWithHighestAvgRatings=AverageRating, bestArtistSongs=BestArtistSongs)

@app.route('/clearTables')
def clear():
   CT.clearTables()
   return redirect('/')

@app.route('/clearAndRemakeTables')
def clearAndRemakeTables():
   CT.clearAndRemakeTables()
   return redirect('/')



@app.route('/search', methods=['GET', 'POST'])
def search():
   if request.method == 'POST':
      song_title = request.form['songTitle']
      artist_name = request.form['artistName']
      global searchResults
      searchResults = CRUD_Index.SearchBySong(song_title, artist_name)
      return redirect('/search_results')
   return render_template('search.html')

@app.route('/search_results')
def search_results():
   return render_template('search.html', results=searchResults)


@app.route('/songs')
def songs():
   Songs = CRUD_Song.ReadSong()
   return render_template('songs.html', songs=Songs)

@app.route('/create_song', methods=['POST'])
def create_song():
   SongTitle = request.form['songTitle']
   ArtistName = request.form['artistName']
   AlbumId = request.form['albumId']
   AlbumName = request.form['albumName']
   FeaturedArtist = request.form['featuredArtist']
   Rating = request.form['rating']
   Time = request.form['time']

   CRUD_Song.CreateSong(SongTitle, ArtistName, AlbumId, AlbumName, FeaturedArtist, Rating, Time)
   return redirect('/songs')

@app.route('/update_song', methods=['POST'])
def update_song():
   SongId = request.form['songId']
   SongTitle = request.form['songTitle']
   ArtistName = request.form['artistName']
   AlbumId = request.form['albumId']
   FeaturedArtist = request.form['featuredArtist']
   Rating = request.form['rating']
   Time = request.form['time']

   CRUD_Song.UpdateSong(SongId, SongTitle, ArtistName, AlbumId, FeaturedArtist, Rating, Time)
   return redirect('/songs')

@app.route('/delete_song', methods=['POST'])
def delete_song():
   SongId = request.form['songId']
   CRUD_Song.DeleteSong(SongId)
   return redirect('/songs')


@app.route('/albums')
def albums():
   Albums = CRUD_Album.ReadAlbum()
   return render_template('albums.html', albums=Albums)

@app.route('/create_album', methods=['POST'])
def create_album():
   AlbumName = request.form['albumName']
   ArtistName = request.form['artistName']
   NumSongs = request.form['numSongs']
   Rating = request.form['rating']
   ReleaseYear = request.form['releaseYear']
   PlayTime = request.form['playTime']

   CRUD_Album.CreateAlbum(AlbumName, ArtistName, NumSongs, Rating, ReleaseYear, PlayTime)
   return redirect('/albums')

@app.route('/update_album', methods=['POST'])
def update_album():
   AlbumId = request.form['albumId']
   AlbumName = request.form['albumName']
   ArtistName = request.form['artistName']
   NumSongs = request.form['numSongs']
   Rating = request.form['rating']
   ReleaseYear = request.form['releaseYear']
   PlayTime = request.form['playTime']

   CRUD_Album.UpdateAlbum(AlbumId, AlbumName, ArtistName, NumSongs, Rating, ReleaseYear, PlayTime)
   return redirect('/albums')

@app.route('/delete_album', methods=['POST'])
def delete_album():
   AlbumId = request.form['albumId']
   CRUD_Album.DeleteAlbum(AlbumId)
   return redirect('/albums')



@app.route('/artists')
def artists():
   Artists = CRUD_Artist.ReadArtist()
   return render_template('artists.html', artists=Artists)

@app.route('/create_artist', methods=['POST'])
def create_artist():
   ArtistName = request.form['artistName']
   Rating = request.form['artistRating']
   CRUD_Artist.CreateArtist(ArtistName, Rating)
   return redirect('/artists')

@app.route('/update_artist', methods=['POST'])
def update_artist():
   ArtistName = request.form['artistName']
   Rating = request.form['artistRating']
   CRUD_Artist.UpdateArtist(ArtistName, Rating)
   return redirect('/artists')

@app.route('/delete_artist', methods=['POST'])
def delete_artist():
   ArtistName = request.form['artistName']
   CRUD_Artist.DeleteArtist(ArtistName)
   return redirect('/artists')


@app.route('/genres')
def genres():
   Genres = CRUD_Genre.ReadGenre()
   return render_template('genres.html', genres=Genres)

@app.route('/create_genre', methods=['POST'])
def create_genre():
   GenreName = request.form['genreName']
   SongId = request.form['songId']

   CRUD_Genre.CreateGenre(GenreName, SongId)
   return redirect('/genres')

@app.route('/update_genre', methods=['POST'])
def update_genre():
   GenreId = request.form['genreId']
   GenreName = request.form['genreName']
   SongId = request.form['songId']

   CRUD_Genre.UpdateGenre(GenreId, GenreName, SongId)
   return redirect('/genres')

@app.route('/delete_genre', methods=['POST'])
def delete_genre():
   GenreId = request.form['genreId']
   CRUD_Genre.DeleteGenre(GenreId)
   return redirect('/genres')

@app.route('/recommendations')
def recommendations():
   return render_template('recommendations.html', recommendations = recommendationResults)


@app.route('/recommendations', methods=['POST'])
def recommendations_post():
   # Placeholder for recommendations logic
   seconds = request.form['songId1']
   global recommendationResults
   recommendationResults, totalTime = recom.getRecommendations(seconds)
   # print(recommendationResults)
   return render_template('recommendations.html', recommendations=recommendationResults, totalTime=totalTime)

