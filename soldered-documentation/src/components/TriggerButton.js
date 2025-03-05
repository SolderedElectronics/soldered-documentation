import React from 'react';
import styles from './triggerButton.module.css';

const TriggerButton = () => {
  const handleButtonClick = () => {
    // Find the selectContainer element in the navbar
    const selectContainer = document.querySelector('.selectContainer');
    if (selectContainer) {
      selectContainer.click(); // Trigger a click event on the selectContainer
    } else {
      console.warn('selectContainer not found in the DOM');
    }
  };

  return (
    <div className={styles.selectWrap}>
      <div className={styles.innerDiv}>
        <img src="/img/start_arrow.png" alt="Start Arrow" className={styles.notifyArrow} />
        <button className={styles.triggerButton} onClick={handleButtonClick}>
          Start here:<br></br><strong>Select Inkplate model</strong>
        </button>
      </div>
    </div>
  );
};

export default TriggerButton;
