import React, { useState } from 'react';
import { Link } from "react-router-dom"; // Import Link from react-router-dom
import './Login.css'; // Ensure this path is correct

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        if (username === 'admin' && password === 'password') {
            alert('Login successful!');
            setError('');
        } else {
            setError('Invalid username or password.');
        }
    };

    return (
        <div className="login-container">
            <img src={`${process.env.PUBLIC_URL}/placeholder.png`} alt="Logo" className="logo" />
            <form onSubmit={handleSubmit}>
                <div className="input-group">
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className="input-group">
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Login</button>
                {error && <p className="error">{error}</p>}
            </form>
            <div className="links">
                <Link to="/forgot-password" className="link">Forgot Password?</Link>
                <Link to="/register" className="link">Register</Link>
            </div>
        </div>
    );
};

export default Login;
