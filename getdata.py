from mainAPI import get_access_token, get_user, search_for_artist_id,get_track_ids_from_playlist, search_for_playlist_id, getTrackFeatures
import pandas as pd 
import time



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
    #print(len(ids))

    #dat = getTrackFeatures(sp,ids[0])
    #print(dat)

    tracks = []
    for i in range(5):
        time.sleep(5)
        track = getTrackFeatures(sp,ids[i])
        tracks.append(track)
        print('done with ', i)

    df = pd.DataFrame(tracks, columns= ['name', 'album', 'artist','release_date','length', 'popularity', 'acousticness', 'danceability', 'energy','instrumentalness', 'liveness','loudness'])
    df.to_csv('spotify.csv')



if __name__ == "__main__":
    main()