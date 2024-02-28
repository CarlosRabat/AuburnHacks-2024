import requests
from requests import get
import base64
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import dotenv
import os


# returns client id and client secret
def load_client_info():
    dotenv.load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    return client_id, client_secret


# Grants Access to the spotify API
def get_access_token():
    client_id, client_secret = load_client_info()
    token_url = "https://accounts.spotify.com/api/token"
    auth_headers = f"{client_id}:{client_secret}"
    encoded_auth_headers = base64.b64encode(auth_headers.encode()).decode()

    auth_payload = {
        "grant_type": "client_credentials",
    }

    headers = {"Authorization": f"Basic {encoded_auth_headers}"}

    response = requests.post(token_url, data=auth_payload, headers=headers)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(
            f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}"
        )
        return None


# Header for APIs Querys
def get_auth_header():
    token = get_access_token()
    return {"Authorization": "Bearer " + token}


# get the user for spotipy library
def get_user():
    client_id, client_secret = load_client_info()
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp
