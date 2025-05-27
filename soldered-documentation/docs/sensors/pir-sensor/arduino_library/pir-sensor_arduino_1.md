---
slug: /pir-sensor/arduino/geting-started
title: "PIR Movement sensor \u2013 Arduino Getting Started"
id: pir-sensor-arduino-1
hide_title: false
---
## Arduino library

To install the Arduino library for the Qwiic version, you can download it from the GitHub repository:

<QuickLink  
  title="PIR movement sensor with easyC Arduino library"  
  description="PIR sensor Qwiic Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-PIR-movement-seonor-with-easyC-Arduino-Library/tree/main"  
/>  

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

### Standard version

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| VCC                      | VCC                |
| IO4                      | DOUT               |
| IO2                      | SOUT               |
| GND                      | GND                |

### Qwiic version

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<WarningBox>UPDI stands for Unified Program and Debug Interface. It is used to program and debug Atmel devices. The Atmel chip on this board is used solely for easyC I2C communication. DO NOT try to use this for sensor communication!</WarningBox>