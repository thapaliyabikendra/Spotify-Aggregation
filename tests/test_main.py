from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

artist_eminem = [
  {
    "Unnamed: 0": 166329,
    "acousticness": 0.000644,
    "artists": [
      "Eminem"
    ],
    "danceability": 0.592,
    "duration_ms": 247760,
    "energy": 0.901,
    "explicit": 1,
    "id": "1RBvhBNdJcnrHMF3Lj0sHj",
    "instrumentalness": 0,
    "key": 4,
    "liveness": 0.369,
    "loudness": -3.868,
    "mode": 0,
    "name": "Just Don't Give A Fuck",
    "popularity": 33,
    "release_date": "1998-01-01",
    "speechiness": 0.253,
    "tempo": 85.361,
    "valence": 0.7
  }
]

year_2020 = [
  {
    "Unnamed: 0": 107096,
    "acousticness": 0.0387,
    "artists": [
      "Reik"
    ],
    "danceability": 0.506,
    "duration_ms": 201280,
    "energy": 0.645,
    "explicit": 0,
    "id": "05pXSD1OXWGjPHHU0Pywz7",
    "instrumentalness": 0.0000011,
    "key": 5,
    "liveness": 0.173,
    "loudness": -5.082,
    "mode": 1,
    "name": "Voy a Estar",
    "popularity": 0,
    "release_date": "2020-05-15",
    "speechiness": 0.0332,
    "tempo": 175.854,
    "valence": 0.419
  }
]

genre_rap = [
  {
    "Unnamed: 0": 799,
    "artists": "Noël-Noël",
    "acousticness": 0.951,
    "danceability": 0.712,
    "duration_ms": 188825,
    "energy": 0.184,
    "instrumentalness": 0,
    "liveness": 0.102,
    "loudness": -16.434,
    "speechiness": 0.468,
    "tempo": 114.187,
    "valence": 0.691,
    "popularity": 0,
    "key": 11,
    "mode": 0,
    "count": 1,
    "genres": [
      "country rap",
      "redneck"
    ]
  }
]

def test_say_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome":"Spotify Aggergation"}

def test_get_songs_by_artist():
    response  = client.get("/artist/Eminem")
    assert response.status_code == 200
    assert response.json() == artist_eminem

def test_get_songs_by_year():
    response  = client.get("/year/2020")
    assert response.status_code == 200
    assert response.json() == year_2020


def test_get_artist_by_genre():
    response  = client.get("/genre/rap")
    assert response.status_code == 200
    assert response.json() == genre_rap
