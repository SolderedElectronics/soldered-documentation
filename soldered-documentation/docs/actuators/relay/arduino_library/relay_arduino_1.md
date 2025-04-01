---
slug: /relay/arduino/geting-started 
title: Getting started
id: relay-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Relay board Arduino library"  
  description="Relay board Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Relay-Arduino-Library"  
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

## Connections for regular version
Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
|---|---|
| IO5 | IN |
| 3V3 or 5V | VCC |
| GND | GND |

<InfoBox> Digital version can use any **digital** input pin, Check pinout drawing for your specific board </InfoBox>

---

## Connections for Qwiic version
Below is an example **Qwiic** connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation. To change the circuit board's address, check the [**Address selection**](/documentation/relay/hardware#address-selection-for-qwiic-version).


| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox> Qwiic versions also contain UPDI headers for preprogramming the onboard ATTINY404 MCU, they are used for debugging purposes only! </InfoBox>
