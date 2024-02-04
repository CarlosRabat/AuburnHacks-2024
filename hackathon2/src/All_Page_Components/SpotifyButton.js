import '../HomePage.css';
import React from 'react';

function SpotifyButton() {
    return (
        <a href="https://www.spotify.com" target="_blank" rel="noopener noreferrer">
          <button className="Spotify-link">
            Go to Spotify   
          </button>
        </a>
    )
}
export default SpotifyButton;