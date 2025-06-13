---
slug: /simple-sensor/simple-light-sensor/arduino_library/geting-started
title: Simple Light Sensor - Geting started
sidebar_label: Geting started
id: simple-light-sensor-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Simple light sensor Arduino library"  
  description="Simple light sensor Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Simple-Light-Sensor-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

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
| IO14 (Any ADC pin)       | A0                 |
| IO15 (Any Digital pin)   | D0                 |
| VCC                      | 5V                 |
| GND                      | GND                |

<InfoBox> Digital version can use any **digital** input pin while analog can use any **analog** pin input, Check Pinout drawing for your specific board </InfoBox>

---

## Connections (Qwiic)
Below is an example **Qwiic (I2C)** connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation. To change breakout board's address, check the [**Address selection**](/documentation/simple-sensor/simple-light-sensor/simple-light-sensor-hardware#address-selection-for-qwiic-version).

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox> Qwiic versions also contain UPDI headers for preprogramming the onboard ATTINY404 MCU, they are used for debugging purposes only! </InfoBox>