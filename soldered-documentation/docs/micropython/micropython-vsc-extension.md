---  
slug: /micropython/vsc-extension  
title: MicroPython - Using VSCode with MicroPython  
sidebar_label: Using VSCode with MicroPython  
id: micropython-vsc-extension  
hide_title: false  
---  

## Why Use VSCode for MicroPython?

Writing **MicroPython** code in **Visual Studio Code (VSCode)** provides a much more powerful development experience than most built-in editors that come with boards or simple serial terminals. With the help of the **Soldered MicroPython Helper** extension, you can:

- Write code with syntax highlighting, IntelliSense, and auto-complete.  
- Organize code into modules (`.py` files) for better maintainability.  
- Easily **upload, run, and manage files** on your MicroPython device.  
- View **live serial output** directly inside VS Code.  
- Install MicroPython firmware and Soldered libraries with one click.  
- Use an integrated, modern development workflow — without ever leaving VS Code.

## Requirements

To use the extension, install the following tools:

- **[Visual Studio Code](https://code.visualstudio.com/)** – your development environment  
- **[Python 3.7+](https://www.python.org/downloads/)** – required for esptool and mpremote  
- **[Node.js + npm](https://nodejs.org/)** – used for serial communication

```bash
python --version
node -v
npm -v
```

**To enable all features of the extension, run the following commands in your terminal**

```bash
# Install Python tools for firmware flashing and file communication
pip install esptool mpremote

# Install Node.js package for serial communication
npm install serialport
```

These tools power:

- Firmware flashing: `esptool`  
- File/device access: `mpremote`  
- Serial monitor integration: `serialport`

### Editing the PATH Variable

#### On Windows

- Open **Start**, search for **"environment variables"**, and open **"Edit the system environment variables"**.  
- Click **Environment Variables...**, then under **User variables**, select **Path** and click **Edit**.  
- Click **New**, paste the folder path (e.g., where `esptool` or `mpremote` is installed), and confirm with **OK**.  
- Restart the terminal to apply changes.

#### On Linux/macOS

Edit your shell config file (e.g., `~/.bashrc`, `~/.zshrc` or `~/.profile`) and add:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Apply changes with:

```bash
source ~/.bashrc  # or the appropriate file
```

Open a new terminal and test with:

```bash
esptool --help
mpremote --help
```

### Serial Port Access

- **Windows**: Usually works out of the box.  
- **Linux**: Add your user to the `dialout` group for permission to access serial ports:

```bash
sudo usermod -a -G dialout $USER
```

Log out and back in (or reboot) for changes to apply.

## Installing the Extension

1. Open **VS Code**.  
2. Go to the Extensions tab (or press `Ctrl+Shift+X`).  
3. Search for **Soldered MicroPython Helper**.  
4. Click **Install**.

After installation, you’ll see a **MicroPython** panel in the sidebar. This is your main interface for interacting with your device.

<CenteredImage src="/img/mp-vsc-ext/marketplace-install.png" width="600px" />

<InfoBox>You can also find the [**extension**](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper) on the marketplace!</InfoBox>

## Connecting Your MicroPython Device

1. Plug in your MicroPython-compatible board via USB.  
2. Open the extension in the tab.  
3. Click the **"Select Port"** dropdown in the sidebar.  
4. Choose the correct serial port for your device (e.g., `COM3`).

<InfoBox>Tip: If no port appears, ensure drivers are installed and the board is powered.</InfoBox>

Once connected, the extension will automatically detect your board type and show basic info.

## Installing MicroPython Firmware

Don’t have MicroPython installed yet?

1. In the sidebar, click **"Install Firmware"**.  
2. Choose your board model and firmware version.  
3. The extension downloads the correct binary and flashes it to your device.  
4. Done — ready to go.

<CenteredImage src="/img/mp-vsc-ext/firmware-select.png" width="400px" />

<InfoBox>Read the Info & Instructions section for currently supported Firmware installations.</InfoBox>

## Creating or Opening a Project

You can start from scratch or open an existing folder with `.py` files:

1. Go to **File → Open Folder...** and select your MicroPython project directory.  
2. Create new files like `main.py`, `boot.py`, or any custom modules.  
3. All your files in this folder can now be uploaded, edited, and run directly from VS Code.

## Uploading and Running Code

Use the sidebar controls to:

- **List and refresh files** – The `Files on Device` window shows what's on your board.  
- **Upload files** – Use the various upload buttons to transfer Python files to your board.  
- **Run Selected File** – Executes the current script.  
- **Stop Code** – Stops running code, which is usually used for infinite loops. This action is performed automatically if you run another file while one is currently running.  
- **Delete Selected File** – Removes the selected file from the board.

<CenteredImage src="/img/mp-vsc-ext/upload-active-file.png" width="800px" />

## Viewing Live Serial Output

The extension includes a built-in **Serial Monitor**:

1. Open the **Output** tab (in the bottom panel).  
2. Real-time logs, `print()` output, and exceptions from your MicroPython code will appear here.  
3. This allows you to debug directly without needing a separate terminal app.

<CenteredImage src="/img/mp-vsc-ext/serial-output.png" width="800px" />

## Using the Library Browser to Access Soldered Modules

Need drivers for sensors or displays?

1. Click the **"Library Browser"** tab.  
2. Search for keywords like `APDS`, `LCD`, or `DRV`.  
3. Select which libraries to install (just `.py` files, examples, or both).  
4. The extension automatically downloads and adds the files to your project.

<CenteredImage src="/img/mp-vsc-ext/soldered-modules.png" width="400px" />

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