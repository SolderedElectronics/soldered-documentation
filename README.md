# Soldered Documentation

![Soldered Documentation](https://soldered.com/documentation/assets/ideal-img/soldered_docs_social_card.54d7173.1700.jpg)

Welcome to the **Soldered Documentation** repository! This repository hosts all official documentation for Soldered products, which is published at [soldered.com/documentation/](https://soldered.com/documentation/). The documentation is built using [Docusaurus](https://docusaurus.io/).  

### This documentation is a work in progress!

**Search** now works and our current priority is making it more precise and useful! We're working on adding all our products to this new documentation, including our sensors, actuators, Inkplate and Dasduino boards and batteries. So, please be patient with us as we continue to work on it! If you're looking for any info you aren't able to find in the documentation, please [contact us](https://soldered.com/contact/).

---

## Getting Started

To contribute to or edit the documentation, follow these instructions:

### Requirements

Before you start editing, make sure you have:

- [Node.js and npm](https://nodejs.org/) installed on your computer.
- Basic familiarity with markdown syntax.
- [Git](https://git-scm.com/) installed on your computer. You can use GitHub desktop if you prefer.

### Installation

1. Clone the repository and navigate to the `soldered-documentation` folder in your terminal:

```bash
git clone [repository-url]
cd soldered-documentation
```

2. Install project dependencies:

```bash
npm install
```

(Docusaurus and all other required packages will be installed automatically based on the provided `package-lock.json`.)

### Editing Documentation

- Create a new branch for your edits:

```bash
git checkout -b your-branch-name
```

- All documentation files are located in the `/docs` folder. Edit existing markdown files or create new ones directly in this folder.
- Images used in the documentation should be placed in the `/static/img` folder.

### Previewing Your Changes

Run the following command to preview your changes locally:

```bash
npm run start
```

A local development server will start, typically accessible at [http://localhost:3000](http://localhost:3000). **All changes you make will be automatically reflected in real-time.**

### Publishing Changes

Once you're satisfied with your edits, commit your changes and create a pull request. After approval, your edits will be deployed live.

---

## Soldered Documentation Buddy

**Soldered Documentation Buddy** is a basic companion app written in Flask, which made it easy to get started with editing the documentation. It's meant to help you in writing, formatting, and managing documentation files seamlessly. This tool will simplify creating markdown files, managing images, and optimizing your documentation workflow. You can run it by running `documentation-buddy.py` in the `documentation-buddy` folder.

---

## About Soldered

<img src="https://raw.githubusercontent.com/SolderedElectronics/Soldered-Simple-Sensor-Arduino-Library/dev/extras/Soldered-logo-color.png" alt="soldered-logo" width="500"/>

At Soldered, we design and manufacture a wide selection of electronic products to help you turn your ideas into acts and bring you one step closer to your final project. Our products are intented for makers and crafted in-house by our experienced team in Osijek, Croatia. We believe that sharing is a crucial element for improvement and innovation, and we work hard to stay connected with all our makers regardless of their skill or experience level. Therefore, all our products are open-source. Finally, we always have your back. If you face any problem concerning either your shopping experience or your electronics project, our team will help you deal with it, offering efficient customer service and cost-free technical support anytime. 

## Have fun!

And thank you from your fellow makers at Soldered Electronics.
