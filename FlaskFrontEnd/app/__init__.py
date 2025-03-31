from flask import Flask, render_template
import CRUD.CRUD_Song as CRUD_Song
import CRUD.CRUD_Album as CRUD_Album
import CRUD.CRUD_Artist as CRUD_Artist
import CRUD.CRUD_Genre as CRUD_Genre
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/songs')
def songs():
   Songs = CRUD_Song.ReadSong()
   return render_template('songs.html', songs=Songs)

@app.route('/albums')
def albums():
   Albums = CRUD_Album.ReadAlbum()
   return render_template('albums.html', albums=Albums)

@app.route('/artists')
def artists():
   Artists = CRUD_Artist.ReadArtist()
   return render_template('artists.html', artists=Artists)

@app.route('/genres')
def genres():
   Genres = CRUD_Genre.ReadGenre()
   return render_template('genres.html', genres=Genres)