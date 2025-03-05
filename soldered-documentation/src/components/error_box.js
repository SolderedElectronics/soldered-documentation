import React from 'react';
import styles from './error_box.module.css';

const ErrorBox = ({ children }) => (
  <div className={styles.errorBox}>
    <span className={styles.icon}>❌</span>
    <div>{children}</div>
  </div>
);

export default ErrorBox;