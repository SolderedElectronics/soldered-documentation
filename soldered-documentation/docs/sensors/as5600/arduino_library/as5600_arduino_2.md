---
slug: /as5600/arduino/examples 
title: As5600 - Initialization
sidebar_label: Initialization
id: as5600-arduino-2 
hide_title: False
---

This page contains a simple example of initializing the APDS-9960 sensor.

---

## Initialization

To use the AS5600 sensor, first include the required library, create a sensor object, and initialize it in the `setup()` function. You can use the return value of `begin()` to verify that everything is connected correctly:

```cpp
// Include the library
#include "Position-sensor-AS5600-breakout-SOLDERED.h"

// Create sensor object
PositionSensor sensor;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); // Begin serial communication (for printing)

    if (!sensor.begin()) // Initialize the sensor
    {
        Serial.print("AS5600 not found!");
        while (true)
        {
            delay(1000);
        }
}

// ...
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the AS5600 sensor, setting up communication over I2C and verifying its presence."
  returnDescription="True if initialization is successful, false otherwise."
  parameters={[]}
/>