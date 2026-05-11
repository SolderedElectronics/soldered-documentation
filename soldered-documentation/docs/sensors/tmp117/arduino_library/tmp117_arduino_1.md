---
slug: /tmp117/arduino/getting-started
title: TMP117 Temperature Sensor Getting started
sidebar_label: Getting started
id: tmp117-arduino-1
hide_title: true
---

# Getting started

## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** or download it directly from GitHub:  

<QuickLink  
  title="TMP117 High-Accuracy Temperature Sensor Arduino Library"  
  description="TMP117 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Temperature-Sensor-TMP117-Arduino-Library/tree/main"  
/>  

<InfoBox>

**Are you a first-time Arduino user?** For a detailed tutorial on getting started with Arduino, refer to this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive tutorial on how to set up and upload code to an Arduino board for the first time, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS** using the Qwiic connector. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **TMP117 Breakout Board** |
| ------------------------- | ------------------------- |
| Qwiic                     | Qwiic                     |

<InfoBox>

If you prefer, you can manually connect using I²C pins:

| **Dasduino CONNECTPLUS**     | **TMP117 Breakout Board** |
| ---------------------------- | ------------------------- |
| IO21 (Default SDA pin)       | SDA                       |
| IO22 (Default SCL pin)       | SCL                       |
| 3V3                          | VCC                       |
| GND                          | GND                       |
| IO25 (any digital pin works) | ALERT (optional)          |

</InfoBox>