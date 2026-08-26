# Soldered Documentation

![Soldered Documentation](https://docs.soldered.com/assets/images/soldered_docs_social_card-ad511a2bacbd799beb36ea797101074f.jpg)

Welcome to the **Soldered Documentation** repository! This repository hosts all official documentation for Soldered products, which is published at [docs.soldered.com](https://docs.soldered.com/). The documentation is built using [Docusaurus](https://docusaurus.io/).  

### This documentation is a work in progress!

Some features of this documentation like **search** and all the supporting pages are still a work in progress! We're working on adding all our products to this new documentation, including our sensors, actuators, Inkplate and Dasduino boards and batteries. So, please be patient with us as we continue to work on it!

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

### Where things live

- All documentation files are located in the `/docs` folder. Edit existing markdown files or create new ones directly in this folder.
- Images used in the documentation should be placed in the `/static/img` folder.

### Editing Documentation

Using your LLM of choice in this folder, create a branch for the docs you're currently writing and edit them there. Once you're happy, merge to master using the LLM to cherry-pick only the files you've added.

Working on a branch keeps unfinished pages off master, and cherry-picking only your new files avoids clobbering pages someone else changed in the meantime.

### Previewing Your Changes

Run the following command to preview your changes locally:

```bash
npm run start
```

A local development server will start, typically accessible at [http://localhost:3000](http://localhost:3000). **All changes you make will be automatically reflected in real-time.**

Preview before you deploy. There is no staging site — what you build is what goes live.

### Publishing Changes

Commit everything using the LLM by telling it `commit everything`, then build and deploy.

Deploying is a one-time setup per computer (SSH key, then a `deploy.env` file), after which it is a single command:

```bash
./deploy.sh
```

Run `.\check_env.ps1` on Windows to verify your machine is set up correctly — it checks your tools, config, and SSH access to the server, and tells you what to fix if something is missing. Full setup instructions are in `DEPLOY_SETUP.md`.

Do not add `-a` to the `rsync` line in `deploy.sh`. The build folder on Windows reports mode `700` for every file, and `-a` would copy that onto the server. The site is served through POSIX ACLs, where the group bits act as the ACL mask, so mode `700` makes the `nginx` entry ineffective and every page returns 403 including the homepage. The flags there set the modes explicitly instead, and the comment above them explains each one.

---

## Soldered Documentation Buddy

We're currently developing **Soldered Documentation Buddy**, an intuitive app designed to assist you in writing, formatting, and managing documentation files seamlessly. This tool will simplify creating markdown files, managing images, and optimizing your documentation workflow.

**Coming soon! Stay tuned for updates.**

---

## About Soldered

<img src="https://raw.githubusercontent.com/SolderedElectronics/Soldered-Simple-Sensor-Arduino-Library/dev/extras/Soldered-logo-color.png" alt="soldered-logo" width="500"/>

At Soldered, we design and manufacture a wide selection of electronic products to help you turn your ideas into acts and bring you one step closer to your final project. Our products are intented for makers and crafted in-house by our experienced team in Osijek, Croatia. We believe that sharing is a crucial element for improvement and innovation, and we work hard to stay connected with all our makers regardless of their skill or experience level. Therefore, all our products are open-source. Finally, we always have your back. If you face any problem concerning either your shopping experience or your electronics project, our team will help you deal with it, offering efficient customer service and cost-free technical support anytime. 

## Have fun!

And thank you from your fellow makers at Soldered Electronics.
