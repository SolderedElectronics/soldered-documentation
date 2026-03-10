---
slug: /mcp2518/arduino/geting-started 
title: CAN Transciever MCP2518 - Getting started and Initialization
id: mcp2518-arduino-1
sidebar_label: Getting started and Initialization
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

<InfoBox>In the following examples, we will be using **TWO** **MCP2518** modules, they will be connected as follows:</InfoBox>

| **First MCP2518** | **Second MCP2518**|
|---  |---  |
| CANH | CANH |
| CANL | CANL |

---


## Initialization

To start using the **MCP2518 CAN**, you need to include the approperiate libraries, define the **SPI Chip select** pin, create an instance of CANBus object, and initialize it within the `setup()` function. This ensures proper communication between the Arduino and The MCP2518 module.

```cpp 
#include "CANBus-SOLDERED.h"
#include <SPI.h>

const int SPI_CS_PIN =10;

CANBus CAN(SPI_CS_PIN);

void setup(){
  while(0!=CAN.begin(CAN_125K_500K)){

  }
}
```

<FunctionDocumentation
  functionName="CAN.begin()"
  description="This function initialises CAN and set speed."
  returnDescription="Number"
  returnType="int"
  parameters={[
    { type: 'unt32_t', name: 'speedset', description: 'Data transmision rate.' },
    { type: 'const byte', name: 'clockset', description: 'Frequency set.' },
  ]}
/>