import React from 'react';
import PropTypes from 'prop-types';
import styles from './InkplateTile.module.css';
import Link from '@docusaurus/Link';
import IdealImage from '@theme/IdealImage'; // Import IdealImage

function InkplateTile({title, picture, links}) {
  // Construct the image resource path for IdealImage
  // The 'picture' prop should be the path relative to the 'static' directory
  // e.g., if your image is in 'static/img/my-image.jpg', 'picture' should be '/img/my-image.jpg'
  const imageSrc = picture ? require(`@site/static${picture}`) : null;

  return (
    <div className={styles.inkplateTileCard}>
      {title && <h2 className={styles.cardTitle}>{title}</h2>}
      {imageSrc && ( // Check if imageSrc is valid
        <div className={styles.cardImageContainer}>
          <IdealImage
            img={imageSrc} // Use the processed imageSrc
            alt={title || 'Tile Image'}
            className={styles.cardImage} // Your existing CSS class for styling the image area
          />
        </div>
      )}
      {links && links.length > 0 && (
        <ul className={styles.cardLinks}>
          {links.map((link, idx) => (
            <li key={idx} className={styles.cardLinkItem}>
              <Link to={link.url} className={styles.cardLink}>
                {link.title}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

InkplateTile.propTypes = {
  title: PropTypes.string,
  picture: PropTypes.string, // Should be a path like '/img/your-image.jpg'
  links: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      url: PropTypes.string.isRequired,
    })
  ),
};

export default InkplateTile;