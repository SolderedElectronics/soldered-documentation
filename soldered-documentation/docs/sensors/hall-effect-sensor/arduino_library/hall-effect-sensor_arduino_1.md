---
slug: /hall-effect-sensor/arduino/geting-started
title: "Hall Effect Sensor \u2013 Arduino Getting Started"
id: hall-effect-sensor-arduino-1
hide_title: false
---
## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Hall effect sensor Arduino library"  
  description="Hall effect sensor Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library"  
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

## Connections (regular version)
Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
|---|---|
| IO5 for digital / IO12 for analog | OUT |
| 3V3 | VCC |
| GND | GND |

<InfoBox> Digital version can use any **digital** input pin while analog can use any **analog** pin input, Check Pinout drawing for your specific board </InfoBox>

---

## Connections (Qwiic)
Below is an example **Qwiic (I2C)** connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation. To change the breakout board's address, check the [**Address selection**](/documentation/hall-effect-sensor/hardware#address-selection/).

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox> Qwiic versions also contain UPDI headers for preprogramming the onboard ATTINY404 MCU, they are used for debugging purposes only!. </InfoBox>

