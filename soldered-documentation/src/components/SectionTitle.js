// src/components/SectionTitle.js
import React from 'react';
import styles from './sectionTitle.module.css';

const SectionTitle = ({ title, backgroundImage, height }) => (
  <>
    <div
      className={styles.sectionTitle}
      style={{
        // Omit the variable entirely when there's no image, so the ::before
        // overlay doesn't request url(undefined)
        ...(backgroundImage && { '--background-image': `url(${backgroundImage})` }),
        height: height || undefined, // Use the provided height or let CSS handle it
      }}
    >
      <h1 className={styles.title}>
        <span className={styles.indent}></span>
        {title}
      </h1>
    </div>
  </>
);

export default SectionTitle;