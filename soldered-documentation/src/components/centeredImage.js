import React from 'react';
import IdealImage from '@theme/IdealImage';
import styles from './centeredImage.module.css';

const CenteredImage = ({ src, alt, caption, width = '100%' }) => (
  <div className={styles.container}>
    <IdealImage img={require(`@site/static${src}`)} alt={alt} className={styles.image} style={{ width: width }} />
    {caption && <div className={styles.caption}>{caption}</div>}
  </div>
);

export default CenteredImage;
