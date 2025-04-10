---
slug: /arduino-GitHub
title: Using Git with Arduino projects
id: arduino-GitHub
hide_title: False
pagination_next: null
pagination_prev: null
---

## Why Use GitHub with Arduino?

Even for single-person projects, using Git and GitHub brings significant benefits:

*   **Version Control** – Roll back to earlier code versions when bugs appear.
*   **Backup** – Cloud storage ensures you don’t lose your work.
*   **Collaboration** – Easily share and collaborate with others.
*   **Traceability** – Track when and why changes were made.
*   **Documentation** – Use README.md and issues for project context.  
*   **Publishing** – Share open-source libraries, projects, or inspiration with the world.
    

## Prerequisites

1.  A working Arduino project folder, e.g., Documents/Arduino/exampleProject.
    
2.  Git installed on your system.→ [Download Git](https://git-scm.com/)
    
3.  A GitHub account.→ [Sign up for GitHub](https://github.com/)
    
4.  (Optional) GitHub Desktop or familiarity with CLI commands.
    

## Step-by-Step: Use GitHub with an Existing Arduino Project

### Step 1: Navigate to Your Arduino Project Folder

1.  Open File Explorer (or terminal) to locate your project folder, e.g.:
   
 ```cpp
Documents/Arduino/exampleProject/
```
    

### Step 2: Initialize Git

1.  Open a terminal (e.g., Git Bash, Terminal, or CMD on Windows).
2.  Navigate to your project folder:
   
```cpp
cd ~/Documents/Arduino/exampleProject
git init
```

<CenteredImage src="/img/arduino-GitHub/1.png"/>

3.  This creates a .git folder, turning your sketch folder into a Git repository.
    

### Step 3: Check What Will Be Tracked

1.  Run the following command:

```cpp
git status
```

<CenteredImage src="/img/arduino-GitHub/1.png"/>


2.  You’ll see all files in the folder marked as untracked (e.g., .ino, .cpp, .h, etc.).
    

### Step 4: Add a .gitignore File (Optional)

Some files don’t belong in Git (like compiled binaries or temporary files). Create a .gitignore file in the root of your project folder.

#### Example .gitignore:

```cpp
# Arduino build files
*.hex
*.elf
*.bin

# Mac and VSCode files
.DS_Store
.vscode/

# Temporary files
*.tmp
```

### Step 5: Make the First Commit

1.  Add all files to the repository:

```cpp
git add .
```
     
<CenteredImage src="/img/arduino-GitHub/1.png"/>

2.  Save a snapshot of the project:
    
```cpp
git commit -m "Initial commit – exampleProject"
```

<CenteredImage src="/img/arduino-GitHub/1.png"/>


### Step 6: Create a New GitHub Repository

1.  Go to [GitHub](https://github.com/) and log in. 
2.  Click **New repository**.
3.  Name it (e.g., exampleProject). 
4.  Choose Private or Public visibility. 
5.  Don’t initialize with a README — you already have code.
6.  Click **Create repository**.
    
<CenteredImage src="/img/arduino-GitHub/1.png"/>


GitHub will show instructions for pushing an existing repo.

### Step 7: Link Local Repo to GitHub

1.  In the terminal (in your project folder), run:
   
```cpp
git remote add origin https://github.com/YOUR_USERNAME/exampleProject.git
git branch -M main
git push -u origin main
```

<CenteredImage src="/img/arduino-GitHub/1.png"/>


2.  Your local Arduino project is now published on GitHub!
    

### Optional: Add README and LICENSE

#### Create README.md:

```cpp
# exampleProject

An Arduino project demonstrating a reusable LED blinker class.
```


#### Add LICENSE:


For open-source projects, consider MIT or GPL licenses:

1.  Create a LICENSE file locally or via GitHub’s web UI.
    
2.  Include license details to clarify usage rights.
    

### Typical Workflow Going Forward

```cpp
# Make changes in VSCode or Arduino IDE.
# Then commit & push:
git add .
git commit -m "Describe what you changed"
git push

```

If collaborating with others, always run git pull before starting work.

### Bonus: Clone the Repo on Another Machine

On a new computer or fresh environment:

```cpp
git clone https://github.com/YOUR_USERNAME/exampleProject.git
```

Open the cloned folder in Arduino IDE or VSCode and continue development seamlessly.

