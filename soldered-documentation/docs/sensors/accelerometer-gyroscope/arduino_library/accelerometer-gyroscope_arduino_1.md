---
slug: /accelerometer-gyroscope/arduino/geting-started 
title: LSM6DS – Getting started
id: accelerometer-gyroscope-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository (all 3 variants use the same library):
<QuickLink  
  title="Accelerometer & Gyroscope LSM6DS 6-DOF breakout Arduino library"  
  description="Soldered-LSM6DS3-Arduino-Library"  
  url="https://github.com/SolderedElectronics/Soldered-LSM6DS3-Arduino-Library"  
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

<WarningBox> The **IO21** and **IO22** pins can differ for your personally used board, so **make sure to validate** the information before you start working!</WarningBox>
