---
slug: /hx711/arduino/getting-started
title: "HX711 Load Cell Amplifier \u2013 Arduino getting started"
id: hx711-arduino-1
hide_title: false
---
## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Load cell amplifier HX711 board Arduino library"  
  description="HX711 Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to set up and upload code for the first time on an Arduino board, from scratch!"  
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

| **Dasduino CONNECT**  | **HX711 Breakout Board** |
| --------------------- | ------------------------ |
| VCC                   | VCC                      |
| GND                   | GND                      |
| IO2 (any digital pin) | DT (Data)                |
| IO3 (any digital pin) | SCK (Clock)              |

</InfoBox>

## Connecting the Load cell with the HX711

| **Load Cell Wires** | **HX711 Breakout Board** |
| ------------------- | ------------------------ |
| Red                 | E+                       |
| Black               | E-                       |
| Green               | A-                       |
| White               | A+                       |