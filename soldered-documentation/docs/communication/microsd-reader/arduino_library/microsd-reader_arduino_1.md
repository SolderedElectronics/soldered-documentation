---
slug: /microsd-reader/arduino/geting-started 
title: Getting started
id: microsd-reader-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Soldered SdFat Arduino library"  
  description="Sd card communication Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-SdFat-Arduino-Library/tree/master"  
/>  

s
<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="#"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| IO5 (Default CS pin)   | CS                 |
| IO23 (Default MOSI pin)  | MOSI                |
| IO19 (Default MISO pin)  | MISO                |
| IO18 (Default CLK pin)   | SCLK                |
| GND                      | GND                 |
| 3.3V                      | VCC                |