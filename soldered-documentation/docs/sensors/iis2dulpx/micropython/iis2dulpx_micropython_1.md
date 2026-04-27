---
slug: /iis2dulpx/micropython/geting-started
title: Getting started
sidebar_label: Getting started
id: iis2dulpx-micropython-1
hide_title: False
---

## MicroPython module

To install the MicroPython module, download it from the GitHub repository:

<QuickLink
  title="IIS2DULPX Accelerometer breakout MicroPython module"
  description="A MicroPython module for the Soldered IIS2DULPX Accelerometer breakout board"
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Sensors/IIS2DULPX"
/>

<InfoBox>

**First time MicroPython user?** For a detailed tutorial on how to get started with MicroPython, see this section of our docs:

<QuickLink
  title="Getting started with MicroPython"
  description="A comprehensive tutorial on how to set up and upload code for the first time on a MicroPython board, from scratch!"
  url="/micropython/getting-started-with-vscode/"
/>

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| IO21 (Default SDA pin)   | SDA                |
| IO22 (Default SCL pin)   | SCL                |
| VCC                      | VCC                |
| GND                      | GND                |

</InfoBox>

<WarningBox>The **IO21** and **IO22** pins can differ for your personally used board, so **make sure to validate** the information before you start working!</WarningBox>

If you also want to use interrupt-based features (wake-up, tap detection, etc.), connect one of the interrupt pins:

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Any digital input pin    | INT1 or INT2       |
