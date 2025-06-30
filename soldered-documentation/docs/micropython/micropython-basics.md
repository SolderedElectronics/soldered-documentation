---
slug: /micropython/overview
title: MicroPython Overview
sidebar_label: MicroPython Overview
id: micropython-basics
hide_title: false
pagination_prev: null
---

<CenteredImage src="/img/soldered_micropython_img.png" alt="Soldered and Micropython logo" />

<br>
</br>

**MicroPython** is a lightweight and efficient implementation of Python 3 designed specifically for microcontrollers and embedded systems.

With MicroPython, your scripts can interact with hardware just like in **Arduino**, **ESP-IDF**, **PlatformIO**, or other embedded platforms you're used to. It's ideal for quickly prototyping, testing components using MicroPython modules, or building complete standalone projects with ease.

Gone are the days of long compile times, heavy board definitions, and clunky development setups. MicroPython brings a streamlined, user-friendly, and modular development experience that enables fast, flexible prototyping and iteration.

On this page, you'll find a quick overview of what MicroPython is.

## Why Use MicroPython?

- Easy to learn and ideal for beginners
- Interactive REPL (Read-Evaluate-Print Loop) for fast testing and debugging
- Lightweight and fast for many embedded applications
- Runs on a wide range of boards: ESP32, Raspberry Pi Pico, STM32, and more

## How MicroPython Works

Unlike standard Python interpreters, MicroPython is optimized to run with minimal hardware resources, making it perfect for microcontrollers.

You write Python code, upload it to your device, and the interpreter runs it, allowing you to control sensors, actuators, displays, and more using familiar Python syntax.

The MicroPython interpreter is part of the **MicroPython firmware**, a precompiled binary that runs on your microcontroller. Your Python scripts are uploaded to the device and executed line-by-line by the interpreter.

There are two main ways to work with MicroPython:

1. Using the `mpremote` command-line tool
2. Using our custom VS Code extension (more details coming soon!)

## Workflow

This graphic illustrates a typical development workflow when using MicroPython:

<CenteredImage src="/img/micropython/micropython_development.png" alt="MicroPython development flow" width="450px" />

### Step-by-Step Breakdown

- **Download MicroPython firmware** from the [official MicroPython website](https://micropython.org/download/). Locate your microcontroller model and download the appropriate `.bin` file.
- **Flash the firmware** to your device by uploading the `.bin` file. This step is similar to uploading an Arduino sketch, but in this case, you're installing the MicroPython runtime, which will interpret your scripts.

<InfoBox>

**You only need to do the first two steps once!**  
Once MicroPython is installed, updating your project is as simple as copying a new `.py` file to the board.

</InfoBox>

- **Write or edit your Python script** (`main.py`), which serves the same purpose as an Arduino `.ino` sketch. You can use any code editor to make changes.
- **Add modules (libraries)** by copying the appropriate `.py` files into a `lib/` directory on the board.
- **Copy your code** to the device using `mpremote`, your IDE, or a file manager.
- **Run your script**: the interpreter will execute your code automatically if it's named `main.py`, or you can run scripts manually via REPL.
- **Check output** through `print()` statements, visible via the serial console (just like regular Python debugging).

This covers the basic workflow. For more details on how to install and use MicroPython modules from Soldered Electronics, check out the next section.

## Learn More

You can explore the official MicroPython project here:  
🔗 [https://micropython.org](https://micropython.org)
