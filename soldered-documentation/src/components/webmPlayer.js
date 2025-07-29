import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl'; // Import useBaseUrl
import styles from './WebmPlayer.module.css';

function WebmPlayer({ src, width }) {
  // Use useBaseUrl to ensure the path is correct regardless of siteBaseUrl
  const videoSrc = useBaseUrl(src);

  const videoStyle = {
    width: width ? `${width}px` : '100%', // Apply width if provided, otherwise 100%
    height: 'auto', // Maintain aspect ratio
  };

  return (
    <div className={styles.webmPlayerContainer}>
      <video controls autoPlay loop muted style={videoStyle}>
        {/* Use the resolved videoSrc here */}
        <source src={videoSrc} type="video/webm" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
}

export default WebmPlayer;