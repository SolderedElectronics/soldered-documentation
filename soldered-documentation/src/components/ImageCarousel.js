import React, { useState } from 'react';
import IdealImage from '@theme/IdealImage';
import styles from './imageCarousel.module.css';

const ImageCarousel = ({ images, width = '100%' }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const totalImages = images.length;

  const goToPrevious = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + totalImages) % totalImages);
  };

  const goToNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % totalImages);
  };

  const currentImage = images[currentIndex];

  return (
    <div className={styles.carouselContainer} style={{ width }}>
      <div className={styles.imageContainer}>
        <IdealImage
          img={require(`@site/static${currentImage.src}`)}
          alt={currentImage.alt}
          className={styles.image}
          style={{ width: '100%' }}
        />
        {currentImage.caption && (
          <div className={styles.caption}>{currentImage.caption}</div>
        )}
      </div>
      <button
        className={styles.arrowLeft}
        onClick={goToPrevious}
        aria-label="Previous image"
      >
        &#9664;
      </button>
      <button
        className={styles.arrowRight}
        onClick={goToNext}
        aria-label="Next image"
      >
        &#9654;
      </button>
    </div>
  );
};

export default ImageCarousel;
