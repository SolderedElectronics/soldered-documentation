---
slug: /ina219/arduino/geting-started 
title: INA219 - Getting started
sidebar_label: Getting started
id: ina219-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Voltage & current sensor INA219 breakout Arduino library"  
  description="Voltage & current sensor INA219 breakout Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-INA219-Current-Sensor-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins are used in the examples throughout this documentation.

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