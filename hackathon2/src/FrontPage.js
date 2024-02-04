import './HomePage.css';
import ArtistNameTextBox from './Front_Page_Components/ArtistName.js';
import DevInfo from './All_Page_Components/DevInfo.js';
import SpotifyButton from './All_Page_Components/SpotifyButton.js';
import Description from './Front_Page_Components/Description.js'; 
import SubmitButton from './Front_Page_Components/SubmitButton.js';
//import BottomButton from './Front_Page_Components/bottomButton.js';

//This is the home page of the project.
function FrontPage() {
  return (
    <div className="App">
      <img className="Spotify-logo" src={require('./SpotifyLogo.png')} alt="logo"/>
      <header className="App-header">
        <p>
          Spotify API WebApp.
        </p>
        <SpotifyButton /> {/* This is the Spotify Button in the top right corner */}
        <DevInfo /> {/*This is the paragraph bottom left */}
        {/* Need to integrate this below with back end */}
        <Description />
        <ArtistNameTextBox />  {/*This is the text next to the text box and submit button */}
        <SubmitButton /> {/* This is the submit button and text box */}
        {/* <BottomButton /> */}
      </header>
    </div>
  );
}
export default FrontPage;
