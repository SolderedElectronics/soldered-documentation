---
slug: /mcp23017/arduino/blinking-led-example
title: Mcp23017 - Blinking LED example
id: mcp23017-arduino-2
hide_title: false
---

This page contains an example for setting up a blinking LED via the I/O extender.

---

## Connections for this example

<CenteredImage src="/img/mcp23017/led_connection.png" width="100%" />

---

## Full example

In this example, we first include the library and create an instance of the board. Next, in the `setup()` function, we initialize the I2C communication with the I/O expander and set the pin mode for the GPA0 pin (we are using this pin for the LED). Finally, in the `loop()` function, we change the pin output every second:

```cpp
// Include the board file
#include "MCP23017-SOLDERED.h"

// Create an instance of the board object
MCP_23017 mcp;

void setup()
{
    // Initialize the board
    mcp.begin();

    // Set the pin to output
    mcp.pinMode(GPA0, OUTPUT);
}

void loop()
{
    // Blink the pin
    mcp.digitalWrite(GPA0, HIGH);
    delay(1000);

    // Turn off the pin
    mcp.digitalWrite(GPA0, LOW);
    delay(1000);
}
```

<FunctionDocumentation
  functionName="mcp.begin()"
  description="Initializes the I/O extender via I2C"
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="mcp.pinMode(uint8_t pin, uint8_t mode)"
  description="Controls a single pin's direction"
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'pin', description: "pin number" },
    { type: 'uint8_t', name: 'mode', description: "OUTPUT, INPUT or INPUT_PULLUP" },
  ]}
/>

<FunctionDocumentation
  functionName="mcp.digitalWrite(uint8_t pin, uint8_t state)"
  description="Sets the state for a specific pin"
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'pin', description: "pin number" },
    { type: 'uint8_t', name: 'state', description: "state in which to put the pin" },
  ]}
/>