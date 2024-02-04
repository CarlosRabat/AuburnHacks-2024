from user import get_access_token, get_user

def getTrackFeatures (id):
    token = get_access_token()
    sp = get_user()
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