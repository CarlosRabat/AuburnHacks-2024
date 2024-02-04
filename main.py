from user import get_access_token, get_user
from artist import search_for_artist_id, search_related_artist
from playlist import search_for_playlist_id
from track import get_track_ids_from_playlist
from related_artist import related_artist
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/get_related_artist/{artist_name}")
def get_related_artist(artist_name: str):
    # artists = related_artist(artist_name)
    return {"related_artists": "Artist1"}


@app.get("/get_related_artist_test/{artist_name}")
def get_related_artist_test(artist_name):
    artists = related_artist(artist_name)
    return artists
