---
slug: /gnss-gps/arduino/getting-started 
title: Getting started
id: gnss-gps-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="GNSS GPS L86-M33 board Arduino library"  
  description="GNSS L860-M33 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-GNSS-L86-M33-Arduino-Library/tree/main"  
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

<InfoBox>

If you're using the **regular version**, use these pins to manually connect:

| **Dasduino CONNECTPLUS** | **L86-M33 Board** |
| ------------------------ | ----------------- |
| VCC                      | 5V                |
| GND                      | GND               |
| IO22 (any digital pin)   | TX                |
| IO21 (any digital pin)   | RX                |

For the **optional pins**:

| **Dasduino CONNECTPLUS** | **L86-M33 Board** |
| ------------------------ | ----------------- |
| RESET                    | RST               |
| IO18 (any digital pin)   | F-ON              |
| IO19 (any digital pin)   | PPS               |
| Antenna connector        | ANT-D             |
</InfoBox>