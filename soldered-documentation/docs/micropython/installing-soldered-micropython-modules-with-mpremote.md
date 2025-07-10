---  
slug: /micropython/installing-soldered-micropython-modules  
title: Installing Soldered MicroPython Modules  
sidebar_label: Installing Soldered MicroPython Modules  
id: micropython-install  
hide_title: false  
---

**Soldered MicroPython Modules** is an open-source collection of MicroPython drivers for various Soldered products, including sensors, displays, and input devices. These libraries are written to be lightweight, beginner-friendly, and compatible with most MicroPython boards.

<QuickLink 
  title="Soldered MicroPython Modules Repository" 
  description="All available MicroPython Modules for Soldered products"
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules" 
/>

This guide shows how to install the modules using two recommended approaches:

- With the [**Soldered MicroPython Helper**](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper) extension for VS Code
- Using the [**mpremote CLI**](https://docs.micropython.org/en/latest/reference/mpremote.html) tool 

## Option 1: Installing Modules via VS Code Extension

If you're using the **Soldered MicroPython Helper** extension in Visual Studio Code, installing modules is seamless:

1. Open the **Fetch Soldered MicroPython Module** section in the extension sidebar.
2. Search for the module name or keyword (e.g., `bme280`, `shtc3`, `lcd`).
3. Choose whether to download:
   - Only the `.py` driver
   - Example files
   - Or both
4. The selected files will be uploaded directly to your development board.

<CenteredImage src="/img/mp-vsc-ext/soldered-modules.png" width="400px" alt="Soldered Modules" caption="Fetch Soldered MicroPython Module section."/>

<InfoBox>Once uploaded, you can use the modules in your scripts just like any other MicroPython module:</InfoBox>

```python
from shtc3 import SHTC3
```

## Option 2: Installing Modules with `mpremote`

You can also install modules using the official `mpremote` tool and the MicroPython package installer (`mip`).

### 1. Install mpremote

Follow the guide on our [**Getting started with mpremote**](/micropython/getting-started-with-mpremote/) page.

Or install it directly:

```bash
pip install mpremote
```

### 2. Install the desired module

Use the following command format:

```bash
mpremote mip install github:SolderedElectronics/Soldered-Micropython-modules/CATEGORY/MODULE_NAME
```

For example:

```bash
mpremote mip install github:SolderedElectronics/Soldered-Micropython-modules/Sensors/BME280
```

<CenteredImage src="/img/mp-vsc-ext/cmd-mpremote-modules.png" width="800px" caption="Installing the BME280 library and examples driectly from github." />


### 3. Import and use the module

```python
from bme280 import BME280
```

### 4. Dependencies

If a module uses additional dependencies, those must be installed manually. Check the `package.json` in the module folder on GitHub for any listed dependencies:

```json
"deps": [
  ["github:SolderedElectronics/Soldered-Micropython-modules/Qwiic/Qwiic.py", "main"]
]
```

Repeat the same `mpremote mip install ...` process for each listed dependency.

## Manual Installation (Alternative via Thonny)

If you're using **Thonny** or another basic IDE, you can also install modules manually:

1. Open the `.py` module file in Thonny.
2. Save it to your board via: **File → Save As... → MicroPython device**
3. Save the file inside a `lib/` folder on the board (create if needed).
4. Repeat this for any dependencies.
5. Then import it normally:

```python
from shtc3 import SHTC3
```