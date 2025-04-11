---
slug: /tca9548a/arduino/geting-started 
title: Getting started
id: tca9548a-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library for the TCA9548A I2C Multiplexer, you can download it from the GitHub repository:
<QuickLink  
  title="IO expander TCA9548A breakout Arduino library"  
  description="IO expander Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-TCA9548A-I2C-Multiplexer-Arduino-Library"  
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
| SDA                     | SDA                |
| SCL                     | SCL                |
| GND                     | GND                |
| 5V                      | VCC                |


</InfoBox>