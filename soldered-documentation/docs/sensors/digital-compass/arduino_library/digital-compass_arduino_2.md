---
slug: /digital-compass/arduino/examples 
title: Digital Compass - Detecting compass heading
sidebar_label: Detecting compass heading
id: digital-compass-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the Digital Compass.

---

## Initialization

To start working with the **Digital Compass AK09918C 3-Axis Magnetometer breakout**, you need to set up your Arduino enviroment. Firstly, include the **required library**, create the sensor object, and **initialize** the sensor in the `setup()` function. You can use the return of the `begin()` to check if everything is connected correctly:

```cpp
#include "AK09918-SOLDERED.h"

AK09918 compass;

void setup()
{
    Serial.begin(115200);

    AK09918_err_type_t err = compass.begin(Wire, AK09918_CONT_MEASURE_MODE1);
    if (err != AK09918_ERR_OK)
    {
        Serial.print("Sensor init failed: ");
        Serial.println(compass.strError(err));
        while (true)
            ;
    }

    Serial.println("AK09918 compass heading — keep the board flat!");
    Serial.println("Heading\t\tDirection\tX\t\tY\t\tZ");
}
```

