import React from 'react';
import Head from '@docusaurus/Head';
import MDXCode from '@theme/MDXComponents/Code';
import MDXA from '@theme/MDXComponents/A';
import MDXPre from '@theme/MDXComponents/Pre';
import MDXDetails from '@theme/MDXComponents/Details';
import MDXHeading from '@theme/MDXComponents/Heading';
import MDXUl from '@theme/MDXComponents/Ul';
import MDXLi from '@theme/MDXComponents/Li';
import MDXImg from '@theme/MDXComponents/Img';
import Admonition from '@theme/Admonition';
import Mermaid from '@theme/Mermaid';

import ErrorBox from '@site/src/components/error_box';
import InfoBox from '@site/src/components/info_box';
import WarningBox from '@site/src/components/warning_box';
import SuccessBox from '@site/src/components/successbox';
import ProductTable from '@site/src/components/ProductTable';
import CenteredImage from '@site/src/components/centeredImage';
import ExpandableSection from '@site/src/components/ExpandableSection';
import YouTubeEmbed from '@site/src/components/YouTubeEmbed';
import QuickLink from '@site/src/components/QuickLink';
import SectionTitle from '@site/src/components/SectionTitle';
import FunctionDocumentation from '@site/src/components/FunctionDocumentation';
import FlickityCarousel from '@site/src/components/FlickityCarousel';
import WebmVideo from '@site/src/components/WebmVideo';

const MDXComponents = {
  // Built-in Docusaurus components
  Head,
  details: MDXDetails, // For MD mode support
  Details: MDXDetails,
  code: MDXCode,
  a: MDXA,
  pre: MDXPre,
  ul: MDXUl,
  li: MDXLi,
  img: MDXImg,
  h1: (props) => <MDXHeading as="h1" {...props} />,
  h2: (props) => <MDXHeading as="h2" {...props} />,
  h3: (props) => <MDXHeading as="h3" {...props} />,
  h4: (props) => <MDXHeading as="h4" {...props} />,
  h5: (props) => <MDXHeading as="h5" {...props} />,
  h6: (props) => <MDXHeading as="h6" {...props} />,
  admonition: Admonition,
  mermaid: Mermaid,

  // Custom components
  ErrorBox,
  InfoBox,
  WarningBox,
  SuccessBox,
  ProductTable,
  CenteredImage,
  ExpandableSection,
  YouTubeEmbed,
  QuickLink,
  SectionTitle,
  FunctionDocumentation,
  FlickityCarousel,
  WebmVideo
};

export default MDXComponents;
