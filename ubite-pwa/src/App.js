import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Login from './frontend/Login'; // Adjust the path as necessary
import ForgotPassword from './frontend/ForgotPassword'; // Import your Forgot Password component
import Register from './frontend/Register'; // Import your Register component
//import HomePage from 
const App = () => {
    return (
        <Routes> {/* Wrap your Route components in Routes */}
            <Route path="/" element={<Login />} />
            <Route path="/forgot-password" element={<ForgotPassword />} />
            <Route path="/register" element={<Register />} />
             {/* Add other routes as needed */}
        </Routes>
    );
};

export default App;
