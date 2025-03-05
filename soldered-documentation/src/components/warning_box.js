// src/components/InfoBox.js
import React from 'react';
import styles from './warning_box.module.css';

const WarningBox = ({ children }) => (
  <div className={styles.warningBox}>
    <span className={styles.icon}>⚠️</span>
    <div>{children}</div>
  </div>
);

export default WarningBox;
