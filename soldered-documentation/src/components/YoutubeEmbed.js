// src/components/YouTubeEmbed.js
import React from 'react';

const YouTubeEmbed = ({ videoId, width = 560 }) => {
  const height = (width / 16) * 9; // Maintain 16:9 aspect ratio

  return (
    <div style={{ display: 'flex', justifyContent: 'center' }}>
      <iframe
        width={width}
        height={height}
        src={`https://www.youtube.com/embed/${videoId}`}
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen
      ></iframe>
    </div>
  );
};

export default YouTubeEmbed;