---
slug: /pomodoro-timer-solder-kit/how-to-reprogram
title: Pomodoro Timer Solder Kit - How to reprogram
sidebar_label: How to Reprogram
id: pomodoro-solder-kit-how-to-reprogram
hide_title: True
pagination_next: null
---

# How to Reprogram

## Introduction

On this page, we'll show you how to reprogram your Pomodoro Solder Kit and upload new firmware to it.

<WarningBox>Be careful while working with firmware! Always make sure you upload valid `.py` files and don’t remove essential system files from your board.</WarningBox>

<InfoBox>This tutorial assumes your Pomodoro Kit is already assembled. If not, check the [**Assembly Guide**](/documentation/pomodoro-solder-kit/assembly-guide) first.</InfoBox>

<QuickLink 
  title="Pomodoro Timer Solder Kit Firmware Repository" 
  description="Source code and official MicroPython firmware files"
  url="https://github.com/SolderedElectronics/pomodoro-timer-firmware"
/>

<CenteredImage src="/img/pomodoro-solder-kit/github_repo_overview.png" alt="Pomodoro Timer firmware GitHub repository overview"  caption="Official Pomodoro Timer firmware repository on GitHub"/>

---

## MicroPython Firmware (RP2040)

The Pomodoro Timer Solder Kit uses a specific and tested version of the MicroPython firmware for the RP2040 chip.  
This exact firmware binary is included in the official repository and should be used whenever reinstalling or reflashing MicroPython on the board.

<QuickLink 
  title="RP2040 MicroPython firmware"
  description="Source code and official MicroPython firmware files"
  url="https://github.com/SolderedElectronics/pomodoro-timer-firmware/blob/main/pomodoro_timer_firmware.uf2"
/>

This UF2 contains the correct MicroPython interpreter version used during development and testing of the Pomodoro Timer firmware.  
Using other or newer MicroPython builds may lead to unexpected behavior or incompatibilities with board drivers, file handling or timing.

<WarningBox>Do not replace the UF2 with unofficial or third-party RP2040 MicroPython builds unless you fully understand the consequences.  
Only the provided binary is guaranteed to work with this project.</WarningBox>

---

## 1. What You’ll Need

Before we start, make sure you have:

- A **Soldered Pomodoro Solder Kit**
- A **USB-C cable** (data-capable)
- A **computer with Python 3 installed**
- Either:
  - **Visual Studio Code** with the [**Soldered MicroPython Helper**](https://soldered.com/documentation/micropython/getting-started-with-vscode/), or  
  - The **mpremote** command-line tool.

---

## 2. Connecting the Kit

1. Plug your Pomodoro Kit into your computer using a USB-C cable.  
2. Wait for it to appear as a serial device (on Windows: `COMx`, on macOS/Linux: `/dev/ttyACMx` or `/dev/ttyUSBx`).

You can verify the connection using:

```bash
ls /dev/tty*
```

or on Windows:
```bash
mode
```

---

## 3. Recommended Method: Soldered MicroPython Helper (VS Code Extension)

This is the easiest and most beginner-friendly way to upload and manage firmware on your Pomodoro Timer.

<CenteredImage 
  src="/img/pomodoro-solder-kit/vscode_helper.png" 
  alt="VS Code MicroPython Helper" 
  width="500px" 
  caption="Soldered MicroPython Helper inside VS Code"
/>

<QuickLink 
  title="Soldered MicroPython Helper extension" 
  description="Recommended way to upload firmware and manage files"
  url="https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper"
/>

### 3.1 Install the Extension

1. Install the Soldered MicroPython Helper extension from the VS Code Marketplace

2. Open Visual Studio Code.

3. Click on the Soldered MicroPython Helper icon in the left sidebar.

<CenteredImage 
  src="/img/pomodoro-solder-kit/mpext.png"
  alt="MP Helper in the left sidebar."
  width="300px"
  caption="Location of the Soldered MicroPython Helper in the left sidebar."
/>

### 3.2 Connect to Your Pomodoro Timer

Find "COM port selection" right below "Info & Instructions" and select the correct COM port.

<CenteredImage 
  src="/img/pomodoro-solder-kit/vscode_connect_board.png"
  alt="Connecting to Pomodoro Timer in VS Code"
  width="300px"
  caption="Selecting the correct serial port for the Pomodoro Timer"
/>

<WarningBox>If the board does not appear:  
• Try another USB cable (must support data)  
• Close applications that may be using the serial port  
• Reconnect the board</WarningBox>

### 3.3 Open the Firmware Repository

Inside VS Code, open the project folder you downloaded or cloned:

```
https://github.com/SolderedElectronics/pomodoro-timer-firmware
```


<InfoBox>Ensure the folder contains: <code>main.py</code>, <code>seven_segment.py</code>, <code>buzzer_music.py</code> and <code>music_options.py</code>.</InfoBox>

### 3.4 Manage Files (Upload & Edit)

Open the tab **Upload & Manage Python Scripts**

<CenteredImage 
  src="/img/pomodoro-solder-kit/vscode_file_management.png"
  alt="Upload & Manage Python Scripts tab in VS Code"
  width="300px"
  caption="File management interface for uploading and editing Pomodoro firmware files"
/>

In this tab you can:

#### Download files from the board
Double-click any file to download it locally and open it for editing.

#### Upload individual files
Upload modified Python files back to the RP2040.

#### Upload the entire firmware repository
Choose **Upload Python File(s) From PC**, then select the top-level firmware folder you downloaded.  
The extension will automatically scan that folder and all of its subfolders, detect every `.py` file, and upload them to the board.

<InfoBox>Uploading the entire repository is the simplest way to restore original firmware or upload a customized version.</InfoBox>

### 3.5 Upload Required Firmware Files

Make sure these files are uploaded:

- main.py  
- seven_segment.py  
- buzzer_music.py  
- music_options.py

### 3.6 Apply the Firmware (Reset the Board)

After uploading the files:

- Press "RESET MCU" in the extension  
  or  
- Unplug and reconnect your Pomodoro Timer

The board will restart and run the newly uploaded firmware.

<InfoBox>If the display does not show expected behavior, verify that all required files were uploaded correctly.</InfoBox>

---

## 4. Alternative Method: mpremote (CLI)

<QuickLink 
  title="mpremote (CLI Tool)" 
  description="Official MicroPython command-line interface for RP2040 boards"
  url="https://docs.micropython.org/en/latest/reference/mpremote.html"
/>

`mpremote` is the official command-line tool for communicating with MicroPython devices, including the RP2040 used in the Pomodoro Timer.  
It provides access to the file system, allows uploading `.py` files, running scripts, and performing board resets.

<InfoBox>The CLI method provides the same functionality as the VS Code extension, but all steps are performed manually through the terminal.</InfoBox>

### 4.1 Install mpremote

```bash
pip install mpremote
```

```bash
mpremote --version
```

### 4.2 Detect and Connect to Your Board

#### List available MicroPython-compatible devices
This command scans all connected serial ports and shows devices that respond as MicroPython boards:

```bash
mpremote devs
```

Use this to confirm that your computer detects the Pomodoro Timer and to identify which serial port it uses.

#### Show detailed list of connectable ports
This gives a more explicit view of all ports and their identifiers:

```bash
mpremote connect list
```

Helpful if you have multiple USB devices connected and need to distinguish which one is the RP2040.

#### Connect to the board manually
Once you know the correct port, connect using:

```bash
mpremote connect COM4
mpremote connect /dev/ttyACM0
mpremote connect /dev/tty.usbmodemXXXX
```

After a successful connection, you can run mpremote commands directly on the device.

<WarningBox>If the board does not appear, check your USB cable (must support data), close any application that may be using the serial port, and reconnect the device.</WarningBox>


### 4.3 Managing Files on the Board

#### Upload files to the device
This command copies one or more Python files from your computer to the root of the RP2040 filesystem:

```bash
mpremote cp main.py seven_segment.py buzzer_music.py music_options.py :
```

The colon (`:`) represents the device filesystem.

You can also specify the connection inline:

```bash
mpremote connect COM4 cp main.py seven_segment.py buzzer_music.py music_options.py :
```

Use this when you want to upload updated firmware files or replace existing files on the device.

#### List files stored on the device
Shows all files currently present on the RP2040 filesystem:

```bash
mpremote ls
```

This is equivalent to:

```bash
mpremote fs ls
```

Use this to verify that the correct firmware files are present after uploading.

#### Remove a file from the device
Deletes a file from board storage:

```bash
mpremote rm old_script.py
```

Explicit path variant:

```bash
mpremote rm :old_script.py
```

<WarningBox>Only delete files you are sure you no longer need. Avoid removing critical firmware files unless replacing them immediately.</WarningBox>


### 4.4 Running and Resetting Your Board

#### Run a script directly (without saving it)
Executes a Python script from your computer on the RP2040:

```bash
mpremote run main.py
```

The script runs in RAM and is not stored on the device.  
Useful for quick testing or debugging without overwriting your firmware.

#### Reset the board
Performs a soft hardware reset, like pressing the reset button:

```bash
mpremote reset
```

After a reset, the board automatically runs `main.py` if it exists on the device.

<InfoBox>If your device does not behave as expected after uploading files, run a reset to ensure the firmware restarts cleanly and loads the latest versions of your scripts.</InfoBox>

---

## 5. Checking if Everything Works

After flashing, when you power on the Pomodoro Timer, it should:

- Light up the **RGB LED (purple)**  
- Play a **short jingle**  
- Display the **settings menu** on the 7-segment display  

If all this works, your firmware upload was successful.

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_15.webp" alt="Pomodoro Timer finished build" width="700px" caption="Firmware successfully running!"/>

---

## 6. Next Steps: Simple Mods

Now that your Pomodoro Kit is up and running, here are a few simple and safe modifications you can make to customize it to your liking.

### 1. Change Default Session Durations
In `main.py`, find the `set_times()` function and modify:
```python
study = 25
rest = 5
```
For example:
```python
study = 50
rest = 10
```

### 2. Adjust Step Size
Still in `set_times()`, change how fast the time increases or decreases:
```python
study = min(study + 5, 95)
rest  = min(rest + 5, 95)
```
You can replace `5` with `1` for smaller steps or `10` for faster adjustments.

### 3. Change LED Colors
In `main()`, edit the LED color for each mode:
```python
update_led((0, 255, 0))    # Study
update_led((255, 0, 0))    # Rest
```
For example:
```python
update_led((0, 0, 255))    # Blue study
update_led((255, 100, 0))  # Orange rest
```

### 4. Adjust LED Brightness
In `main.py`, change the brightness level:
```python
brightness_level = 0.3
```
You can use any value between `0.0` (off) and `1.0` (maximum brightness).

### 5. Customize the Jingles
You can easily replace the default melodies in `music_options.py` using [onlinesequencer.net](https://onlinesequencer.net).

Steps:
1. Go to **onlinesequencer.net** and create your melody.
2. Copy the sequence and paste it into one of the variables, for example:
   ```python
   intro_default = "Online Sequencer: 120; E4 B4 C5"
   ```
3. Remove the `"Online Sequencer"` text and any trailing characters like `;:`
4. Save and upload your modified file.

**Example:**
Change the startup tune in `music_options.py`:
```python
intro_default = "T120 O5 C D E F G"
```
Then re-upload your firmware as before. Upon startup, your new melody will play.

---

You can modify a lot more. For example, you can change how the buttons behave, create new LED patterns, or even write your own timer logic.  

Feel free to experiment and explore the code. If something stops working, you can always follow this guide again to restore the original firmware.  

Everything is open-source, so have fun and make it your own!


