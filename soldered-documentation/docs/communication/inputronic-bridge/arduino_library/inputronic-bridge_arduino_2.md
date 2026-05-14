---
slug: /inputronic-bridge/arduino/examples 
title: Inputronic BRIDGE - Arduino example
sidebar_label: Arduino example
id: inputronic-bridge-arduino-2 
hide_title: False
---
This page contains a simple example of how to poll and read standard USB events (like Keyboard and Mouse inputs) from the **Inputronic BRIDGE** using the I2C protocol.

---

## Connections for this example

For this example, we will use the easiest connection method: connecting the board via the Qwiic system to the **Nula DeepSleep**. Make sure the onboard protocol jumpers (**JP3 & JP4**) are left open, as this defaults the board to I2C communication.

---

## Full example

In this example, we first include the necessary library and create an instance of the `InputronicParser`. Inside `setup()`, we initialize the I2C bus and attempt to connect to the BRIDGE. In the `loop()`, we continuously poll the module for new events and print the parsed keyboard characters and mouse movements to the Serial Monitor.

```cpp
#include "Inputronic-BRIDGE.h"

InputronicParser parser;

void setup()
{
    Serial.begin(115200);

    // Initialize the I2C bus (using standard pins)
    Wire.begin();
    
    // Configure parser for the default I2C address
    parser.configureI2c(0x50); 

    // Begin communication over I2C
    if (!parser.begin(InputronicParser::PROTOCOL_I2C, Wire))
    {
        Serial.println("Could not connect to BRIDGE over I2C!");
        while (true);
    }

    Serial.println("BRIDGE connected. Waiting for inputs...");
}

void loop()
{
    // Poll the bridge for new data
    auto events = parser.pollEvents();

    // Check if a valid keyboard event occurred
    if (events.keyboard.valid)
    {
        Serial.print("Keyboard: ");
        for (uint8_t i = 0; i < events.keyboard.keyCount; i++)
        {
            Serial.print(events.keyboard.keys[i]);
        }
        Serial.println();
    }

    // Check if a valid mouse event occurred
    if (events.mouse.valid)
    {
        Serial.printf("Mouse X:%d Y:%d L:%d R:%d\n",
                      events.mouse.x, events.mouse.y,
                      events.mouse.btnLeft, events.mouse.btnRight);
    }

    delay(10); // Small delay to prevent spamming the bus
}
```
<FunctionDocumentation
functionName="parser.begin(CommProtocol p, TwoWire &wire)"
description="Initializes the Inputronic BRIDGE parser and establishes communication."
returnDescription="Returns true if initialization is successful, false otherwise."
parameters={[
{ type: 'CommProtocol', name: 'p', description: "The communication protocol to use (e.g., PROTOCOL_I2C, PROTOCOL_UART, PROTOCOL_SPI)." },
{ type: 'TwoWire &', name: 'wire', description: "Reference to the communication bus object (e.g., Wire, Serial1, SPI)." }
]}
/>

<FunctionDocumentation
functionName="parser.configureI2c(uint8_t address)"
description="Sets the I2C address for the BRIDGE module. Should be called before begin()."
returnDescription="None"
parameters={[
{ type: 'uint8_t', name: 'address', description: "The I2C address of the board (default is 0x50)." }
]}
/>

<FunctionDocumentation
functionName="parser.onDataReady(void (*callback)())"
description="Registers a user callback function to be executed when the INT pin triggers in interrupt-driven mode."
returnDescription="None"
parameters={[
{ type: 'void (*callback)()', name: 'callback', description: "The function to call when an interrupt is fired." }
]}
/>