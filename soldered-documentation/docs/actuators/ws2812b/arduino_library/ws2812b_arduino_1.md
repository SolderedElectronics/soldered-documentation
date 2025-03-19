---
slug: /ws2812b/arduino/geting-started 
title: Getting started
id: ws2812b-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Smart LEDs Arduino library"  
  description="Smart Leds Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-WS2812-Smart-Leds-Arduino-Library/tree/main"  
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

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECT**  | **Smart LED WS2812B** |
| --------------------- | --------------------- |
| VCC (3.3V)            | VCC                   |
| GND                   | GND                   |
| IO2 (any digital pin) | DIN                   |

<InfoBox>The DOUT pin on a WS2812B LED strip is used to pass the data signal to the next LED or another strip in a daisy-chain configuration.</InfoBox>