---
slug: /inputronic-keyboard/micropython/getting-started 
title: Inputronic Keyboard - Getting started
sidebar_label: Getting started
id: inputronic-keyboard-micropython-1 
hide_title: False
---

## MicroPython module

To install the MicroPython module, download it from the GitHub repository:
<QuickLink
    title="Soldered Inputronic Keyboard MicroPython module"
    description="A MicroPython module for the Soldered Inputronic Keyboard"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Communication/Inputronic-KEYBOARD"
/>

<InfoBox>

**First time MicroPython user?** For a detailed tutorial on how to get started with MicroPython, see this section of our docs:

<QuickLink
    title="Getting started with MicroPython"
    description="A comprehensive tutorial on how to set up and upload code for the first time on a MicroPython board from scratch!"
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

If you prefer, you can use I²C pins to manually connect:

| **Dasduino CONNECTPLUS** | **Breakout Board**|
|---|---|
|IO21 (Default SDA pin) | SDA|
|IO22 (Default SCL pin) | SCL |
|3V3|3V3|
|GND|GND|

</InfoBox>