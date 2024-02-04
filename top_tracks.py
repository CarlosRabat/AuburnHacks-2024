from artist import search_for_artist_id
from requests import get
import json
from user import get_auth_header


def get_artist_top_tracks(artist_id, market='US'):
    # API Endpoint
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"

    # Headers with authentication
    headers = get_auth_header()

    # Parameters
    params = {'market': market}

    # Making the API call
    result = get(url, headers=headers, params=params)
    json_result = result.json()

    # Extracting relevant information
    top_tracks = json_result.get('tracks', [])

    # Returning the list of top tracks
    return top_tracks

# Example usage:
# artist_id = "0TnOYISbd1XYRBk9myaseg"  # Replace with the actual artist ID
# top_tracks = get_artist_top_tracks(artist_id)
# print(top_tracks)

artist_id = search_for_artist_id('taylor swift')
output = get_artist_top_tracks(artist_id)
#print(top_tracks)


top_tracks = []
for track_info in output:
    track_name = track_info['name']
    track_popularity = track_info['popularity']
    artists = [artist['name'] for artist in track_info['artists']]
    
    top_tracks.append({
        'name': track_name,
        'popularity': track_popularity,
        'artists': artists
    })

# Sort tracks by popularity in descending order
top_tracks.sort(key=lambda x: x['popularity'], reverse=True)

# Display top tracks
for i, track in enumerate(top_tracks, start=1):
    print(f"{i}. {track['name']} by {', '.join(track['artists'])} - Popularity: {track['popularity']}")

