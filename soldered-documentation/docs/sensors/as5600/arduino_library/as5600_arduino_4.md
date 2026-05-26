---
slug: /as5600/arduino/Read_Angle
title: AS5600 - Read Angle
sidebar_label: Read Angle
id: as5600-arduino-4 
hide_title: False

---

This page contains simple examples demonstrating sensor initialization and angle measurement using the AS5600 magnetic position sensor.

---

## Read Angle

In this code snippet, the `loop()` function continuously reads the current angular position measured by the AS5600 sensor. The `readAngle()` function returns the angle value, while `rawAngle()` returns the raw sensor measurement which is converted to degrees.

```cpp
void loop()
{
    Serial.print(sensor.readAngle());                          // Read angle value
    Serial.print("\t");                                        // Tab spacing for readability
    Serial.println(sensor.rawAngle() * AS5600_RAW_TO_DEGREES); // Convert raw value to degrees

    delay(1000); // Wait before taking another measurement
}
```

<FunctionDocumentation
  functionName="sensor.readAngle()"
  description="Reads the current angular position measured by the AS5600 sensor."
  returnDescription="An integer representing the measured angle."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.rawAngle()"
  description="Reads the raw angular measurement value from the AS5600 sensor."
  returnDescription="A raw integer value representing the sensor measurement."
  parameters={[]}
/>

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
    Serial.begin(115200); // Begin serial communication

    Wire.begin(6, 7);

    if (!sensor.begin()) // Initialize sensor
    {
        Serial.print("AS5600 not found!");

        while (true)
        {
            delay(1000);
        }
    }

    Serial.println("AS5600 found!");

    while (!sensor.detectMagnet()) // Wait for magnet detection
    {
        Serial.println("Magnet not detected!");
        delay(1000);
    }
}

void loop()
{
    Serial.print(sensor.readAngle());
    Serial.print("\t");
    Serial.println(sensor.rawAngle() * AS5600_RAW_TO_DEGREES);

    delay(1000);
}
```
<CenteredImage src="/img/as5600/angle.png" alt="Serial Monitor" caption="Angle Read Serial Monitor output"/>

<QuickLink 
  title="Read_Angle.ino" 
  description="Example file for using the AS5600 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-Position-sensor-AS5600-breakout-Arduino-Library/blob/main/examples/Read_Angle/Read_Angle.ino" 
/>