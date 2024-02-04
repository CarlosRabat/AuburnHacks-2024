import requests
from requests import get
import base64
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_access_token(client_id, client_secret):
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


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist_id(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    artist_id = json_result.get("artists", {}).get("items", [{}])[0].get("id")

    return artist_id


def search_for_playlist_id(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    playlist_id = json_result.get("playlists", {}).get("items", [{}])[0].get("id")

    return playlist_id


def search_related_artist(token, artist_id, limit=5):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    related_artists = json_result.get("artists", [])[:limit]
    artist_names = [artist.get("name") for artist in related_artists]
    return artist_names


def get_track_ids_from_playlist(sp, token, playlist_id):
    id = []
    play_list = sp.user_playlist(token, playlist_id)
    for item in play_list["tracks"]["items"]:
        track = item["track"]
        id.append(track["id"])
    return id


def get_user(client_id, client_secret):
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def getTrackFeatures (sp, id):
    meta = sp.track(id)
    features =sp.audio_features(id)

    #print(meta)

    #meta data
    name =meta['name']    
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']   
    release_date = meta['album']['release_date'] 
    length = meta['duration_ms']
    popularity = meta['popularity'] 


    #features from the dat

    acousticness = features[0]['acousticness'] 
    danceability = features[0]['danceability']   
    energy = features[0]['energy'] 
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]["liveness"]
    loudness = features[0]['loudness']
    
    
    track = [name, album, artist,release_date,length, popularity, acousticness, danceability, energy,instrumentalness, liveness,loudness]
    return track



def main():
    # Replace these with your own values
    client_id = "fcf64bb0ff3d47298a54df28088d4f75"
    client_secret = "bab82d0743d74edcb3f18d24fc5953d3"

    access_token = get_access_token(client_id, client_secret)

    # artist_id = search_for_artist_id(access_token, "ACDC")
    # related_artist = search_related_artist(access_token, artist_id)
    sp = get_user(client_id, client_secret)

    playlist_id = search_for_playlist_id(access_token, "Top Global")
    ids = get_track_ids_from_playlist(sp, access_token, playlist_id)

    #print(ids[0])

    #dat = getTrackFeatures(sp,ids[0])
    #print(dat)

   



if __name__ == "__main__":
    main()
