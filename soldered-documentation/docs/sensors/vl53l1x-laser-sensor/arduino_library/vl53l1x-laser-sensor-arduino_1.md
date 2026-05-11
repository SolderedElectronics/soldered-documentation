---
slug: /vl53l1x-laser-sensor/arduino/getting-started 
title: VL53L1X ToF Laser Distance Sensor - Getting started (Arduino)
sidebar_label: Getting started
id: laser-distance-sensor-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="VL53L1X Laser Distance Sensor Arduino Library"  
  description="Laser Distance Sensor Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-VL53L1X-Laser-Distance-Sensor-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>


## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.


### Qwiic

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

### Native

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| VCC / 3V3                | VCC                |
| IO21                     | SDA                |
| IO22                     | SCL                |
| GND                      | GND                |