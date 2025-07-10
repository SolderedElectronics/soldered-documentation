---  
slug: /micropython/getting-started-with-vscode  
title: MicroPython - Getting started with VSCode  
sidebar_label: Getting started with VSCode  
id: micropython-vsc-extension  
hide_title: false  
---  

## Why Use VS Code for MicroPython?

Writing **MicroPython** code in **Visual Studio Code (VS Code)** provides a much more powerful development experience than most built-in editors that come with boards or simple serial terminals. With the help of the [**Soldered MicroPython Helper extension**](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper), you can:

- Write code with syntax highlighting, IntelliSense, and auto-complete.  
- Organize code into modules (`.py` files) for better maintainability.  
- Easily **upload, run, and manage files** on your MicroPython device.  
- View **live serial output** directly inside VS Code.  
- Install MicroPython firmware and Soldered libraries with one click.  
- Use an integrated, modern development workflow without ever leaving VS Code.

## Requirements and Initial Setup

Before using the extension, make sure the following tools are installed **and working** correctly. These tools are **essential** for communication with your MicroPython board.

<InfoBox title="Why do I need all this?">
To upload files, flash firmware, and access serial output from your MicroPython board, your system must have the right tools installed and available globally via your terminal.
</InfoBox>

### Required Tools

- **[Visual Studio Code](https://code.visualstudio.com/)** – main development environment  
- **[Python 3.7+](https://www.python.org/downloads/)** – used to run `esptool` and `mpremote`  
- **[Node.js + npm](https://nodejs.org/)** – used by the extension to access serial ports (via the `serialport` library)

<WarningBox title="Important">
You must be able to run the commands `python`, `node`, and `npm` in your terminal. If these commands fail, your environment is not set up correctly.
</WarningBox>

Verify installation:

```bash
python --version   # Expected: Python 3.7 or higher
node -v            # Expected: Node.js 14+ or higher
npm -v             # Confirms npm is available
```

### What Are These Tools?

- **[`esptool`](https://github.com/espressif/esptool)** – used to flash MicroPython firmware to ESP32/ESP8266 boards
- **[`mpremote`](https://docs.micropython.org/en/latest/reference/mpremote.html)** – used to run code, upload files, and interact with your board over USB
- **[`serialport`](https://www.npmjs.com/package/serialport)** – a Node.js library the extension uses to read/write serial data

## Quick Setup: Install Required Tools

Run the following commands **in your terminal** to install everything:

```bash
# Install Python tools for firmware flashing and file communication
pip install esptool mpremote

# Install Node.js package for serial communication
npm install serialport
```

If these commands succeed without errors, you're ready to use the extension.

## Test the Setup

Run the following commands to ensure the tools are globally available:

```bash
esptool --help
mpremote --help
```

If you see help text with usage instructions, you're good to go.

If you get an error like “command not found” or “not recognized,” it likely means the tool is not in your PATH.

## Fixing PATH Issues

<InfoBox title="Why this matters">
Your system needs to find `esptool` and `mpremote` when called from the terminal. This is done via the PATH environment variable.
</InfoBox>

### On Windows

1. Open **Start**, search for **"environment variables"**, and select **"Edit the system environment variables"**.  
2. Click **Environment Variables...**.  
3. Under **User variables**, select `Path` and click **Edit**.  
4. Click **New**, then add the folder where Python installs scripts (usually:  
   `C:\Users\YOURNAME\AppData\Roaming\Python\Python3x\Scripts`).  
5. Click **OK** to save and restart your terminal.

### On Linux/macOS

Add the following to your shell config file (`~/.bashrc`, `~/.zshrc`, or `~/.profile`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then apply the changes:

```bash
source ~/.bashrc  # or the relevant file
```

Once set, re-test with:

```bash
esptool --help
```

If help text appears, you're ready to flash and upload!

## Installing the Extension

1. Open **VS Code**.  
2. Go to the Extensions tab (or press `Ctrl+Shift+X`).  
3. Search for **Soldered MicroPython Helper**.  
4. Click **Install**.

After installation, you’ll see a **MicroPython** panel in the sidebar. This is your main interface for interacting with your device.

<CenteredImage src="/img/mp-vsc-ext/marketplace-install.png" width="600px" alt="Extension on the marketplace" caption="Installing Soldered MicroPython Helper from the extension tab."/>

<InfoBox>You can also find the [**extension**](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper) on the marketplace!</InfoBox>

## Connecting Your MicroPython Device

1. Plug in your MicroPython-compatible board via USB.  
2. Open the extension in the tab.  
3. Click the **"Select Port"** dropdown in the sidebar.  
4. Choose the correct serial port for your device (e.g., `COM3`).

<InfoBox>Tip: If no port appears, ensure that drivers are installed and that the board is powered.</InfoBox>

Once connected, the extension will automatically detect your board type and display basic information.

## Installing MicroPython Firmware

Don't have MicroPython installed **on your development board** yet?

1. In the sidebar, click **"Install MicroPython on your board"**.  
2. Select your board model and desired firmware version.  
3. The extension will automatically download the correct binary and flash it to your device.  
4. Once complete, your board is ready to use with MicroPython.

<CenteredImage src="/img/mp-vsc-ext/firmware-select.png" width="400px" alt="Firmware search" caption="Search and install MicroPython firmware." />

<InfoBox>If you're using a **Soldered** board, MicroPython is already pre-installed. You can skip this step unless you want to update or reflash the firmware.</InfoBox>

<InfoBox>For a list of supported board types and firmware versions, see the **Info & Instructions** section inside the extension panel.</InfoBox>

## Creating or Opening a Project

You can start from scratch or open an existing folder with `.py` files:

1. Go to **File → Open Folder...** and select your MicroPython project directory.  
2. Create new files like `main.py`, `boot.py`, or any custom modules.  
3. All your files in this folder can now be uploaded, edited, and run directly from VS Code.

## Uploading and Running Code

Use the sidebar controls to:

- **List and refresh files** – The `Files on Device` window shows what is currently on your board.  
- **Upload files** – Use the various upload buttons to transfer Python files to your board.  
- **Run Selected File** – Runs the currently open file on the board and streams its output live in the Output tab.  
- **Stop Code** – Stops running code, which is usually used for infinite loops. This action is performed automatically if you run another file while one is currently running.  
- **Delete Selected File** – Removes the selected file from the board.

<CenteredImage src="/img/mp-vsc-ext/upload-active-file.png" width="800px" alt="Upload & Manage" caption="Upload & Manage Python Scripts section." />

## Viewing Live Serial Output

The extension includes a built-in **Serial Monitor**:

1. Open the **Output** tab (in the bottom panel).  
2. Real-time logs, `print()` output, and exceptions from your MicroPython code will appear here.  
3. This allows you to debug directly without needing a separate terminal app.

<CenteredImage src="/img/mp-vsc-ext/serial-output.png" width="800px" alt="Serial output." caption="Live Serial output within VSCode."/>

## Using the Library Browser to Access Soldered Modules

Need drivers for sensors or displays? You can access the [**Soldered MicroPython Modules library**](https://github.com/SolderedElectronics/Soldered-MicroPython-Modules) from the extension.

1. Click the **"Fetch Soldered MicroPython Module"** tab.  
2. Search for keywords like `APDS`, `LCD`, or `DRV`.  
3. Select which libraries to install (just `.py` files, examples, or both).  
4. The extension automatically downloads and adds the files to your project.

<InfoBox>For a detailed explanation of how this works, see the [**Installing Soldered Modules via VS Code**](/micropython/installing-soldered-micropython-modules#option-1-installing-modules-via-vs-code-extension) guide.</InfoBox>

<CenteredImage src="/img/mp-vsc-ext/soldered-modules.png" width="400px" alt="Soldered Modules" caption="Fetch Soldered MicroPython Module section."/>

## Source Code and Development

You can view the full source code for this extension on [**GitHub**](https://github.com/SolderedElectronics/Soldered-MicroPython-Helper).

<InfoBox>If you'd like to contribute or modify this extension locally, follow the steps below.</InfoBox>

### 1. Install dependencies

Make sure you have [Node.js](https://nodejs.org/), `npm`, and [Python 3.x](https://www.python.org/) installed.

```bash
npm install
pip install esptool mpremote
```

### 2. Build the extension

```bash
npm run vscode:prepublish
```

### 3. Launch in VS Code

- Open the project folder in VS Code.  
- Press `F5` to open a new Extension Development Host window.  
- The extension will load there and can be tested as if it were installed.