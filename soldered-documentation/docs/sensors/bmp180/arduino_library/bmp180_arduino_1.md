---
slug: /bmp180/arduino/geting-started
title: Bmp180 - Getting started
sidebar_label: Getting started
id: bmp180-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, download it from the GitHub repository:
<QuickLink  
  title="Pressure & temperature sensor BMP180 breakout Arduino library"  
  description="BMP180 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-BMP180-Temperature-Pressure-Sensor-Arduino-Library"  
/>  


<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

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