import React, { useState } from 'react';
import './ForgotPassword.css'; 

const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        if (email) {
            setMessage(`A reset link has been sent to ${email}`);
            setEmail('');
        } else {
            setMessage('Please enter a valid email address.');
        }
    };

    return (
        <div className="reset-password-container">
            <h2>Reset Password</h2>
            <form onSubmit={handleSubmit}>
                <div className="input-group">
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Send Reset Link</button>
                {message && <p className="message">{message}</p>}
            </form>
        </div>
    );
};

export default ForgotPassword;
