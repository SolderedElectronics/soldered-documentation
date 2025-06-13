---  
slug: /apds-9960/arduino/geting-started  
title: Apds-9960 – Getting started
id: apds-9960-arduino-1  
hide_title: False  
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:  
<QuickLink  
  title="APDS-9960 Color and Gesture Sensor breakout Arduino library"  
  description="APDS-9960 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-APDS9960-Light-Gesture-Color-Sensor-Arduino-Library/tree/main"  
/>  

<InfoBox>

**Are you a first-time Arduino user?** For a detailed tutorial on getting started with Arduino, refer to this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive tutorial on how to set up and upload code to an Arduino board for the first time, from scratch!"  
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

If you prefer, you can manually connect using I2C pins:

| **Dasduino CONNECTPLUS**     | **Breakout Board** |
| ---------------------------- | ------------------ |
| IO21 (Default SDA pin)       | SDA                |
| IO22 (Default SCL pin)       | SCL                |
| VCC                          | VCC                |
| GND                          | GND                |
| IO25 (any digital pin works) | INT                |

<WarningBox>The VLED pin is used for power to the IR LED if the **JP3** jumper is open.</WarningBox>

| **Dasduino CONNECTPLUS**     | **Breakout Board** |
| ---------------------------- | ------------------ |
| 3V3                          | VLED               |

</InfoBox>