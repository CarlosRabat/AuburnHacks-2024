import React from 'react';
import { Link } from 'react-router-dom';

function BottomButton() {
  return (
    <div className="bottom-button">
      <Link to="/second-page">
        <button>Go to Second Page</button>
      </Link>
    </div>
  );
}

export default BottomButton;