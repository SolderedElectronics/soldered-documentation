import React from 'react';
import { useLocation } from '@docusaurus/router';

const HomepageStyles = () => {
  const location = useLocation();

  // Only apply styles if on the homepage
    return (
      <style>
        {`
          .theme-doc-breadcrumbs {
            display: none;
          }
        `}
      </style>
    );

  return null;
};

export default HomepageStyles;
