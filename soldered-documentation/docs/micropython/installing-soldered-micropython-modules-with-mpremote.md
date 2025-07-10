---
slug: /micropython/installing-soldered-micropython-modules
title: Installing Soldered MicroPython Modules
sidebar_label: Installing Soldered MicroPython Modules
id: micropython-install
hide_title: false
---

**Soldered MicroPython Modules** is an open-source library of MicroPython drivers developed and maintained by Soldered for our range of DIY electronics modules, sensors, and development boards. The goal is to make it easy for makers, educators, and engineers to get started quickly with Soldered hardware using MicroPython—whether for prototyping, classroom learning, or embedded projects.

<QuickLink 
  title="Soldered MicroPython Modules Repository" 
  description="All available MicroPython Modules for Soldered products"
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules" 
/>

Each module in the library is designed to be lightweight, readable, and compatible with a wide range of MicroPython-compatible microcontrollers.

## Installation
You can install a specific module using mpremote or manually downloading specific files onto the board using an IDE such as [**Thonny**](https://thonny.org/)

### Installing using mpremote (recommended)
First, see the following tutorial to install the mpremote package:
<QuickLink 
  title="Installing mpremote" 
  description="Official tutorial from MicroPython docs"
  url="https://docs.micropython.org/en/latest/reference/mpremote.html" 
/>

After mpremote is installed, you will be able to flash a module to the board using the following command:

```sh
  mpremote mip install github:SolderedElectronics/Soldered-Micropython-modules/CATEGORY/ENTER-MODULE-HERE
```
Or, if you're running a Windows OS:

```sh
  python -m mpremote mip install github:SolderedElectronics/Soldered-Micropython-modules/CATEGORY/ENTER-MODULE-HERE
```

For example, downloading the BME280 module looks like this:

```sh
  mpremote mip install github:SolderedElectronics/Soldered-Micropython-modules/Sensors/BME280
```

The module can now be imported and used on your board:
```python
from bme280 import BME280
```

### Installing using Thonny

1. **Connect your board** to your computer via USB.
2. Open **Thonny**, and make sure the correct interpreter is selected:
   - Go to **Tools > Options > Interpreter**
   - Select "MicroPython (Raspberry Pi Pico / ESP32 / etc.)"
   - Choose the correct port and click **OK**
3. Open the `modules/` folder from this library on your computer.
4. For each module you want to use:
   - Open the `.py` file (e.g., `shtc3.py`) in Thonny
   - Go to **File > Save As...**
   - Choose **MicroPython device**
   - Save the file inside the `/lib/` directory on the device (create it if it doesn’t exist)
5. Once the modules are on your board, you can import them in your MicroPython scripts like any other module: 
```python
from bme280 import BME280
```
**Note:** When manually installing the modules you must also manually install any dependancies a module might use, those can be found in the package.json file in any module folder:

```json
"deps": [
    ["github:SolderedElectronics/Soldered-Micropython-modules/Qwiic/Qwiic.py", "main"]
  ],
```
