---
slug: /pcal6416a/arduino/initialization
title: PCAL6416A - Initialization
sidebar_label: Initialization
id: pcal6416a-arduino-2 
hide_title: false
---


This page contains a simple example of initializing the PCAL6416A GPIO expander.

---

## Initialization

To use the PCAL6416A GPIO expander, first include the required library, create an expander object, and initialize communication in the `setup()` function. The `begin()` function starts I2C communication with the device and doesn't need any manual `Wire.begin()` call before it.

```cpp
// Include required library
#include "PCAL6416A-SOLDERED.h"

// Create PCAL6416A object
PCAL6416A expander;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); // Begin serial communication with PC

    // Initialize communication with PCAL6416A
    expander.begin();

    Serial.println("PCAL6416A initialized.");
}

void loop()
{
}
```

<FunctionDocumentation
  functionName="expander.begin()"
  description="Initializes communication with the PCAL6416A GPIO expander over I2C. Uses the default address 0x20 unless a different address is passed in."
  returnDescription="None."
  parameters={[
    {
      "name": "address",
      "type": "uint8_t",
      "description": "Optional I2C address of the PCAL6416A device. Defaults to 0x20. Pass 0x21 if JP3 has been cut and bridged to VDD."
    }
  ]}
/>