# importing the necessary packages
import spotipy 
sp = spotipy.Spotify() 
from spotipy.oauth2 import SpotifyClientCredentials 
import spotipy.util as util

# setting up authorization
cid = "fcf64bb0ff3d47298a54df28088d4f75"
secret = "bab82d0743d74edcb3f18d24fc5953d3"
# saving the info you're going to need
username = 'Justus'
scope = 'user-library-read' #check the documentation
authorization_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
redirect_uri ='https://localhost.com/callback/'

token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)