import { useEffect } from "react";
import "prismjs"; // Ensure PrismJS is imported
import "prismjs/components/prism-jsx"; // Import additional languages if needed

const FixPrism = () => {
  useEffect(() => {
    if (typeof window !== "undefined" && window.Prism) {
      window.Prism.highlightAll();
    }
  }, []);

  return null;
};

export default FixPrism;
