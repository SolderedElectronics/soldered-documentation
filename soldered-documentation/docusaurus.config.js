// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from 'prism-react-renderer';

require('dotenv').config();

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Soldered Documentation',
  tagline: 'Hardware specifications, detailed tutorials and open source files for all Soldered Electronics products',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://soldered.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/documentation/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'soldered', // Usually your GitHub org/user name.
  projectName: 'soldered-documentation', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
        },
        blog: false,
        pages: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-ideal-image',
      {
        quality: 80, // Adjust image quality (default is 75)
        max: 1700, // Max resolution
        min: 400, // Min resolution
        steps: 2, // Number of sizes generated
        disableInDev: false, // Enables optimized images in development mode
        fileTypes: ['jpeg', 'jpg', 'png', 'webp'],
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      announcementBar: {
        id: 'support_us',
        content:
          'This documentation is a work in progress! <b>Please leave your feedback <a target="_blank" rel="noopener noreferrer" href="https://soldered.com/contact/">here</a></b>.',
        backgroundColor: '#6F3B8B',
        textColor: '#ffffff',
        isCloseable: false,
      },
      docs: {
        sidebar: {
          hideable: false,
          autoCollapseCategories: false,
        },
      },
      image: 'img/soldered_docs_social_card.jpg',
      navbar: {
        title: "Documentation",
        logo: {
          alt: 'Soldered Electronics',
          src: 'img/soldered_logo_white.svg',
        },
        items: [
          { type: 'search', position: 'left' },
          {
            href: 'https://soldered.com',
            label: 'Back to Soldered.com',
            position: 'right',
            className: 'back-to-soldered-button',
          },
        ],
      },
      algolia: process.env.ALGOLIA_APP_ID
        ? {
          apiKey: process.env.ALGOLIA_API_KEY,
          indexName: process.env.ALGOLIA_INDEX_NAME,
          appId: process.env.ALGOLIA_APP_ID,
        }
        : undefined,
      footer: {
        links: [
          {
            title: 'About',
            items: [
              {
                label: 'Homepage',
                href: 'https://soldered.com/',
              },
              {
                label: 'About Soldered Electronics',
                href: 'https://soldered.com/about-us/',
              },
              {
                label: 'Why Soldered products?',
                href: 'https://soldered.com/why-soldered-products/',
              },
              {
                label: 'Contact us',
                href: 'https://soldered.com/contact/',
              },
            ],
          },
          {
            title: 'Soldered Product Documentation',
            items: [
              {
                label: 'Soldered Electronics GitHub',
                href: 'https://github.com/SolderedElectronics',
              },
              {
                label: 'Qwiic/easyC',
                href: '/qwiic',
              },
            ],
          },
          {
            title: 'Inkplate documentation',
            items: [
              {
                label: 'Getting started with Inkplate',
                href: 'https://inkplate.readthedocs.io/',
              },
              {
                label: 'Getting started with Inkplate 6MOTION',
                href: 'https://docs.inkplate.com/',
              },
              {
                label: 'Inkplate Arduino Library',
                href: 'https://github.com/SolderedElectronics/Inkplate-Arduino-library',
              },
              {
                label: 'Soldered Image Converter',
                href: 'https://docs.inkplate.com/Inkplate-6MOTION/basics/image-converter',
              },
            ],
          },
        ],
        logo: {
          alt: 'Soldered Electronics',
          src: 'img/soldered_logo_purple.svg',
          href: 'https://soldered.com/',
          width: 160,
          height: 51,
        },
        copyright: `Copyright © ${new Date().getFullYear()} Soldered. All rights reserved. Built with <a href="https://docusaurus.io/" target="_blank" rel="noopener noreferrer" class="footer__link-item">Docusaurus <svg width="13.5" height="13.5" aria-hidden="true" viewBox="0 0 24 24" class="iconExternalLink_node_modules-@docusaurus-theme-classic-lib-theme-Icon-ExternalLink-styles-module"><path fill="currentColor" d="M21 13v10h-21v-19h12v2h-10v15h17v-8h2zm3-12h-10.988l4.035 4-6.977 7.07 2.828 2.828 6.977-7.07 4.125 4.172v-11z"></path></svg></a>`
      },
      prism: {
        theme: prismThemes.nightOwlLight,
        darkTheme: prismThemes.oceanicNext,
      },
    }),
};

export default config;
