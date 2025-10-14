---
slug: /ad8495/micropython/getting-started
title: Thermocouple sensor AD8495 - Getting started (MicroPython)
sidebar_label: Getting started
id: ad8495-micropython-1
hide_title: False
---

## MicroPython module

To install the MicroPython module, download it from the GitHub repository:
<QuickLink  
  title="Soldered Thermocouple Sensor AD8495 Breakout MicroPython module"  
  description="An MicroPython module for the Soldered Thermocouple sensor AD8495 Breakout"  
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/Sensors/AD8495/AD8495/ad8495.py"  
/>

<InfoBox>

**First time MicroPython user?**  For a detailed tutorial on how to get started with MicroPython, see this section of our docs:

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
| ------------------------ | ------------------ |
| 3v3                      | VCC                |
| GND                      | GND                |
| 32                       | OUT                |