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

<WarningBox>Make sure you're using our library! Generic libraries don't work with our adapter.</WarningBox>

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

## The Key Pins to Connect

| **Dasduino CONNECTPLUS** | **I2C LCD Driver Board** |
| ------------------------ | ------------------------ |
| IO21 (Default SDA pin)   | SDA                      |
| IO22 (Default SCL pin)   | SCL                      |
| VCC (5V)                 | 5V                       |
| GND                      | GND                      |

## What About the Other Pins?
Most of the other pins **(D0-D7, E, R/W, RS, VO)** are used for parallel communication with an LCD. However, since this board is an **I2C interface**, these extra pins **don't require** connecting with Dasduino.


## Adjusting the contrast
If your LCD display appears **blank** or the **characters** are **not visible**, you may need to adjust the **contrast**. This is a common issue when first setting up an LCD with the Dasduino.

On the back of the adapter board, there is a small potentiometer (usually a square component with a tiny screw). Use a small screwdriver to carefully turn it left or right until the characters become visible.

<CenteredImage src="/img/lcd-i2c/contrast_onboard.png" alt="contrast control" caption="Potentiometer on the LCD I2C adapter" width="500px"/>
