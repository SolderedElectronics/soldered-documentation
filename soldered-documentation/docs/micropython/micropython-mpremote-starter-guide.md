---
slug: /micropython/getting-started-with-mpremote
title: MicroPython - Getting started with mpremote
sidebar_label: Getting started with mpremote
id: micropython-mpremote-starter
hide_title: false
---

## What is mpremote?

[**mpremote**](https://docs.micropython.org/en/latest/reference/mpremote.html) is the official MicroPython **command-line tool** for interacting with MicroPython boards. It allows you to:

- Upload and download files
- Run Python scripts directly
- Access the MicroPython REPL (interactive prompt)
- Manage files on the board (list, delete, etc.)
- Chain commands together for automation

If you're using MicroPython regularly — even for small projects — `mpremote` is an essential tool that helps you skip repetitive steps and focus on coding.

## Installation

Before using `mpremote`, make sure you have Python 3 installed. Then, install the tool using pip:

```bash
pip install mpremote
```

To check that it's available, run:

```bash
mpremote --help
```

This should display a list of available commands.

## Connecting to Your MicroPython Board

The easiest way to connect:

```bash
mpremote connect auto
```

This will automatically find the first connected MicroPython device.

If you want to connect to a specific port, use:

```bash
mpremote connect COM3         # Windows example
mpremote connect /dev/ttyUSB0 # Linux/macOS example
```

## Uploading and Running Files

To **upload a file** (e.g. `main.py`) to the device:

```bash
mpremote fs cp main.py :
```

To **run a script immediately** (without copying it to the device):

```bash
mpremote run myscript.py
```

You can also upload an entire folder of files:

```bash
mpremote fs cp src/ :
```

This will copy all files from the `src/` folder to the board.

## Managing Files on the Board

List all files on the device:

```bash
mpremote fs ls
```

Remove a file from the device:

```bash
mpremote fs rm main.py
```

## Using the MicroPython REPL

The REPL lets you interact with your board directly, line by line. Start it with:

```bash
mpremote repl
```

To exit the REPL safely, press:

- `Ctrl+A` then `Ctrl+D`

This closes the session without disconnecting the device incorrectly.


## Combining Commands

You can chain multiple commands in a single line. For example:

```bash
mpremote connect auto run myscript.py
```

This connects to the board and immediately runs the script.

