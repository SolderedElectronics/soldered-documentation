---
slug: /bme688/micropython/geting-started 
title: MicroPython -  Getting started
sidebar_label: Getting started
id: bme688-micropython-1 
hide_title: False
---

## MicroPython module

To install the MicroPython module, download it from the GitHub repository:
<QuickLink
    title="Soldered BME688 sensor Breakout  board MicroPython module"
    description="An MicroPython module for the Soldered BME688 sensor Breakout board"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Sensors/BME688/BME688"
/>

<InfoBox>

**First time MicroPython user?** For a detailed tutorial on how to get started with MicroPython, see this section of our docs:

<QuickLink
    title="Getting started with MicroPython"
    description="A comprehensive tutorial on how to set up and upload code for the first time on an MicroPython board from scratch!"
    url="/documentation/micropython/getting-started-with-vscode/"
/>

</InfoBox>

---

## Connections 
Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
|---|---|
|Qwiic|Qwiic|

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS** | **Breakout Board**|
|---|---|
|IO21 (Default SDA pin) | SDA|
|IO22 (Default SCL pin) | SCL |
|VCC|VCC|
|GND|GND|

</InfoBox>