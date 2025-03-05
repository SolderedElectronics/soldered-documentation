import React from 'react';
import styles from './AsSeenOn.module.css';

const logos = [
  { src: '/img/seen_on_hackaday.png', alt: 'Hackaday', name: 'Hackaday', url: 'https://hackaday.com/blog/?s=inkplate' },
  { src: '/img/seen_on_bug.svg', alt: 'Bug.hr', name: 'Bug.hr', url: 'https://www.bug.hr/crowdfunding/nova-kampanja-za-hrvatski-proizvod-inkplate-najmanji-do-sada-30292' },
  { src: '/img/seen_on_crowdsupply.svg', alt: 'CrowdSupply', name: 'CrowdSupply', url: 'https://www.crowdsupply.com/soldered' },
];

const AsSeenOn = () => {
  return (
    <div className={styles.asSeenOn}>
      <h4 className={styles.header}>As seen on</h4>
      <div className={styles.logoRow}>
        {logos.map((logo, index) => (
          <div key={index} className={styles.logoItem}>
            <a href={logo.url} target="_blank" rel="noopener noreferrer">
              <img
                src={logo.src}
                alt={logo.alt}
                className={styles.logoIcon}
              />
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AsSeenOn;
