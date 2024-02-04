import React from 'react';
import '../HomePage.css';
import { useState } from 'react';

function SubmitButton() {
    const [answer, setAnswer] = useState('');
    const [error, setError] = useState(null);
    const [status, setStatus] = useState('typing');
    
    if (status === 'success') {
        return <h1>That's right!</h1>
    }
    
    async function handleSubmit(e) {
        e.preventDefault();
        setStatus('submitting');
        try {
        await submitForm(answer);
        setStatus('success');
        } 
        catch (err) {
            setStatus('typing');
            setError(err);
        }
    }
    
    function handleTextareaChange(e) {
        setAnswer(e.target.value);
    }
    
    return (
        <>
        <form onSubmit={handleSubmit}>
            <input
            value={answer}
            onChange={handleTextareaChange}
            disabled={status === 'submitting'}
            />
            <br />
            <button disabled={
            answer.length === 0 ||
            status === 'submitting'
            }>
            Submit
            </button>
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