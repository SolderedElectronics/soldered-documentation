---
slug: /as5600/arduino/direction
title: AS5600 - Direction
sidebar_label: Direction
id: as5600-arduino-2 
hide_title: False
---

This page contains an example demonstrating initialization, direction configuration, and angle reading using the AS5600 magnetic position sensor.

---

## Initialization

Include the library and create the sensor object:

```cpp
#include "Position-sensor-AS5600-breakout-SOLDERED.h"

PositionSensor sensor;
```

In `setup()`, initialize the sensor and wait for a magnet to be detected:

```cpp
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
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the AS5600 sensor and establishes I2C communication."
  returnDescription="Boolean value, true if the sensor is detected and communication succeeds, false otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.magnetDetected()"
  description="Checks whether a magnet is positioned correctly above the AS5600 sensor."
  returnDescription="Boolean value, true if a magnet is detected, false otherwise."
  parameters={[]}
/>

<CenteredImage src="/img/as5600/Init_Not.png" alt="Serial Monitor - magnet not detected" caption="Serial Monitor output when magnet is not detected" width="100%" />

---

## Direction configuration

In `setup()`, after initializing the sensor, call `setDirection()` to configure which rotation direction increases the angle:

```cpp
// Set direction of angle increment to counterclockwise
sensor.setDirection(AS5600_COUNTERCLOCK_WISE);
```

<FunctionDocumentation
  functionName="sensor.setDirection()"
  description="Sets the direction in which the angle value increases when the magnet is rotated."
  returnDescription="None"
  parameters={[
    {
      name: "direction",
      type: "int",
      description: "Use AS5600_COUNTERCLOCK_WISE for counterclockwise increase, or AS5600_CLOCK_WISE for clockwise increase."
    }
  ]}
/>

| Constant                 | Description                       |
| ------------------------ | --------------------------------- |
| `AS5600_COUNTERCLOCK_WISE` | Angle increases counterclockwise |
| `AS5600_CLOCK_WISE`        | Angle increases clockwise        |

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

    // Set direction of angle increment to counterclockwise
    sensor.setDirection(AS5600_COUNTERCLOCK_WISE);
}

void loop()
{
    Serial.print(sensor.readAngle());                           // Angle as integer
    Serial.print("\t");
    Serial.println(sensor.rawAngle() * AS5600_RAW_TO_DEGREES);  // Angle in degrees

    delay(1000);
}
```

<CenteredImage src="/img/as5600/dir.png" alt="Serial Monitor - direction output" caption="Serial Monitor output for direction detection" width="100%" />

<QuickLink 
  title="Direction.ino" 
  description="Full example for direction detection using the AS5600 sensor"
  url="https://github.com/SolderedElectronics/Soldered-Position-sensor-AS5600-breakout-Arduino-Library/blob/main/examples/Direction/Direction.ino" 
/>
