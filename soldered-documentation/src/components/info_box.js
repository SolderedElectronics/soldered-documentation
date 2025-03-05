// src/components/InfoBox.js
import React from 'react';
import styles from './info_box.module.css';

const InfoBox = ({ children }) => (
  <div className={styles.infoBox}>
    <span className={styles.icon}>ℹ️</span>
    <div>{children}</div>
  </div>
);

export default InfoBox;
