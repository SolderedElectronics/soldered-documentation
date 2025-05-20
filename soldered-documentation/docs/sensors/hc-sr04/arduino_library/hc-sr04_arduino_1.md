---
slug: /hc-sr04/arduino/geting-started
title: Hc Sr04 - Getting started
id: hc-sr04-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Ultrasonic sensor with easyC Arduino library"  
  description="Ultrasonic sensor with easyC Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Ultrasonic-Sensor-easyC-Arduino-Library/tree/main"  
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


<WarningBox>UPDI stands for Unified Program and Debug Interface. It is used to program and debug Atmel devices. The Atmel chip on this board is used for the easyC I2C communication only. DO NOT try to use this for sensor communication!</WarningBox>