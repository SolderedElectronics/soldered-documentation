---
slug: /bmv080/arduino/geting-started 
title: BMV080 Particulate Matter Sensor - Getting Started
sidebar_label: Getting Started
id: bmv080-arduino-1 
hide_title: true
---

<SectionTitle title="BMV080 - Getting Started" backgroundImage="/img/faq.webp" />

## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** or download it directly from GitHub:  

<QuickLink  
  title="BMV080 Particulate Matter Sensor Arduino Library"  
  description="BMV080 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-BMV080-Arduino-Library"  
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

For a quick and seamless connection, use a **Qwiic cable**. Just plug one end of the cable into your Dasduino board and the other into the sensor.

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>

<InfoBox>

Alternatively, you can **manually connect** the sensor using I²C pins:

| **Dasduino CONNECTPLUS**     | **BMV080 Breakout Board** |
| ---------------------------- | ------------------------- |
| IO21 (Default SDA pin)       | SDA                       |
| IO22 (Default SCL pin)       | SCL                       |
| 3V3                          | 3V3                       |
| GND                          | GND                       |
| IO13 (any digital pin works) | IRQ (optional)            |

</InfoBox>