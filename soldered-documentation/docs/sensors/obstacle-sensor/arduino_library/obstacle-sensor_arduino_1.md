---
slug: /obstacle-sensor/arduino/geting-started
title: Obstacle Sensor - Getting started
sidebar_label: Getting started
id: obstacle-sensor-arduino-1
hide_title: false
---

## Arduino library 

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Soldered-Obstacle-Sensor-Arduino-Library"  
  description="Library for Qwiic IR Obstacle Sensor board."  
  url="https://github.com/SolderedElectronics/Soldered-Obstacle-Sensor-Arduino-Library"  
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

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox> This board also contains UPDI headers for preprogramming the onboard ATTINY404; they are used only for debugging purposes. </InfoBox>