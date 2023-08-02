import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';

const ImageCarousel = () => {
  return (
    <Carousel showArrows={true}>
      <div>
        <img
          src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg"
          alt="Hong Kong"
          style={{ maxWidth: '1500px', maxHeight: '1500px' }}
        />
        <p className="legend">Hong Kong</p>
      </div>
      <div>
        <img
          src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp"
          alt="Macao"
          style={{ maxWidth: '1500px', maxHeight: '1500px' }}
        />
        <p className="legend">Macao</p>
      </div>
      <div>
        <img
          src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp"
          alt="Japan"
          style={{ maxWidth: '1500px', maxHeight: '1500px' }}
        />
        <p className="legend">Japan</p>
      </div>
      <div>
        <img
          src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp"
          alt="Las Vegas"
          style={{ maxWidth: '1500px', maxHeight: '1500px' }}
        />
        <p className="legend">Las Vegas</p>
      </div>
    </Carousel>
  );
};

export default ImageCarousel;
