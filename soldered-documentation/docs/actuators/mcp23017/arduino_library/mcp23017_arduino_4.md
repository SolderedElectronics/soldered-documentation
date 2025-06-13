---
slug: /mcp23017/arduino/button-input-example
title: Mcp23017 - Button input example
sidebar_label: Button input example
id: mcp23017-arduino-4
hide_title: false
---

This page contains an example of reading input from a button.

---

## Connections for this example

<CenteredImage src="/img/mcp23017/button_connection.png" width="100%" />

---

## Full example

In this example, we first include the library and create an instance of the board. Next, in the `setup()` function, we initialize the I2C communication with the I/O expander and set the pin mode for the GPB0 pin (which is used for the button). Finally, in the `loop()` function, we read the pin and print the status of the button to the Serial monitor:

```cpp
#include "MCP23017-SOLDERED.h"

MCP_23017 mcp;

void setup()
{
    // Initialize MCP23017
    mcp.begin();

    // Initialize serial communication
    Serial.begin(115200);

    // Set up the buttons
    mcp.pinMode(GPB0, INPUT_PULLUP);
}

void loop()
{
    // Read the button
    if (mcp.digitalRead(GPB0) == LOW)
    {
        // Button is pressed
        Serial.println("Button is pressed");
    }
    else
    {
        // Button is not pressed
        Serial.println("Button is not pressed");
    }

    delay(1000);
}
```

<CenteredImage src="/img/mcp23017/button.png" alt="Button state on serial monitor" caption="Button state on serial monitor" width="100%" />

<FunctionDocumentation
  functionName="mcp.begin()"
  description="Initializes the I/O extender via I2C"
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="mcp.pinMode(uint8_t pin, uint8_t mode)"
  description="Controls a single pin direction"
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'pin', description: "pin number" },
    { type: 'uint8_t', name: 'mode', description: "OUTPUT, INPUT, or INPUT_PULLUP" },
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

<FunctionDocumentation
  functionName="mcp.digitalRead(uint8_t pin)"
  description="Gets the state of a specific pin"
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'pin', description: "pin number" },
  ]}
/>