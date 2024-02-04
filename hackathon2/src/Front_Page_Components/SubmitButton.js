import React from 'react';
import '../HomePage.css';
import { useState } from 'react';

function SubmitButton() {
    const [answer, setAnswer] = useState('');
    const [error, setError] = useState(null);
    const [status, setStatus] = useState('typing');
    const [responseData, setResponseData] = useState(null)
    const [artistName, setArtistName] = useState('')
    
    if (status === 'success') {
        return <h1>That's right!</h1>
    }
    
    async function handleSubmit(e) {
        e.preventDefault();
        setStatus('submitting');
        
        try {
            const response = await fetch(`http://127.0.0.1:8000/get_related_artist/${encodeURIComponent(artistName)}`, {
                method: 'GET', // or 'GET', 'PUT', 'DELETE', etc.
                headers: {
                    'Content-Type': 'application/json'
                },
                //body: JSON.stringify({ answer }) // your data to send to the server
            });
            if (!response.ok) {
                throw new Error('Failed to submit form');
            }
            const responseData = await response.json();
            setResponseData(responseData)
            //await submitForm(answer);
            //setStatus('success');
        } catch (err) {
            setStatus('typing');
            setError(err);
        }
    }

    const handleChange = (e) => {
        setArtistName(e.target.value); // Update artistName state with input value
        setAnswer(e.target.value);
    };
    
    
    return (
        <>
        <form onSubmit={handleSubmit}>
            <input
            type="text"
            value={artistName}
            onChange={handleChange}
            placeholder="Enter artist name"
            />
            <br />
            <button disabled={
            answer.length === 0 ||
            status === 'submitting'
            }>
            Submit
            </button>
            {responseData && (
                <div>
                    <h2>Response Data:</h2>
                    <pre>{JSON.stringify(responseData, null, 2)}</pre>
                </div>
            )}
            {error !== null &&
            <p className="Error">
                {error.message}
            </p>
            }
        </form>
        </>
    );
    }
    
function submitForm(answer) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
        let shouldError = answer.toLowerCase() !== 'lima'
        if (shouldError) {
            reject(new Error('Not a valid Artist name!'));
        } else {
            resolve();
        }
        }, 1500);
    });
}

export default SubmitButton;