import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import './WeatherCard.css'; // Import the CSS file

const WeatherCard = ({ weather }) => {
  if (!weather || !weather.name || !weather.sys || !weather.sys.country) {
    return null; // Return null if required data is missing
  }

  return (
    <Card className="card">
      <CardContent className="card-content">
        <Typography variant="h5" gutterBottom>
          Weather in {weather.name}, {weather.sys.country}
        </Typography>
        <Typography variant="subtitle1">
          Temperature: {weather.main.temp}°C
        </Typography>
        <Typography variant="subtitle1">
          Weather: {weather.weather[0].description}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default WeatherCard;
