---
slug: /as5600/arduino/angular-speed
title: AS5600 - Angular speed
sidebar_label: Angular speed
id: as5600-arduino-4 
hide_title: False
---

This page contains an example demonstrating how to read the angular speed of a rotating magnet using the AS5600 magnetic position sensor.

---

## Reading angular speed

Instead of tracking absolute angle, `getAngularSpeed()` tells you how fast the magnet is currently rotating. Initialization is the same as every other example, wait for `begin()` and `magnetDetected()` to succeed before reading anything:

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

    while (!sensor.magnetDetected())
    {
        Serial.println("Magnet not detected!");
        delay(1000);
    }

    Serial.println("Magnet detected!");
}

void loop()
{
    Serial.print("w = ");
    Serial.print(sensor.getAngularSpeed());
    Serial.println(" deg/s");

    delay(1000);
}
```

<FunctionDocumentation
  functionName="sensor.getAngularSpeed()"
  description="Calculates the angular speed of the magnet by comparing the current angle reading to the previous one. By default, it triggers a fresh angle reading and returns the result in degrees per second."
  returnDescription="A float representing the angular speed, in the unit selected by the mode parameter."
  parameters={[
    {
      name: "mode",
      type: "uint8_t",
      description: "Optional. AS5600_MODE_DEGREES (default), AS5600_MODE_RADIANS, AS5600_MODE_RPM, or AS5600_MODE_RPS."
    },
    {
      name: "update",
      type: "bool",
      description: "Optional. True (default) triggers a fresh readAngle() call before calculating speed; false reuses the last reading."
    }
  ]}
/>

<InfoBox>
`getAngularSpeed()` works out speed from the difference between the current and previous angle reading, so the first call after `begin()` won't have a meaningful previous value to compare against. Give it a moment to settle once the magnet starts moving.
</InfoBox>

Running the sketch above while turning the magnet back and forth by hand produces output like this, with the sign flipping depending on which way it's currently turning:

<CenteredImage src="/img/as5600/ang_speed.png" alt="Serial Monitor output showing angular speed readings" caption="Serial Monitor output showing angular speed readings as the magnet is turned by hand" width="100%" />

---

## Choosing a unit

The `mode` parameter picks what unit the result comes back in, useful if your project thinks in RPM (a spinning wheel) rather than degrees per second:

```cpp
sensor.getAngularSpeed(AS5600_MODE_RPM); // revolutions per minute
```

| Constant | Unit |
| -------- | ---- |
| `AS5600_MODE_DEGREES` | Degrees per second (default) |
| `AS5600_MODE_RADIANS` | Radians per second |
| `AS5600_MODE_RPM` | Revolutions per minute |
| `AS5600_MODE_RPS` | Revolutions per second |

---

## Full example

```cpp
#include <Wire.h>
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

    while (!sensor.magnetDetected())
    {
        Serial.println("Magnet not detected!");
        delay(1000);
    }

    Serial.println("Magnet detected!");
}

void loop()
{
    Serial.print("w = ");
    Serial.print(sensor.getAngularSpeed());
    Serial.println(" deg/s");

    delay(1000);
}
```

<QuickLink 
  title="Angular_Speed.ino" 
  description="Full example for reading the angular speed of a rotating magnet using the AS5600 sensor"
  url="https://github.com/SolderedElectronics/Soldered-Position-sensor-AS5600-breakout-Arduino-Library/blob/main/examples/Angular_Speed/Angular_Speed.ino" 
/>
