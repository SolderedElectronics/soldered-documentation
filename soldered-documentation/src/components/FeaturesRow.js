import React from 'react';
import styles from './FeaturesRow.module.css';

const features = [
  {
    icon: '/img/icon_fast_update.png',
    title: 'Fast update',
    description:
      'Inkplate 6 MOTION has our fastest e-Paper refresh rate yet (11FPS)',
    link: '/Inkplate-6MOTION/basics/partial-update', // Update with correct URL
  },
  {
    icon: '/img/features_wifi_icon.png',
    title: 'WiFi enabled',
    description:
      'Easily connect, download and display images and send sensor data to the cloud',
    link: '/Inkplate-6MOTION/wifi/wifi-basics', // Update with correct URL
  },
  {
    icon: '/img/features_battery_icon.png',
    title: 'Low power mode',
    description:
      'Have your sketch run for months using deep sleep and smart Li-Ion battery management',
    link: '/Inkplate-6MOTION/low-power/deep-sleep', // Update with correct URL
  },
];

const FeaturesRow = () => {
  return (
    <div className={styles.featuresRow}>
      {features.map((feature, index) => (
        <div key={index} className={styles.featureItem}>
          <a href={feature.link}>
            <img src={feature.icon} alt={feature.title} className={styles.featureIcon} />
          </a>
          <h3 className={styles.featureTitle}>{feature.title}</h3>
          <p className={styles.featureDescription}>{feature.description}</p>
        </div>
      ))}
    </div>
  );
};

export default FeaturesRow;
