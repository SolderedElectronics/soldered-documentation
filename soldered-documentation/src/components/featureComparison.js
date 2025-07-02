import React, { useState, useEffect } from 'react';
import IdealImage from '@theme/IdealImage';
import styles from './featureComparison.module.css';

const parseMarkdownLinks = (text) => {
    if (typeof text !== 'string') return text;

    // Replace all [label](url) with <a href="url">label</a>
    const regex = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g;

    const parts = [];
    let lastIndex = 0;
    let match;

    while ((match = regex.exec(text)) !== null) {
        if (match.index > lastIndex) {
            parts.push(text.slice(lastIndex, match.index));
        }
        parts.push(
            <a key={match[2]} href={match[2]} target="_blank" rel="noopener noreferrer">
                {match[1]}
            </a>
        );
        lastIndex = regex.lastIndex;
    }

    if (lastIndex < text.length) {
        parts.push(text.slice(lastIndex));
    }

    return parts.length > 0 ? parts : text;
};

const FeatureComparison = ({ data }) => {
    const [currentIndex, setCurrentIndex] = useState(0);
    const [transitionDirection, setTransitionDirection] = useState('none');

    // Collect all features in the order they appear
    const seen = new Set();
    const features = [];

    data.forEach((item) => {
        Object.keys(item).forEach((key) => {
            if (key !== 'name' && key !== 'image' && !seen.has(key)) {
                seen.add(key);
                features.push(key);
            }
        });
    });

    const currentInkplate = data[currentIndex];

    const handlePrev = () => {
        if (currentIndex > 0) {
            setTransitionDirection('left');
            setCurrentIndex(currentIndex - 1);
        }
    };

    const handleNext = () => {
        if (currentIndex < data.length - 1) {
            setTransitionDirection('right');
            setCurrentIndex(currentIndex + 1);
        }
    };

    const handleSelect = (index) => {
        if (index !== currentIndex) {
            setTransitionDirection(index > currentIndex ? 'right' : 'left');
            setCurrentIndex(index);
        }
    };

    useEffect(() => {
        const timeout = setTimeout(() => setTransitionDirection('none'), 300);
        return () => clearTimeout(timeout);
    }, [currentIndex]);

    const prevName = currentIndex > 0 ? data[currentIndex - 1].name : '';
    const nextName = currentIndex < data.length - 1 ? data[currentIndex + 1].name : '';

    return (
        <div className={styles.featureComparison}>
            {/* Top navigation list */}
            <div className={styles.topSelector}>
                {data.map((item, idx) => (
                    <button
                        key={item.name}
                        onClick={() => handleSelect(idx)}
                        className={`${styles.selectorItem} ${idx === currentIndex ? styles.selected : ''
                            }`}
                    >
                        {item.name}
                    </button>
                ))}
            </div>

            <div className={styles.imageContainer}>
                <IdealImage
                    img={require(`@site/static/${currentInkplate.image}`)}
                    alt={currentInkplate.name}
                    className={styles.inkplateImage}
                    style={{
                        width: '80%',
                        height: 'auto',
                        margin: '0 auto',
                        display: 'block',
                    }}
                />
            </div>

            {/* Navigation Arrows and Current Model */}
            <div className={styles.modelControls}>
                <button onClick={handlePrev} disabled={currentIndex === 0}>←</button>
                <span className={styles.currentName}>{currentInkplate.name}</span>
                <button onClick={handleNext} disabled={currentIndex === data.length - 1}>→</button>
            </div>

            {/* Previous/Next Model Names */}
            <div className={styles.modelNames}>
                <span className={styles.prevName}>{prevName}</span>
                <span className={styles.nextName}>{nextName}</span>
            </div>

            {/* Table */}
            <div className={styles.tableWrapper}>
                <table className={styles.comparisonTable}>
                    <thead>
                        <tr>
                            <th className={styles}>Feature</th>
                            <th
                                className={`${styles.inkplateCol} ${transitionDirection === 'left'
                                    ? styles.slideLeft
                                    : transitionDirection === 'right'
                                        ? styles.slideRight
                                        : ''
                                    }`}
                            >
                                Value
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {features.map((feature) => (
                            <tr key={feature}>
                                <td className={styles.fixedCol}>{feature}</td>
                                <td
                                    className={`${styles.inkplateCol} ${transitionDirection === 'left'
                                        ? styles.slideLeft
                                        : transitionDirection === 'right'
                                            ? styles.slideRight
                                            : ''
                                        }`}
                                >
                                    {parseMarkdownLinks(currentInkplate[feature])}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default FeatureComparison;
