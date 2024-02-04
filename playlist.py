from requests import get
import json
from user import get_auth_header


def search_for_playlist_id(playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header()
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    playlist_id = json_result.get("playlists", {}).get("items", [{}])[0].get("id")

    return playlist_id
