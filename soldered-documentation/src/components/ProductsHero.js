import React, { useEffect, useState, useRef } from "react";
import styles from "./ProductsHero.module.css";

const IMAGE_FOLDER = "/img/small_product_images/";
const MAX_IMAGES = 25; // Maximum number of images to keep in DOM
const BUFFER_IMAGES = 5; // Extra images to keep as buffer
const IMAGE_WIDTH = 110; // Width of images + margin
const REMOVAL_THRESHOLD = -IMAGE_WIDTH * 2; // Remove when image is this far off-screen

// ✅ Provide a list of image filenames (no need for dynamic imports)
const imageFilenames = [
    "333000.jpg",
    "333001.jpg",
    "333002.jpg",
    "333003.jpg",
    "333004.jpg",
    "333005.jpg",
    "333006.jpg",
    "333007.jpg",
    "333008.jpg",
    "333009.jpg",
    "333010.jpg",
    "333011.jpg",
    "333012.jpg",
    "333013.jpg",
    "333014.jpg",
    "333015.jpg",
    "333016.jpg",
    "333017.jpg",
    "333018.jpg",
    "333019.jpg",
    "333020.jpg",
    "333021.jpg",
    "333022.jpg",
    "333023.jpg",
    "333024.jpg",
    "333025.jpg",
    "333026.jpg",
    "333027.jpg",
    "333028.jpg",
    "333029.jpg",
    "333030.jpg",
    "333031.jpg",
    "333032.jpg",
    "333033.jpg",
    "333034.jpg",
    "333035.jpg",
    "333036.jpg",
    "333037.jpg",
    "333039.jpg",
    "333040.jpg",
    "333041.jpg",
    "333042.jpg",
    "333043.jpg",
    "333044.jpg",
    "333045.jpg",
    "333046.jpg",
    "333047.jpg",
    "333049.jpg",
    "333050.jpg",
    "333051.jpg",
    "333052.jpg",
    "333054.jpg",
    "333055.jpg",
    "333056.jpg",
    "333058.jpg",
    "333059.jpg",
    "333060.jpg",
    "333061.jpg",
    "333063.jpg",
    "333065.jpg",
    "333066.jpg",
    "333067.jpg",
    "333068.jpg",
    "333069.jpg",
    "333070.jpg",
    "333073.jpg",
    "333075.jpg",
    "333077.jpg",
    "333079.jpg",
    "333080.jpg",
    "333081.jpg",
    "333082.jpg",
    "333083.jpg",
    "333084.jpg",
    "333087.jpg",
    "333088.jpg",
    "333089.jpg",
    "333090.jpg",
    "333091.jpg",
    "333092.jpg",
    "333093.jpg",
    "333094.jpg",
    "333095.jpg",
    "333096.jpg",
    "333098.jpg",
    "333101.jpg",
    "333102.jpg",
    "333103.jpg",
    "333104.jpg",
    "333105.jpg",
    "333106.jpg",
    "333107.jpg",
    "333108.jpg",
    "333109.jpg",
    "333110.jpg",
    "333111.jpg",
    "333113.jpg",
    "333114.jpg",
    "333115.jpg",
    "333116.jpg",
    "333117.jpg",
    "333118.jpg",
    "333119.jpg",
    "333120.jpg",
    "333121.jpg",
    "333122.jpg",
    "333123.jpg",
    "333124.jpg",
    "333125.jpg",
    "333127.jpg",
    "333128.jpg",
    "333129.jpg",
    "333130.jpg",
    "333131.jpg",
    "333132.jpg",
    "333133.jpg",
    "333134.jpg",
    "333135.jpg",
    "333136.jpg",
    "333143.jpg",
    "333144.jpg",
    "333148.jpg",
    "333149.jpg",
    "333150.jpg",
    "333151.jpg",
    "333152.jpg",
    "333153.jpg",
    "333154.jpg",
    "333160.jpg",
    "333163.jpg",
    "333164.jpg",
    "333169.jpg",
    "333170.jpg",
    "333179.jpg",
    "333188.jpg",
    "333201.jpg",
    "333211.jpg",
    "333213.jpg",
    "333224.jpg",
    "333225.jpg",
    "333226.jpg",
    "333250.jpg",
    "333268.jpg",
    "333270.jpg",
    "333271.jpg",
    "333272.jpg",
    "333273.jpg",
    "333301.jpg",
    "333325.jpg",
    "333326.jpg",
    "333327.jpg",
    "333328.jpg",
    "333329.jpg",
    "333330.jpg",
    "333331.jpg",
    "333332.jpg",
];


const ProductsHero = () => {
    const containerRef = useRef(null);
    const [imageQueue, setImageQueue] = useState([]);
    const animationRef = useRef(null);
    const lastTimeRef = useRef(0);
    const speedRef = useRef(0.5); // Pixels to move per frame
    const containerWidthRef = useRef(0);
    const [isPaused, setIsPaused] = useState(false);

    // Get a random image filename that's different from recent ones
    const getRandomImage = (recentImages) => {
        // Avoid repeating images that are currently visible if possible
        const recentSet = new Set(recentImages || []);
        const availableImages = imageFilenames.filter(img => !recentSet.has(img));

        // If we've used all images or have very few left, just pick randomly from all
        if (availableImages.length < 5) {
            return imageFilenames[Math.floor(Math.random() * imageFilenames.length)];
        }

        return availableImages[Math.floor(Math.random() * availableImages.length)];
    };

    // Generate unique ID for each image instance
    const generateId = () => `img_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

    // Initialize image queue
    useEffect(() => {
        if (imageFilenames.length === 0) return;

        // Determine container width for better initialization
        if (containerRef.current) {
            containerWidthRef.current = containerRef.current.getBoundingClientRect().width;
        } else {
            containerWidthRef.current = window.innerWidth;
        }

        // Calculate how many images we need to fill the screen plus buffer
        const imagesNeeded = Math.ceil(containerWidthRef.current / IMAGE_WIDTH) + BUFFER_IMAGES;
        const initialCount = Math.min(MAX_IMAGES, imagesNeeded);

        // Track used images to avoid immediate repeats
        const usedImages = [];

        // Create initial queue with properly spaced images
        const initialQueue = [];
        let currentPos = 0;

        for (let i = 0; i < initialCount; i++) {
            const filename = getRandomImage(usedImages);
            usedImages.push(filename);
            if (usedImages.length > 10) usedImages.shift(); // Keep track of last 10 used

            initialQueue.push({
                filename,
                id: generateId(),
                position: currentPos
            });

            currentPos += IMAGE_WIDTH;
        }

        setImageQueue(initialQueue);

        // Cleanup animation frame on unmount
        return () => {
            if (animationRef.current) {
                cancelAnimationFrame(animationRef.current);
            }
        };
    }, []);

    // Update container width on resize
    useEffect(() => {
        const handleResize = () => {
            if (containerRef.current) {
                containerWidthRef.current = containerRef.current.getBoundingClientRect().width;
            }
        };

        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);

    // Animation loop
    useEffect(() => {
        if (imageQueue.length === 0) return;

        const animate = (timestamp) => {
            if (!lastTimeRef.current) lastTimeRef.current = timestamp;
            const elapsed = timestamp - lastTimeRef.current;
            lastTimeRef.current = timestamp;

            // Only move images if not paused
            if (!isPaused) {
                // Ensure consistent animation speed
                const moveAmount = speedRef.current * (elapsed / 16);

                setImageQueue(prevQueue => {
                    // Get current filenames to avoid immediate repeats
                    const currentFilenames = prevQueue.map(img => img.filename);

                    // Move all existing images
                    let updatedQueue = prevQueue.map(img => ({
                        ...img,
                        position: img.position - moveAmount
                    }));

                    // Remove images that are far off-screen to the left
                    updatedQueue = updatedQueue.filter(img => img.position > REMOVAL_THRESHOLD);

                    // Find the rightmost image position
                    const rightmostPosition = updatedQueue.reduce(
                        (max, img) => Math.max(max, img.position),
                        -Infinity
                    );

                    // Add new images if needed to maintain proper coverage and buffer
                    const containerWidth = containerWidthRef.current;

                    if (rightmostPosition < containerWidth && updatedQueue.length < MAX_IMAGES) {
                        const newImagePosition = rightmostPosition + IMAGE_WIDTH;
                        const newFilename = getRandomImage(currentFilenames);

                        updatedQueue.push({
                            filename: newFilename,
                            id: generateId(),
                            position: newImagePosition
                        });
                    }

                    return updatedQueue;
                });
            }

            animationRef.current = requestAnimationFrame(animate);
        };

        animationRef.current = requestAnimationFrame(animate);

        return () => {
            if (animationRef.current) {
                cancelAnimationFrame(animationRef.current);
            }
        };
    }, [imageQueue, isPaused]);

    // Get product ID from filename (remove file extension)
    const getProductId = (filename) => {
        return filename.split('.')[0];
    };

    return (
        <div className={styles.heroContainer}>
            <div className={styles.imageRow} ref={containerRef}>
                {imageQueue.map(img => {
                    const productId = getProductId(img.filename);
                    return (
                        <a
                            key={img.id}
                            href={`https://solde.red/${productId}`}
                            className={styles.productLink}
                            style={{ transform: `translateX(${img.position}px)` }}
                            onMouseEnter={() => setIsPaused(true)}
                            onMouseLeave={() => setIsPaused(false)}
                            target={"_blank"}
                        >
                            <img
                                src={`${IMAGE_FOLDER}${img.filename}`}
                                alt={`Product ${productId}`}
                                className={styles.productImage}
                                loading="lazy"
                                width={IMAGE_WIDTH - 10} // Account for margin
                            />
                        </a>
                    );
                })}
            </div>
        </div>
    );
};

export default ProductsHero;