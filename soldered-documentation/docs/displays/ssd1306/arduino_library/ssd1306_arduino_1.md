---
slug: /ssd1306/arduino/geting-started 
title: Getting started
id: ssd1306-arduino-1 
hide_title: False
---

This page provides the essential information for getting started, including board and library installation and wiring the breakout board to your microcontroller.

---

## Arduino library

To install the Arduino library, you can download it from the GitHub repository:
<QuickLink  
  title="OLED Display Arduino library"  
  description="OLED Display Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-OLED-Display-Arduino-Library/tree/main"  
/>  


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