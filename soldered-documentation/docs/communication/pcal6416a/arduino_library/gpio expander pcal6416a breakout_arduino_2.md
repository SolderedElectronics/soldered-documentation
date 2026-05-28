---
slug: /gpio expander pcal6416a breakout/arduino/initialization
title: PCAL6416AHF - Initialization
sidebar_label: Initialization
id: gpio expander pcal6416a breakout-arduino-2 
hide_title: false
---


This page contains a simple example of initializing the PCAL6416A GPIO expander.

---

## Initialization

To use the PCAL6416A GPIO expander, first include the required libraries, create an expander object, and initialize communication in the `setup()` function. You can use the `begin()` function to start I2C communication with the device.

```cpp
// Include required libraries
#include <Wire.h>
#include "PCAL6416A-SOLDERED.h"

// Create PCAL6416A object
PCAL6416A expander;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); // Begin serial communication with PC

    // Required for NULA DeepSleep Qwiic board
    Wire.begin(8, 9);

    // Initialize communication with PCAL6416A
    expander.begin(0x20);

    Serial.println("PCAL6416A initialized.");
}

void loop()
{
}
```

<FunctionDocumentation
  functionName="expander.begin(0x20)"
  description="Initializes communication with the PCAL6416A GPIO expander over the I2C interface using address 0x20."
  returnDescription="Starts communication with the PCAL6416A device."
  parameters={[
    {
      "name": "address",
      "type": "uint8_t",
      "description": "I2C address of the PCAL6416A device."
    }
  ]}
/>