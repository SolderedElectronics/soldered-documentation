---
slug: /apds-9960/arduino/Initialization
title: Initialization
id: apds-9960-arduino-2
hide_title: False
---

This page contains a simple example of initialization of the APDS-9960 sensor.

---

To use the APDS-9960 sensor, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:

```cpp
// Include the library
#include "APDS9960-SOLDERED.h"

// Create an APDS-9960 object
APDS_9960 APDS;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); //Begin serial communication with PC
    while (!Serial) //Wait until serial becomes active
        ;

    if (!APDS.begin())  //Begin communication with sensor
    {
        Serial.println("Error initializing APDS-9960 sensor!");
      while(1); //Loop forever if sensor is not available
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

