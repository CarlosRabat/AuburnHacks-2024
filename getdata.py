from mainAPI import get_access_token, get_user, search_for_artist_id, search_for_playlist_id, getTrackFeatures
import pandas as pd 
import time
from track import get_track_ids_from_playlist
from user import get_access_token, get_user


def main():
    # Replace these with your own values

    client_id = "fcf64bb0ff3d47298a54df28088d4f75"
    client_secret = "bab82d0743d74edcb3f18d24fc5953d3"
    print('success')
    access_token = get_access_token(client_id, client_secret)
    print('success')
    # artist_id = search_for_artist_id(access_token, "ACDC")
    # related_artist = search_related_artist(access_token, artist_id)
    sp = get_user(client_id, client_secret)
    print('success')
    playlist_id = search_for_playlist_id(access_token, "Top Global")
    print('success')
    ids = get_track_ids_from_playlist(playlist_id)
    print('success')
    #print(ids[0])
    #print(len(ids))

    #dat = getTrackFeatures(sp,ids[0])
    #print(dat)

    tracks = []
    for i in range(2):
        time.sleep(5)
        track = getTrackFeatures(sp,ids[i])
        tracks.append(track)
        print('done with ', i)

    df = pd.DataFrame(tracks, columns= ['name', 'album', 'artist','release_date','length', 'popularity', 'acousticness', 'danceability', 'energy','instrumentalness', 'liveness','loudness'])
    df.to_csv('spotify.csv')



if __name__ == "__main__":
    main()