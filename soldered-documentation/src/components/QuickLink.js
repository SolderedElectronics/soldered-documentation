// src/components/QuickLink.js
import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './quickLink.module.css';

const QuickLink = ({ title, description, url, image }) => {
  // Process URLs with useBaseUrl
  const processedUrl = url.startsWith('http') || url.startsWith('#') ? url : useBaseUrl(url);
  const processedImage = image && !image.startsWith('http') ? useBaseUrl(image) : image;

  return (
    <a href={processedUrl} className={styles.quickLink} target="_blank" rel="noopener noreferrer">
      {image && (
        <div className={styles.imageContainer}>
          <img src={processedImage} alt={title} className={styles.image} />
        </div>
      )}
      <div className={image ? styles.contentWithImage : styles.content}>
        <h3 className={styles.title}>{title}</h3>
        <p className={styles.description}>{description}</p>
      </div>
    </a>
  );
};

export default QuickLink;