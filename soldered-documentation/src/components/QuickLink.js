// src/components/QuickLink.js
import React from 'react';
import styles from './quickLink.module.css';

const QuickLink = ({ title, description, url }) => (
  <a href={url} className={styles.quickLink} target="_blank" rel="noopener noreferrer">
    <h3 className={styles.title}>{title}</h3>
    <p className={styles.description}>{description}</p>
  </a>
);

export default QuickLink;
