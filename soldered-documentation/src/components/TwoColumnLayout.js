import React from 'react';
import styles from './TwoColumnLayout.module.css';

const TwoColumnLayout = ({ children }) => {
  const columns = React.Children.toArray(children);

  return (
    <div className={styles.twoColumnLayout}>
      <div className={styles.column}>{columns[0]}</div>
      <div className={styles.column}>{columns[1]}</div>
    </div>
  );
};

export default TwoColumnLayout;
