---
slug: /apds-9960/arduino/Initialization
title: "Color and Gesture sensor APDS-9960 \u2013 Arduino initialization"
id: apds-9960-arduino-2
hide_title: false
---
This page contains a simple example of initializing the APDS-9960 sensor.

---

## Initialization

To use the APDS-9960 sensor, first include the required library, create a sensor object, and initialize it in the `setup()` function. You can use the return value of `begin()` to verify that everything is connected correctly:

```cpp
// Include the library
#include "APDS9960-SOLDERED.h"

// Create an APDS-9960 object
APDS_9960 APDS;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); // Begin serial communication with the PC
    while (!Serial) // Wait until the serial port is active
        ;

    if (!APDS.begin())  // Start communication with the sensor
    {
        Serial.println("Error initializing APDS-9960 sensor!");
        while (1); // Loop forever if the sensor is not available
    }

    Serial.println("Sensor initialized.");
}

// ...
```

<FunctionDocumentation
  functionName="APDS.begin()"
  description="Initializes the APDS-9960 sensor, setting up communication over I2C and verifying its presence."
  returnDescription="True if initialization is successful, false otherwise."
  parameters={[]}
/>