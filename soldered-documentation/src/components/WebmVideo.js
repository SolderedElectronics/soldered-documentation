import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import WebmVideo from '@site/src/components/WebmVideo'; // Adjust path to your component

export default function MyPage() {
  return (
    <div>
      {/* Other content */}
      <WebmVideo src={useBaseUrl('/img/test2.webm')} />
      {/* Other content */}
    </div>
  );
}