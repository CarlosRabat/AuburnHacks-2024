from user import get_access_token, get_user
from artist import search_for_artist_id, search_related_artist
from playlist import search_for_playlist_id
from track import get_track_ids_from_playlist
from track_features import getTrackFeatures

# from related_artist

access_token = get_access_token()


artist_id = search_for_artist_id("ACDC")
related_artist = search_related_artist(artist_id)
sp = get_user()

playlist_id = search_for_playlist_id("Top Global")
ids = get_track_ids_from_playlist(playlist_id)

print(related_artist)

def get_playlist_data(ids):

    tracks = []
    for i in range(2):
        time.sleep(5)
        track = getTrackFeatures(ids[i])
        tracks.append(track)
        print('done with ', i)

    df = pd.DataFrame(tracks, columns= ['name', 'album', 'artist','release_date','length', 'popularity', 'acousticness', 'danceability', 'energy','instrumentalness', 'liveness','loudness'])
    #df.to_csv('spotify.csv')
    print(df.head())
    return df



if __name__ == "__main__":
    main()