from user import get_access_token, get_user
from artist import search_for_artist_id, search_related_artist
from playlist import search_for_playlist_id
from track import get_track_ids_from_playlist
from related_artist import related_artist
from track_features import getTrackFeatures

# from related_artist
access_token = get_access_token()


artist_id = search_for_artist_id("ACDC")
related_artist = search_related_artist(artist_id)
sp = get_user()

playlist_id = search_for_playlist_id("Top Global")
ids = get_track_ids_from_playlist(playlist_id)

feat = getTrackFeatures(ids[0])

#print(related_artist)
print(feat)
