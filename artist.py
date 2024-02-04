from requests import get
import json
from user import get_auth_header


# Input the Artists names and return the id for further processing
def search_for_artist_id(artist_name):
    # Search API Call
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header()
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    # Only get the id from the rsult
    artist_id = json_result.get("artists", {}).get("items", [{}])[0].get("id")

    return artist_id


# Search the related artists from the selected artist
def search_related_artist(artist_id, limit=5):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = get_auth_header()

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    related_artists = json_result.get("artists", [])[:limit]

    # Only Extract the name, id and images
    artist_info = [
        {
            "name": artist.get("name"),
            "id": artist.get("id"),
            "images": artist.get("images", [{}])[0].get("url"),
        }
        for artist in related_artists
    ]
    return artist_info


# id = search_for_artist_id("Taylor")
# print(search_related_artist(id))
