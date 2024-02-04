from user import get_access_token, get_user
from artist import search_for_artist_id, search_related_artist
from playlist import search_for_playlist_id
from track import get_track_ids_from_playlist
from related_artist import related_artist
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Main GET function to get the related artists to the webapp
@app.get("/get_related_artist/{artist_name}")
def get_related_artist_test(artist_name):
    artists = related_artist(artist_name)
    return artists
