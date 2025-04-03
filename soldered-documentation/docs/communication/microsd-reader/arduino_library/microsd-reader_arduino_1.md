---
slug: /microsd-reader/arduino/geting-started 
title: Getting started
id: microsd-reader-arduino-1 
hide_title: False
---

## Acknowledgement

<InfoBox> The Soldered microSD Card Breakout Arduino library is based on the popular [**SdFat** library](https://github.com/greiman/SdFat) by [Bill Greiman](https://github.com/greiman). As such, its source code is licensed under the **GNU General Public License v3.0 (GPL v3)**. For more details, see the [**GPL v3 license**](https://www.gnu.org/licenses/gpl-3.0.html).</InfoBox>

<CenteredImage src="/img/license/GPL_V3.png" alt="GNU GPL v3" width="150px" />

---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Soldered SdFat Arduino library"  
  description="Sd card communication Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-SdFat-Arduino-Library/tree/master"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to set up and upload code for the first time on an Arduino board, from scratch!"  
  url="#"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| IO5 (Default CS pin)     | CS                 |
| IO23 (Default MOSI pin)   | MOSI               |
| IO19 (Default MISO pin)   | MISO               |
| IO18 (Default CLK pin)    | SCLK               |
| GND                      | GND                |
| 3.3V                     | VCC                |

