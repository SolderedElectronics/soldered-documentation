import React from 'react';
import styles from './successbox.module.css';

const SuccessBox = ({ children }) => (
  <div className={styles.successbox}>
    <span className={styles.icon}>✅</span>
    <div>{children}</div>
  </div>
);

export default SuccessBox;
