---
slug: /lsm9ds1tr/arduino/getting-started 
title: LSM9DS1TR – Getting started
sidebar_label: Getting started
id: lsm9ds1tr-arduino-1 
hide_title: False
---
# Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Accelerometer & Gyroscope & Magnetometer LSM9DS1TR 9-DOF breakout Arduino library"  
  description="Soldered-LSM9DS1TR-Arduino-Library"  
  url="https://github.com/SolderedElectronics/Soldered-LSM9DS1TR-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

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

<WarningBox> The **IO21** and **IO22** pins may differ for your board, so **make sure to validate** the information before you start working!</WarningBox>