import React, { useEffect, useRef, useState } from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './FlickityCarousel.module.css';
import 'flickity/css/flickity.css';

const FlickityCarouselInner = ({ images, options = { wrapAround: true }, jumpers = false }) => {
  const carouselRef = useRef(null);
  const flickityInstance = useRef(null);
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const Flickity = require('flickity');
      const imagesLoaded = require('imagesloaded');

      if (carouselRef.current && !flickityInstance.current) {
        imagesLoaded(carouselRef.current, function() {
          console.log('Images loaded, initializing Flickity');
          flickityInstance.current = new Flickity(carouselRef.current, {
            wrapAround: true,
            adaptiveHeight: true,
            ...options
          });
          setIsLoaded(true);
        });
      }
    }

    return () => {
      if (flickityInstance.current) {
        flickityInstance.current.destroy();
        flickityInstance.current = null;
      }
    };
  }, [options]);

  return (
    <div className={styles.carouselContainer}>
      <div
        className={`${styles.carousel} ${jumpers ? styles.jumpersBackground : ''}`}
        ref={carouselRef}
      >
        {images && images.map((image, index) => (
          <div key={index} className={styles.carouselCell}>
            <div className={styles.imageWrapper}>
              <img 
                src={useBaseUrl(image.src)} 
                alt={image.alt || 'Carousel image'} 
                className={styles.image} 
                onLoad={() => console.log(`Image ${index} loaded:`, image.src)}
                onError={() => console.error(`Failed to load image ${index}:`, image.src)}
              />
            </div>
            {image.caption && <div className={styles.caption}>{image.caption}</div>}
          </div>
        ))}
      </div>
      {!isLoaded && (
        <div className={styles.loadingIndicator}>Loading carousel...</div>
      )}
    </div>
  );
};

const FlickityCarousel = (props) => (
  <BrowserOnly fallback={<div>Loading carousel...</div>}>
    {() => <FlickityCarouselInner {...props} />}
  </BrowserOnly>
);

export default FlickityCarousel;