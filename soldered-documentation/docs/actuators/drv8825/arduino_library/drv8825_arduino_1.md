---
slug: /drv8825/arduino/geting-started 
title: DRV8825 - Getting started
id: drv8825-arduino-1 
sidebar_label: Getting started
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
  title="Soldered-Basic-Stepper-Driver-Arduino-Library"  
  description="Stepper driver Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Basic-Stepper-Driver-Arduino-Library"  
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
Below is an example connection diagram for **Dasduino CONNECTPLUS** and **NEMA17 Stepper motor**. These pins will be used in the examples throughout this documentation.

<CenteredImage src="/img/drv8825/drv8825_connection.png" alt="DRV8825 stepper driver connected to Dasduino CONNECTPLUS" caption="DRV8825 stepper driver connected to Dasduino CONNECTPLUS" width="950px" />

| **Dasduino CONNECTPLUS** 	| **Breakout board** 	|
|---	|---	|
| GND 	| GND 	|
| VCC 	| RST 	|
| VCC 	| SLP 	|
| IO5 	| STEP 	|
| IO4 	| DIR 	|

<InfoBox> Pins **IO4, IO5** can be any digital output pins on your microcontroller. </InfoBox>

You also need to connect **VIN** and **GND** on the **stepper power supply terminals**:

| **Power Supply** | **Breakout Board** |
|------------------|-------------------|
| VCC              | VCC               |
| GND              | GND               |

<WarningBox> **12V is the maximum** supported motor supply voltage! </WarningBox>


<InfoBox> Powering the stepper motor through the **5V VCC pin** on your microcontroller may work **but is not recommended** due to the high current draw of the motor. </InfoBox>

## Limiting the current
Before running the motor, maximum current flowing through the stepper coils must be limited so that it doesn't exceed the motor's rated current. The DRV8825 driver includes a small onboard potentiometer for setting the current limit. The easiest way to limit the current is to use the Vref formula: **Vref=Current Limit/2**. Rated current for NEMA17 is 350mA, so the Vref should be 0.175V.

<CenteredImage src="/img/drv8825/drv8825_current_limit.png" alt="Limiting the current onDRV8825 stepper driver" caption="Limiting the current onDRV8825 stepper driver" width="950px" />

<InfoBox> It's not mandatory to use Vref of 0.175V. Depending on the application, if more torque is needed, Vref can be increased! </InfoBox>