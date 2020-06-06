from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

artist_eminem = [
  {
    "Unnamed: 0": 9887,
    "acousticness": 0.145,
    "artists": [
      "Eminem",
      "Juice WRLD"
    ],
    "danceability": 0.808,
    "duration_ms": 210800,
    "energy": 0.745,
    "explicit": 1,
    "id": "7FIWs0pqAYbP91WWM0vlTQ",
    "instrumentalness": 0,
    "key": 10,
    "liveness": 0.292,
    "loudness": -5.26,
    "mode": 0,
    "name": "Godzilla (feat. Juice WRLD)",
    "popularity": 91,
    "release_date": "2020-01-17",
    "speechiness": 0.342,
    "tempo": 165.995,
    "valence": 0.829
  }
]

year_2020 = [
  {
    "Unnamed: 0": 9875,
    "acousticness": 0.00146,
    "artists": [
      "The Weeknd"
    ],
    "danceability": 0.514,
    "duration_ms": 200040,
    "energy": 0.73,
    "explicit": 0,
    "id": "0VjIjW4GlUZAMYd2vXMi3b",
    "instrumentalness": 0.0000954,
    "key": 1,
    "liveness": 0.0897,
    "loudness": -5.934,
    "mode": 1,
    "name": "Blinding Lights",
    "popularity": 100,
    "release_date": "2020-03-20",
    "speechiness": 0.0598,
    "tempo": 171.005,
    "valence": 0.334
  }
]

genre_rap = [
  {
    "Unnamed: 0": 28,
    "artists": "Dímelo Flow",
    "acousticness": 0.2726666667,
    "danceability": 0.787,
    "duration_ms": 224591.3333333333,
    "energy": 0.657,
    "instrumentalness": 0.000215,
    "liveness": 0.0682,
    "loudness": -3.9093333333,
    "speechiness": 0.1683,
    "tempo": 147.2646666667,
    "valence": 0.5656666667,
    "popularity": 87.6666666667,
    "key": 0,
    "mode": 1,
    "count": 3,
    "genres": [
      "latin",
      "reggaeton",
      "reggaeton flow",
      "trap latino"
    ]
  }
]

genres = [
  {
    "genres": "russian dance",
    "acousticness": 0.00561,
    "danceability": 0.653,
    "duration_ms": 198095,
    "energy": 0.945,
    "instrumentalness": 0.915,
    "liveness": 0.439,
    "loudness": -2.634,
    "speechiness": 0.0959,
    "tempo": 126.091,
    "valence": 0.326,
    "popularity": 85,
    "key": 5,
    "mode": 1
  }
]

def test_say_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome":"Spotify Aggergation"}

def test_get_songs_by_artist():
    response  = client.get("/songs/artist/Eminem")
    assert response.status_code == 200
    assert response.json() == artist_eminem

def test_get_songs_by_year():
    response  = client.get("/songs/year/2020")
    assert response.status_code == 200
    assert response.json() == year_2020

def test_get_artist_by_genre():
    response  = client.get("/artists/rap")
    assert response.status_code == 200
    assert response.json() == genre_rap

def test_get_genres():
    response  = client.get("/genres")
    assert response.status_code == 200
    assert response.json() == genres

def test_get_songs_by_artist_per_size():
    response  = client.get("/songs/artist/Eminem?size=10")
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_get_songs_by_year_per_size():
    response  = client.get("/songs/year/2020?size=20")
    assert response.status_code == 200
    assert len(response.json()) == 20

def test_get_artist_by_genre_per_size():
    response  = client.get("/artists/rap?size=30")
    assert response.status_code == 200
    assert len(response.json()) == 30
