---
slug: /i2s-audio-amplifier/arduino/geting-started 
title: Stereo I2S Audio Amplifier - Getting started
sidebar_label: Getting started
id: i2s-audio-amplifier-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Stereo I2S Audio Amplifier Arduino library"  
  description="Stereo I2S Audio Amplifier library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-I2S-Audio-Amplifier-Arduino-Library"  
/>  

<WarningBox>
**This library only works on multi-core chips like ESP32, ESP32-S3 and ESP32-P4. Your board must have PSRAM! It does not work on the ESP32-S2, ESP32-C3 etc.**
</WarningBox>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **I2S Audio Amplifier board** |
| ------------------------ | ----------------------------- |
| VCC                      | VCC                           |
| IO27                     | BCLK                          |
| IO25                     | DIN                           |
| IO26                     | LRCLK                         |
| GND                      | GND                           |

<CenteredImage src="/img/under_construction.png" alt="Connection image" width="700px"/>