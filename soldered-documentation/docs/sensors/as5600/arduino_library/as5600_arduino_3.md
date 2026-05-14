---
slug: /as5600/arduino/direction
title: AS5600 - Direction
sidebar_label: Direction
id: as5600-arduino-3 
hide_title: False
pagination_next: null
---

This page contains simple examples demonstrating sensor initialization and direction detection using the AS5600 magnetic position sensor.

---

## Direction Detection

In this code snippet, the `loop()` function continuously reads the current angle from the AS5600 sensor. The direction of angle increment is configured using the `setDirection()` function. When the magnet is rotated counterclockwise, the angle value increases, while clockwise rotation decreases the angle value.

```cpp
void loop()
{
    // Angle will increase with counter clockwise rotation, decrease with clockwise rotation

    Serial.print(sensor.readAngle());                          // Get angle value as an integer
    Serial.print("\t");                                        // Tab space for readable output
    Serial.println(sensor.rawAngle() * AS5600_RAW_TO_DEGREES); // Calculate and print degree value of current angle

    delay(1000); // Wait before making the next measurement, so output isn't too fast
}
```

<FunctionDocumentation
  functionName="sensor.readAngle()"
  description="Reads the current angle value from the AS5600 sensor."
  returnDescription="An integer representing the measured angle."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.rawAngle()"
  description="Reads the raw angle value directly from the AS5600 sensor."
  returnDescription="A raw integer value which can be converted to degrees."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.setDirection()"
  description="Sets the direction in which the angle value increases."
  returnDescription="No return value."
  parameters={[
    {
      name: "direction",
      type: "int",
      description: "Direction configuration. Use AS5600_COUNTERCLOCK_WISE or AS5600_CLOCK_WISE."
    }
  ]}
/>

| Constant                        | Description                              |
| --------------------------------| ---------------------------------------- |
| AS5600_COUNTERCLOCK_WISE        | Angle increases counterclockwise         |
| AS5600_CLOCK_WISE               | Angle increases clockwise                |

---

## Full example

Open the Serial Monitor at 115200 baud to observe measured angle values.

```cpp
#include <Wire.h>
#include "Position-sensor-AS5600-breakout-SOLDERED.h"

PositionSensor sensor; // Create sensor object

/**
 * Connecting diagram:
 *
 * AS5600                       Dasduino Core / Connect / ConnectPlus
 * VCC------------------------->VCC
 * GND------------------------->GND
 * SCL------------------------->A5/IO5/IO22
 * SDA------------------------->A4/IO4/IO21
 * 
 * Or, simply use an easyC cable!
 * 
 */

void setup()
{
    Serial.begin(115200); // Begin serial communication (for printing)

    Wire.begin(6, 7);

    if (!sensor.begin()) // Initialize the sensor
    {
        Serial.print("AS5600 not found!");
        while (true)
        {
            delay(1000);
        }
    }

    Serial.print("AS5600 found!");

    while (!sensor.detectMagnet()) // If a magnet is not detected, print message
    {
        Serial.println("Magnet not detected!");
        delay(1000);
    }

    // Set direction of angle increment to counterclockwise
    sensor.setDirection(AS5600_COUNTERCLOCK_WISE);
}

void loop()
{
    // Angle will increase with counter clockwise rotation, decrease with clockwise rotation

    Serial.print(sensor.readAngle());
    Serial.print("\t");
    Serial.println(sensor.rawAngle() * AS5600_RAW_TO_DEGREES);

    delay(1000);
}
```
<CenteredImage src="/img/as5600/dir.png" alt="Serial Monitor" caption="Direction Detection Serial Monitor output"/>

<QuickLink 
  title="Direction.ino" 
  description="Example file for using the AS5600 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-Position-sensor-AS5600-breakout-Arduino-Library/blob/main/examples/Direction/Direction.ino" 
/>