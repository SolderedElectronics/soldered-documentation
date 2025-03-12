---
slug: /apds-9960/arduino/examples 
title: Initialization and Gesture Detection
id: apds-9960-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the SHTC3 temperature and humidity sensor.

---

## Initialization

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

    // for setGestureSensitivity(..) a value between 1 and 100 is required.
    // Higher values make the gesture recognition more sensitive but less accurate
    // (a wrong gesture may be detected). Lower values makes the gesture recognition
    // more accurate but less sensitive (some gestures may be missed).
    // Default is 80
    // APDS.setGestureSensitivity(80);

    Serial.println("Detecting gestures ...");
}

// ...
```
