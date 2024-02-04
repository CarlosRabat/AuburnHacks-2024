import streamlit as st
import pandas as pd
import plotly.express as px
#import seaborn as sns
from user import get_access_token, get_user
from artist import search_for_artist_id, search_related_artist
from playlist import search_for_playlist_id
from track import get_track_ids_from_playlist
from related_artist import related_artist
from track_features import getTrackFeatures
from getdata import get_data

# from related_artist
access_token = get_access_token()


# artist_id = search_for_artist_id("ACDC")
# related_artist = search_related_artist(artist_id)
sp = get_user()

# playlist_id = search_for_playlist_id("Top Global")
# ids = get_track_ids_from_playlist(playlist_id)

# feat = getTrackFeatures(ids[0])
# df = get_data(ids)

# Function to perform manipulation and create dataframe
# def analyze_playlist(playlist_name):
#     # This is a dummy function, replace it with your own logic to fetch playlist data
#     # For simplicity, let's assume we have a predefined playlist data
#     playlist_data = [
#         {'name': 'Song 1', 'album': 'Album 1', 'artist': 'Artist 1', 'release_date': '2022-01-01', 'length': 180, 'popularity': 80},
#         {'name': 'Song 2', 'album': 'Album 2', 'artist': 'Artist 2', 'release_date': '2022-02-01', 'length': 200, 'popularity': 90},
#         {'name': 'Song 3', 'album': 'Album 3', 'artist': 'Artist 1', 'release_date': '2022-03-01', 'length': 160, 'popularity': 85},
#         {'name': 'Song 4', 'album': 'Album 1', 'artist': 'Artist 3', 'release_date': '2022-04-01', 'length': 220, 'popularity': 75},
#         {'name': 'Song 5', 'album': 'Album 4', 'artist': 'Artist 2', 'release_date': '2022-05-01', 'length': 190, 'popularity': 88}
#     ]

#     df = pd.DataFrame(playlist_data)
#     return df

# Function to display barchart
def display_top_artists_chart(df):
    st.subheader("Top 5 Artists Based on Popularity")

    # Group by artist and calculate average popularity
    artist_popularity = df.groupby('artist')['popularity'].mean().sort_values(ascending=False).head(5).reset_index()

    # Create barchart using Plotly
    fig = px.bar(artist_popularity, x='artist', y='popularity', text='popularity',
                 labels={'popularity': 'Average Popularity'},
                 title='Top 5 Artists Based on Popularity',
                 hover_data=['artist', 'popularity'])

    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    st.plotly_chart(fig)

# Function to display artist with the latest album
def display_latest_album_card(df):
    st.subheader("Artist with the Latest Album")

    latest_album = df.sort_values('release_date', ascending=False).iloc[0]

    st.markdown(f"**Artist:** {latest_album['artist']}")
    st.markdown(f"**Album:** {latest_album['album']}")
    st.markdown(f"**Release Date:** {latest_album['release_date']}")

# Function to display longest and shortest albums
def display_album_duration_cards(df):
    st.subheader("Albums Duration Analysis")

    longest_album = df.loc[df['length'].idxmax()]
    shortest_album = df.loc[df['length'].idxmin()]

    st.markdown(f"**Longest Album:** {longest_album['album']} by {longest_album['artist']} ({longest_album['length']} seconds)")
    st.markdown(f"**Shortest Album:** {shortest_album['album']} by {shortest_album['artist']} ({shortest_album['length']} seconds)")

def main():
    st.title("Spotify Playlist Analysis")

    # Get user input
    playlist_name = st.text_input("Enter the name of the playlist:")

    playlist_id = search_for_playlist_id(playlist_name)
    ids = get_track_ids_from_playlist(playlist_id)

    #feat = getTrackFeatures(ids[0])
    #df = get_data(ids)

    if st.button("Analyze Playlist"):
        # Call the predefined function to get the DataFrame
        playlist_df = get_data(ids)# analyze_playlist(playlist_name)

        # Display insights
        display_top_artists_chart(playlist_df)
        display_latest_album_card(playlist_df)
        display_album_duration_cards(playlist_df)

if __name__ == "__main__":
    main()
