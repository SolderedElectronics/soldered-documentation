import React from 'react';
import styles from './TwoColumnLayoutBackground.module.css';

const TwoColumnLayoutBackground = ({ children }) => {
  const columns = React.Children.toArray(children);

  return (
    <div className={styles.twoColumnLayoutBackground}>
      <div className={styles.column}>{columns[0]}</div>
      <div className={styles.column}>{columns[1]}</div>
    </div>
  );
};

export default TwoColumnLayoutBackground;
