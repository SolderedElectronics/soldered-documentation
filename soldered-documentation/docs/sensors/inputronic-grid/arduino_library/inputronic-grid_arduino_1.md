---
slug: /inputronic-grid/arduino/geting-started 
title: Getting started
id: inputronic-grid-arduino-1 
hide_title: False
---
## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Soldered Inputronic GRID Arduino library"  
  description="Arduino Library for the Soldered Inputronic GRID device"  
  url="https://github.com/SolderedElectronics/Soldered-Inputronic-Grid-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **NULA DeepSleep**. These pins will be used in the examples throughout this documentation.

| **NULA DeepSleep** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<ErrorBox>The connection image for this board hasn't been generated yet! We're working on it!</ErrorBox>

<InfoBox>

If you prefer, you can use the soldering pads on the back of the module to manually connect:

| **NULA DeepSleep** | **Breakout Board** |
| ------------------------ | ------------------ |
| IO21 (Default SDA pin)   | SDA                |
| IO22 (Default SCL pin)   | SCL                |
| 3.3V                     | 3V3                |
| GND                      | GND                |

</InfoBox>