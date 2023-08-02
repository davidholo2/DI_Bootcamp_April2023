import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import WeatherCard from './WeatherCard';
import './WeatherPage.css';

const WeatherPage = () => {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState(null);

  const apiKey = 'c8be34a06ab70b022dbc602d21c40efa';

  const fetchWeatherData = async () => {
    try {
      const response = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
      );
      const data = await response.json();
      setWeatherData(data);
    } catch (error) {
      console.error('Error fetching weather data:', error);
    }
  };

  return (
    <div>
      <h2>Weather Page</h2>
      <TextField
        label="Enter City"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <Button variant="contained" onClick={fetchWeatherData}>
        Get Weather
      </Button>
      {weatherData && <WeatherCard weather={weatherData} />}
    </div>
  );
};

export default WeatherPage;
