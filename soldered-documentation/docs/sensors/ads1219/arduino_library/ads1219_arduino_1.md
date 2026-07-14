---
slug: /ads1219/arduino/getting-started 
title: ADS1219 24-bit ADC - Getting started
sidebar_label: Getting started
id: ads1219-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink  
  title="ADS1219 24-bit ADC Arduino library"  
  description="ADS1219 24-bit ADC Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-ADS1219-Arduino-Library/tree/main"  
/>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

If your board has a Qwiic connector, connect it directly to the ADS1219 board with a Qwiic cable:

| **Dasduino CONNECTPLUS** | **ADS1219 Board** |
| ------------------------ | ------------------ |
| Qwiic                     | Qwiic               |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS** | **ADS1219 Board** |
| ------------------------ | ------------------ |
| IO21 (Default SDA pin)    | SDA                 |
| IO22 (Default SCL pin)    | SCL                 |
| VCC                       | VCC                 |
| GND                       | GND                 |

</InfoBox>
