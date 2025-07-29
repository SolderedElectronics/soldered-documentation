import React from 'react';
import IdealImage from '@theme/IdealImage';
import styles from './centeredImage.module.css';

const CenteredImage = ({ src, alt, caption, width = '100%', attribution_name, attribution_link }) => (
  <div className={styles.container}>
    <IdealImage
      img={require(`@site/static${src}`)}
      alt={alt}
      className={styles.image}
      style={{ width: width, maxWidth: '100%' }} // Never overflow parent
    />
    {caption && <div className={styles.caption}>{caption}</div>}
    {attribution_name && attribution_link && (
      <div className={styles.attribution}>
        Image credit: <a href={attribution_link} target="_blank" rel="noopener noreferrer">{attribution_name}</a>
      </div>
    )}
  </div>
);

export default CenteredImage;
