---
slug: /joystick/arduino/geting-started 
title: Getting started
id: joystick-arduino-1 
hide_title: False
---

## Arduino library
To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<ErrorBox>The Ardino library for this board hasn't been generated yet! We're working on it!</ErrorBox>
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

| **Dasduino CONNECTPLUS** | **Breakout Board** |
|---|---|
| IO13 | POSX |
| IO14 | POSY |
| IO15 | SW |
| VCC | VCC |
|GND | GND |

<InfoBox>
POSX, POSY, pins can be any analog pin on controller, SW can be any digital IO pin on controller.
</InfoBox>