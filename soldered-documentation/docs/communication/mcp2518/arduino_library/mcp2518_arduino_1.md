---
slug: /mcp2518/arduino/geting-started 
title: Getting started
id: mcp2518-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Ardino library manager** or download it from the GitHub repository:
<QuickLink  
  title="CAN Transceiver MCP2518 board Arduino library"  
  description="CAN Bus Breakout with MCP2518 Soldered Arduino Library"  
  url="https://github.com/SolderedElectronics/Soldered-CAN-Bus-Breakout-MCP2518-Arduino-Library"  
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

Below is an example connection diagram for **Dasduino CORE**. These pins will be used in the examples throughout this documentation.

| **Dasduino CORE** 	| **Breakout Board** 	|
|---	|---	|
| D10 (or any GPIO pin) 	| NCS 	|
| D11 (MOSI pin) 	| SDI 	|
| D12 (MISO pin) 	| SDO 	|
| D13 (SPI CLK pin) 	| SCK 	|
| GND 	| GND 	|
| VCC 	| VCC 	|