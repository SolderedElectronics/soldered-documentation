// src/components/SectionTitle.js
import React from 'react';
import styles from './madeBySoldered.module.css';

const MadeBySoldered = ({ backgroundImage }) => (
  <div
    className={styles.sectionTitle}
    style={{
      '--background-image': `url(${backgroundImage})`,
    }}
  >
    <p className={styles.title}>
      Inkplate is proudly designed and manufactured by
      <span className={styles.solderedElectronics}> Soldered Electronics</span>
    </p>
    <a
      href="https://soldered.com"
      target="_blank"
      rel="noopener noreferrer"
      className={styles.visitUs}
    >
      Visit us: Soldered.com
    </a>
  </div>
);

export default MadeBySoldered;
