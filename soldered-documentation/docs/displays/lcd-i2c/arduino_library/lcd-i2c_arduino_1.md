---
slug: /lcd-i2c/arduino/geting-started 
title: Getting started
id: lcd-i2c-arduino-1 
hide_title: False
---

This page provides the essential information for getting started, including board and library installation.

--- 

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink  
  title="Soldered 16x2 LCD I2C Arduino Library"  
  description="16x2 LCD I2C Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="#"  
/>  

</InfoBox>

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **I2C LCD Driver Board** |
| ------------------------ | ------------------------ |
| Qwiic                    | Qwiic                    |

<InfoBox> If you prefer, you can use I2C pins to manually connect. Since this board is an I2C LCD driver, most of the pins are not needed for I2C communication. </InfoBox>

### The Key Pins to Connect

| **Dasduino CONNECTPLUS** | **I2C LCD Driver Board** |
| ------------------------ | ------------------------ |
| IO21 (Default SDA pin)   | SDA                      |
| IO22 (Default SCL pin)   | SCL                      |
| VCC (5V)                 | 5V / A                   |
| GND                      | GND / C                  |

### What About the Other Pins?
Most of the other pins **(D0-D7, E, R/W, RS, VO)** are used for parallel communication with an LCD. However, since this board is an **I2C interface**, these extra pins are **not required**.

### Optional Connections
- **VO (Contrast Control)**: Usually, this is handled internally by the board, but if needed, you might connect it to a potentiometer or a fixed resistor.
- **Backlight Control**: If the board has a **VLED pin**, you might connect it to **3V3** or **5V** from Dasduino to enable the LCD backlight.
