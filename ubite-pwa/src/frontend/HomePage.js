import React from 'react';
import { PlusCircle } from 'lucide-react';

const Demo = () => {
  return (
    <div className="bg-gray-100 min-h-screen">
      <Header username="John Doe" />
      <div className="max-w-md mx-auto mt-8">
        <CalorieCounter calories={1500} dailyGoal={2000} />
      </div>
    </div>
  );
};

const Header = ({ username = "User" }) => {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between">
          <div className="logo">
            <img src="/api/placeholder/40/40" alt="Logo" className="h-10" />
          </div>
          
          <div className="text-center flex-1 mx-4">
            <h1 className="text-2xl font-bold text-gray-900">
              Welcome to UBite!
            </h1>
          </div>
          
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

const CalorieCounter = ({ calories = 0, dailyGoal = 2000 }) => {
  const percentage = Math.min((calories / dailyGoal) * 100, 100);
  const radius = 80;
  const strokeWidth = 8;
  const normalizedRadius = radius - strokeWidth * 2;
  const circumference = normalizedRadius * 2 * Math.PI;
  const strokeDashoffset = circumference - (percentage / 100) * circumference;

  return (
    <div className="flex flex-col items-center justify-center p-8 bg-white rounded-lg shadow-sm">
      <div className="relative">
        <svg
          height={radius * 2}
          width={radius * 2}
          className="transform -rotate-90"
        >
          <circle
            stroke="#e5e7eb"
            fill="transparent"
            strokeWidth={strokeWidth}
            r={normalizedRadius}
            cx={radius}
            cy={radius}
          />
          <circle
            stroke="#3b82f6"
            fill="transparent"
            strokeWidth={strokeWidth}
            strokeDasharray={`${circumference} ${circumference}`}
            style={{ strokeDashoffset }}
            r={normalizedRadius}
            cx={radius}
            cy={radius}
            className="transition-all duration-500 ease-in-out"
          />
        </svg>
        
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-3xl font-bold text-gray-800">
            {calories}
          </span>
          <span className="text-sm text-gray-500">
            calories
          </span>
        </div>
      </div>
      
      <div className="mt-4 text-center w-full">
        <p className="text-sm text-gray-600">
          Daily Goal: {dailyGoal} calories
        </p>
        <p className="text-sm text-gray-600">
          {Math.round(percentage)}% consumed
        </p>
        
        <button
          type="submit"
          className="mt-4 w-full bg-blue-600 text-white p-2 rounded-md hover:bg-blue-700 flex items-center justify-center gap-2"
        >
          <PlusCircle size={20} />
          Add Entry
        </button>
      </div>
    </div>
  );
};

export default Demo;