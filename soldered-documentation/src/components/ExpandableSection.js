import React, { useState, useRef } from 'react';
import styles from './expandableSection.module.css';

const ExpandableSection = ({ title, children }) => {
  const [isOpen, setIsOpen] = useState(false);
  const contentRef = useRef(null);

  return (
    <div className={styles.expandableSection}>
      <button className={styles.button} onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? '▼ ' : '▶ '}
        {title}
      </button>
      <div
        ref={contentRef}
        className={styles.content}
        style={{
          height: isOpen ? contentRef.current.scrollHeight : 0,
          overflow: 'hidden',
          transition: 'height 0.3s ease',
        }}
      >
        <div className={styles.innerContent}>{children}</div>
      </div>
    </div>
  );
};

export default ExpandableSection;