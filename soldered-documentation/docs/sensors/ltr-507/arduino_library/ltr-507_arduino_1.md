---
slug: /ltr-507/arduino/geting-started 
title: Getting started
id: ltr-507-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="LTR-507 Arduino library"  
  description="Digital Light and Proximity Sensor Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Digital-Light-Sensor-Arduino-Library/tree/main"  
/>  

<WarningBox>Make sure you're using our library! Otherwise it might won't work.</WarningBox>

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

| **Dasduino CONNECTPLUS**     | **Breakout Board** |
| ---------------------------- | ------------------ |
| IO21 (Default SDA pin)       | SDA                |
| IO22 (Default SCL pin)       | SCL                |
| VCC                          | VCC                |
| GND                          | GND                |
| 3V3                          | VLED               |
| IO25 (any digital pin works) | INT                |


</InfoBox>