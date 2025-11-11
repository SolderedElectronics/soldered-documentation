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

This is the easiest way to manage and program your Pomodoro Kit.

<CenteredImage src="/img/pomodoro-solder-kit/vscode_helper.png" alt="VS Code MicroPython Helper" width="500px" caption="Soldered MicroPython Helper inside VS Code"/>

1. Install the [**Soldered MicroPython Helper**](https://soldered.com/documentation/micropython/getting-started-with-vscode/).  
2. Open **Visual Studio Code** and click the **MicroPython** icon on the left sidebar.  
3. Connect to your board (choose the correct COM or serial port).  
4. In the **File Explorer**, open the folder where you downloaded the Pomodoro firmware repository:
   ```
   https://github.com/SolderedElectronics/pomodoro-timer-firmware
   ```
5. Upload the following files to your board:
   - `main.py`
   - `seven_segment.py`
   - `buzzer_music.py`
   - `music_options.py`
6. Press the **Reset Board** button or unplug and replug the kit.

Your Pomodoro Timer will now boot with the uploaded firmware.

---

## 4. Alternative: Flashing with mpremote (CLI Method)

[`mpremote`](https://docs.micropython.org/en/latest/reference/mpremote.html) is the official command-line tool for interacting with MicroPython devices, such as the RP2040 (Raspberry Pi Pico and Pico W).
It allows you to connect to your board, upload code, manage files, and run scripts directly.

First, make sure `mpremote` is installed:

```bash
pip install mpremote
```

Check the version to confirm:

```bash
mpremote --version
```

---

## Connecting to Your Board

To see which devices are available:

```bash
mpremote devs
```

or equivalently:

```bash
mpremote connect list
```

Then connect to your board:

```bash
mpremote connect COM14          # Windows
mpremote connect /dev/ttyACM0   # Linux
mpremote connect /dev/tty.usbmodemXXXX   # macOS
```

Running just `mpremote` without arguments will auto-connect to the first available device and open a REPL prompt.

---

## Managing Files

### Uploading files
The `cp` command (copy) is the correct way to transfer files to your board.
You can upload multiple files at once by listing them before the colon (`:`), which represents the device’s filesystem root:

```bash
mpremote cp main.py seven_segment.py buzzer_music.py music_options.py :
```

If you want to include the connection inline:

```bash
mpremote connect COM14 cp main.py seven_segment.py buzzer_music.py music_options.py :
```

### Listing files
To check what’s on your board:

```bash
mpremote ls
```

This is shorthand for `mpremote fs ls`.

### Removing files
To delete files from the board:

```bash
mpremote rm old_script.py
```

or explicitly:

```bash
mpremote rm :old_script.py
```

---

## Running and Controlling Your Board

### Run a script directly (without uploading)
Execute a local file on the board:

```bash
mpremote run main.py
```

This runs from RAM — it doesn’t store the file on the board.

### Reset the board
Perform a hardware reset (same as `machine.reset()`):

```bash
mpremote reset
```

If your device has a `main.py` on its filesystem, it will run automatically after reset.

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
