import React, { useEffect, useRef } from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import styles from './FlickityCarousel.module.css';
import 'flickity/css/flickity.css';

const FlickityCarouselInner = ({ images, options = { wrapAround: true }, jumpers = false }) => {
  const carouselRef = useRef(null);
  const flickityInstance = useRef(null);

  useEffect(() => {
    const Flickity = require('flickity');

    setTimeout(() => {
      const imagesLoaded = require('imagesloaded');
      imagesLoaded(carouselRef.current, { background: true }, () => {
        if (carouselRef.current && !flickityInstance.current) {
          flickityInstance.current = new Flickity(carouselRef.current, options);
        }
      });
    }, 500); // Delay by 500ms

    return () => {
      if (flickityInstance.current) {
        flickityInstance.current.destroy();
        flickityInstance.current = null;
      }
    };
  }, [options]);

  return (
    <div
      className={`${styles.carousel} ${jumpers ? styles.jumpersBackground : ''}`}
      ref={carouselRef}
    >
      {images.map((image, index) => (
        <div key={index} className={styles.carouselCell}>
          <div className={styles.imageWrapper}>
            <img src={image.src} alt={image.alt} className={styles.image} loading="eager" />
          </div>
          {image.caption && <div className={styles.caption}>{image.caption}</div>}
        </div>
      ))}
    </div>
  );
};

const FlickityCarousel = (props) => (
  <BrowserOnly fallback={<div>Loading...</div>}>
    {() => <FlickityCarouselInner {...props} />}
  </BrowserOnly>
);

export default FlickityCarousel;
