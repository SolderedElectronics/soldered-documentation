import React, { useState } from 'react';
import styles from './customSelect.module.css';

const CustomSelect = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState('Select Inkplate Model');

  const options = [
    'Inkplate 6',
    'Inkplate 10',
    'Inkplate 2',
    'Inkplate COLOR',
    'Inkplate 6MOTION',
  ];

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  const handleSelect = (option) => {
    setSelectedOption(option);
    setIsOpen(false); // Close the menu after selection
  };

  return (
    <div className={styles.selectContainer}>
      <div
        className={styles.selectButton}
        onClick={handleToggle}
      >
        {selectedOption}
        <span className={styles.arrowDown}></span>
      </div>
      {isOpen && (
        <ul className={styles.selectMenu}>
          {options.map((option, index) => (
            <li
              key={index}
              className={styles.selectOption}
              onClick={() => handleSelect(option)}
            >
              {option}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CustomSelect;
