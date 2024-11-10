import React from 'react';

const Header = ({ username = "User" }) => {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between">
          {/* Logo Space */}
          <div className="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center">
            {/* Replace with your actual logo */}
            <span className="text-gray-500 font-bold">CT</span>
          </div>

          {/* Welcome Message */}
          <div className="text-center flex-1 mx-4">
            <h1 className="text-2xl font-bold text-gray-900">
              Welcome to Calorie Tracker!
            </h1>
          </div>

          {/* User Section */}
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
              <span className="text-white font-medium">
                {username.charAt(0).toUpperCase()}
              </span>
            </div>
            <span className="text-gray-700 font-medium">
              {username}
            </span>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;