---
slug: /gnss-gps/arduino/getting-started
title: Gnss Gps - Getting started
sidebar_label: Getting started
id: gnss-gps-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="GNSS GPS L86-M33 board Arduino library"  
  description="GNSS L86-M33 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-GNSS-L86-M33-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Nula Mini**. These pins will be used in the examples throughout this documentation.

| **Nula Mini**         | **L86-M33 Board** |
| --------------------- | ----------------- |
| VCC                   | 5V                |
| GND                   | GND               |
| IO4 (any digital pin) | TX                |
| IO3 (any digital pin) | RX                |

For the **optional pins**:

| **Nula Mini**         | **L86-M33 Board** |
| --------------------- | ----------------- |
| IO18 (any digital pin) | F-ON             |
| IO19 (any digital pin) | PPS              |
| Antenna connector      | ANT-D            |

<InfoBox>Nula Mini does not expose a dedicated RST pin. Leave the module RST pin unconnected unless you need hardware reset - the module can be reset via software commands instead.</InfoBox>