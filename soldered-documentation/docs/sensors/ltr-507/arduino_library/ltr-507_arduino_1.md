---
slug: /ltr-507/arduino/getting-started 
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

<InfoBox>

**First-time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive and detailed tutorial on how to set up and upload code to an Arduino board for the first time from scratch!"  
  url="#"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **LTR-507** |
| ------------------------ | ----------- |
| Qwiic                    | Qwiic       |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS**     | **LTR-507** |
| ---------------------------- | ----------- |
| IO21 (Default SDA pin)       | SDA         |
| IO22 (Default SCL pin)       | SCL         |
| VCC                          | VCC         |
| GND                          | GND         |
| 3V3                          | VLED        |
| IO25 (any digital pin works) | INT         |

<WarningBox>An IR LED must be connected! Ensure proper wiring for the IR LED as shown below for the proximity sensor to work.</WarningBox>

| **LTR-507** | **IR LED**  |
| ----------- | ----------- |
| VLED        | CATHODE (-) |
| VCC         | ANODE (+)   |


<WarningBox>Interrupt functionality is not yet implemented.</WarningBox>

</InfoBox>