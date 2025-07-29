---
slug: /mq/arduino/geting-started 
title: MQ Gas Sensors – Getting started
sidebar_label: Getting started
id: mq-arduino-1 
hide_title: False
---

This page provides the essential information for getting started, including board and library installation and connecting the breakout board to your microcontroller.

---

## Acknowledgement

<InfoBox> The MQ Gas Sensor Arduino library is based on the [**MQSensorsLib** library](https://github.com/miguel5612/MQSensorsLib) by [Miguel Angel Califa Urquiza](https://github.com/miguel5612). As such, its source code is licensed under the **MIT License**. For more details, see the [**MIT License**](https://opensource.org/license/mit).</InfoBox>

<CenteredImage src="/img/license/MIT.png" alt="BSD license" width="250px" />

---

## Arduino library

To install the Arduino library, download it from the GitHub repository:
<QuickLink  
  title="MQX Gas Sensor Arduino library"  
  description="MQ Gas Sensor Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, refer to this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

### Qwiic

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<WarningBox>UPDI stands for Unified Program and Debug Interface. It is used to program and debug Atmel devices. The Atmel chip on this board is used exclusively for easyC I2C communication. DO NOT try to use this for sensor communication!</WarningBox>

### Native

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| VCC                      | 5V                 |
| IO4                      | DO                 |
| IO13                     | AO                 |
| GND                      | GND                |