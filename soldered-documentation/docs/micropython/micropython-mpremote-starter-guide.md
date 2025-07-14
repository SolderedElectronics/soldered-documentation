---  
slug: /micropython/getting-started-with-mpremote  
title: MicroPython - Getting started with mpremote  
sidebar_label: Getting started with mpremote  
id: micropython-mpremote-starter  
hide_title: false  
---

<InfoBox title="Looking for something easier?">If you prefer a graphical interface instead of typing commands, check out the [**Soldered MicroPython Helper extension**](/micropython/getting-started-with-vscode)  for VSCode. A user-friendly extension that handles uploading, running, and viewing output without touching the terminal.</InfoBox>

## What is mpremote?

[**mpremote**](https://docs.micropython.org/en/latest/reference/mpremote.html) is the official MicroPython **command-line tool** for interacting with MicroPython boards. It allows you to:

- Upload and download files  
- Run Python scripts directly  
- Access the MicroPython REPL (interactive prompt)  
- Manage files on the board (list, delete, etc.)  
- Chain commands together for automation

If you're using MicroPython regularly, even for small projects, `mpremote` is an essential tool that helps you skip repetitive steps and focus on coding.

## Installation

Before using `mpremote`, make sure you have Python 3 installed. Then, install the tool using pip:

```bash
pip install mpremote
```

To verify it's working:

```bash
mpremote --help
```

<CenteredImage src="/img/mp-vsc-ext/cmd-help.png" width="500px" alt="cmdhelpoutput" caption="Expected output when using the --help command."/>

## Connecting to Your MicroPython Board

The easiest way to connect:

```bash
mpremote connect auto
```

This will automatically find the first connected MicroPython device.

To specify the port manually:

```bash
mpremote connect COM3         # Windows
mpremote connect /dev/ttyUSB0 # Linux/macOS
```

<CenteredImage src="/img/mp-vsc-ext/cmd-connect-auto.png" width="500px" caption="Expected output when using connect auto."/>

## Uploading and Running Files

To **upload a file** (e.g. `main.py`) to your board:

```bash
mpremote fs cp main.py :
```

To **run a script directly** (without saving it):

```bash
mpremote run myscript.py
```

Upload a full folder of files:

```bash
mpremote fs cp src/ :
```

## Managing Files on the Board

List files on the device:

```bash
mpremote fs ls
```

Delete a file from the device:

```bash
mpremote fs rm main.py
```

## Using the MicroPython REPL

The REPL allows interactive access to your device:

```bash
mpremote repl
```

To exit safely, press:

```
Ctrl+A, then Ctrl+D
```

## Combining Commands

You can chain commands in one line:

```bash
mpremote connect auto run myscript.py
```

This will connect and immediately execute the script.

<CenteredImage src="/img/mp-vsc-ext/cmd-combining-commands.png" width="700px" caption="Using combined commands to connect to our device and run a sketch."/>