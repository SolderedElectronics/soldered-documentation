---
slug: /led-matrix/arduino/geting-started
title: Arduino - Getting started
sidebar_label: Getting started
id: led-matrix-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Soldered-8x8-MAX7219-LED-Matrix-Arduino-Library"  
  description="8x8 Led Matrix board by Soldered using MAX7219 chip"  
  url="https://github.com/SolderedElectronics/Soldered-8x8-MAX7219-LED-Matrix-Arduino-Library"  
/>  


<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections
Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
|---|---|
| IO4 | LOAD |
| IO18 | CLK |
| IO23 | DIN |
| VCC | VCC |
|GND | GND |

<InfoBox>
LOAD pin can be any digital IO  pin on controller, CLK and DIN pins must be default SPI communication pins(SCK for CLK and MOSI for DIN) if no external library such as Wire.h is used!

</InfoBox>


## Connections for daisy chaining

| **First Board** | **Next Board**|
|---|---|
| CLK | CLK |
| LOAD | LOAD |
| DIN | DOUT |
| VCC | VCC |
|GND | GND |
