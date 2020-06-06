from fastapi import FastAPI
import uvicorn
from .song import Song
from .artist import Artist
from .genre import Genre


# init
app = FastAPI(debug=True)

song = Song()
artist = Artist()
genre = Genre()

# Route
@app.get("/")
def say_hello():
    return {"Welcome":"Spotify Aggergation"}

@app.get("/songs/artist/{artist}")
def get_songs_by_artist(artist:str, page:int=0, size:int=1):
    return song.songs_by_artist(artist)[page*size:(page+1)*size]

@app.get("/songs/year/{year}")
def get_songs_by_year(year:int, page:int=0, size:int=1):
    return song.songs_by_year(year)[page*size:(page+1)*size]

@app.get("/artists/{genre}")
def get_artist_by_genre(genre:str, page:int=0, size:int=1):
    return artist.artists_by_genre(genre)[page*size:(page+1)*size]
    
@app.get("/genres")
def get_genres( page:int=0, size:int=1):
    return genre.popular_genres()[page*size:(page+1)*size]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = "8000")