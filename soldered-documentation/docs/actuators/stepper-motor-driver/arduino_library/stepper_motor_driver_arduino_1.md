---
slug: /stepper-motor-driver/arduino/geting-started
title: Getting started
id: stepper-motor-driver-arduino-1
hide_title: False
---

This page provides the essential information for getting started, including board and library installation and wiring the breakout board to your microcontroller.

---

## Acknowledgement

<InfoBox> The Soldered Basic Stepper Driver Arduino Library is based on the popular [**AccelStepper** library](https://www.airspayce.com/mikem/arduino/AccelStepper/) by [airspayce](https://www.airspayce.com/). As such, its source code is licensed under the **GNU General Public License v3.0 (GPL v3)**. For more details, see the [**GPL v3 license**](https://www.gnu.org/licenses/gpl-3.0.html).</InfoBox>

<CenteredImage src="/img/license/GPL_V3.png" alt="GNU GPL v3" width="150px" />

---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Temperature and humidity sensor SHTC3 breakout Arduino library"  
  description="SHTC3 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-SHTC3-Temperature-Humidity-Sensor-Arduino-Library"  
/>  


<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="#"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CORE**. These pins will be used in the examples throughout this documentation.

<CenteredImage src="/img/stepper-motor-driver/motor-driver-connection.jpeg" alt="Basic stepper driver connected to Dasduino CORE" caption="Basic stepper driver connected to Dasduino CORE" width="600px" />

| **Dasduino CORE** | **Breakout Board** |
|------------------|-------------------|
| D2              | IN 1              |
| D3              | IN 2              |
| D4              | IN 3              |
| D5              | IN 4              |
| GND             | GND (for pulse inputs) |

<InfoBox> Pins **D2, D3, D4, and D5** can be any digital output pins on your microcontroller. </InfoBox>

You also need to connect **VCC** and **GND** on the **stepper power supply terminals**:

| **Power Supply** | **Breakout Board** |
|------------------|-------------------|
| VCC              | VCC               |
| GND              | GND               |

<WarningBox> **14V is the maximum** supported motor supply voltage! </WarningBox>

<WarningBox> If you have the version of this product **with the stepper motor**, the **motor supply voltage must be exactly 5V**! </WarningBox>

<InfoBox> Powering the stepper motor through the **5V VCC pin** on your microcontroller may work **but is not recommended** due to the high current draw of the motor. </InfoBox>