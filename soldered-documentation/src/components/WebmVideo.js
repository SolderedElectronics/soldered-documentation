import React from 'react';

export default function WebmVideo({ src, width, maxWidth = "550px", height = "100%", autoplay = true, loop = true, muted = true, playsinline = true, controls = false }) {
  // Style with max-width that can be overridden
  const containerStyle = {
    maxWidth: width ? undefined : maxWidth,
    width: width || "100%",
    margin: "0 auto"
  };
  
  return (
    <div className="video-container" style={containerStyle}>
      <video 
        width="100%" 
        height={height} 
        autoPlay={autoplay} 
        loop={loop} 
        muted={muted} 
        playsInline={playsinline} 
        controls={controls}
      >
        <source src={src} type="video/webm" />
        Your browser doesn't support webm format
      </video>
    </div>
  );
}