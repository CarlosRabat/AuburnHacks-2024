from user import get_access_token, get_user


# Get all the track ids from a given playlist
def get_track_ids_from_playlist(playlist_id):
    token = get_access_token()
    sp = get_user()
    id = []
    play_list = sp.user_playlist(token, playlist_id)
    for item in play_list["tracks"]["items"]:
        track = item["track"]
        id.append(track["id"])
    return id
