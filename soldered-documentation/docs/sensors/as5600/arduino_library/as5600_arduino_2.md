---
slug: /as5600/arduino/examples 
title: AS5600 - Initialization
sidebar_label: Initialization
id: as5600-arduino-2 
hide_title: False
---

This page contains a simple example of initializing the AS5600 sensor.

---

## Initialization

To use the AS5600 sensor, first include the required library, create a sensor object, and initialize it in the `setup()` function. You can use the return value of `begin()` to verify that everything is connected correctly:

```cpp
#include "Position-sensor-AS5600-breakout-SOLDERED.h"

PositionSensor sensor;

void setup()
{
    Serial.begin(115200);

    Wire.begin();

    if (!sensor.begin())
    {
        Serial.println("AS5600 not found! Check wiring. Freezing.");
        while (true)
        {
            delay(1000);
        }
    }

    Serial.println("AS5600 found!");

    while (!sensor.detectMagnet())
    {
        Serial.println("Magnet not detected!");
        delay(1000);
    }

    Serial.println("Magnet detected!");
}
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the AS5600 sensor and establishes I2C communication."
  returnDescription="Boolean value, true if the sensor is detected and communication succeeds, false otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.detectMagnet()"
  description="Checks whether a magnet is positioned correctly above the AS5600 sensor."
  returnDescription="Boolean value, true if a magnet is detected, false otherwise."
  parameters={[]}
/>
