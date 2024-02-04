from artist import search_for_artist_id, search_related_artist

# Function to get recommended Artists based on the Artists that user prompts


# Get a list with all the related artists
# Get the name of the artist and the id
def related_artist(artist_name):
    artist_id = search_for_artist_id(artist_name)
    related_artists = search_related_artist(artist_id)
    artist_names = [artist["name"] for artist in related_artists]
    return artist_names
