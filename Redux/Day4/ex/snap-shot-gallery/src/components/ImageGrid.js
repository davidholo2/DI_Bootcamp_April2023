// src/components/ImageGrid.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Image from './Image';

const ImageGrid = () => {
  const { category } = useParams();
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(`https://api.pexels.com/v1/search?query=${category}&per_page=30`, {
        headers: {
          Authorization: 'PAtQWAUOjFN1D6tgpbaOIRaRgATH1v3KDyLx0xCta3sfTg8KbTkUxnSY',
        },
      });
      setImages(response.data.photos);
    };

    fetchData();
  }, [category]);

  return (
    <div className="image-grid">
      {images.map(image => (
        <Image key={image.id} src={image.src.medium} alt={image.photographer} />
      ))}
    </div>
  );
};

export default ImageGrid;
