from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/songs')
def songs():
   return render_template('songs.html')
@app.route('/albums')
def albums():
   return render_template('albums.html')
@app.route('/artists')
def artists():
   return render_template('artists.html')
@app.route('/genres')
def genres():
   return render_template('genres.html')