import './SecondPage.css';
import React from 'react';
import DevInfo from './All_Page_Components/DevInfo.js';
import SpotifyButton from './All_Page_Components/SpotifyButton';


function SecondPage() {
    return (
        <div className="App">
            <DevInfo />
            <SpotifyButton />
        </div>
    )
}

export default SecondPage;