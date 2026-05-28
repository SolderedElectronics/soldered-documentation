---
slug: /scd43/arduino/examples
title: SCD43 - Basic readings  
sidebar_label: Basic readings 
id: scd43-arduino-2
hide_title: false
---

This page contains a simple example with function documentation on how to read CO2 concentration, temperature, and relative humidity from the SCD43 sensor.

---

## Initialization

To start working with the **SCD43 breakout**, include the library, create the sensor object, initialize I2C, and call `begin()` in `setup()`. The return value of `begin()` tells you whether the sensor was found:

```cpp
#include "SCD43-SOLDERED.h"

SCD43 sensor;

void setup()
{
    Serial.begin(115200);
    Serial.println("SCD43 - Basic Readings");

    Wire.begin();

    if (!sensor.begin())
    {
        Serial.println("Sensor not found. Check wiring. Halting.");
        while (1)
            ;
    }
}
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the SCD43 sensor over I2C, starts periodic measurement mode, and verifies the sensor is present on the bus."
  returnDescription="Returns true if the sensor was found and initialized successfully, false otherwise."
  parameters={[]}
/>

---

## Reading measurements

The SCD43 produces a new measurement every 5 seconds. Call `readMeasurement()` in a loop - it returns `true` when fresh data is ready. Then use the individual getter functions to retrieve each value:

```cpp
void loop()
{
    if (sensor.readMeasurement()) // returns true when fresh data is available
    {
        Serial.println();
        Serial.print("CO2 (ppm):       ");
        Serial.println(sensor.getCO2());
        Serial.print("Temperature (C): ");
        Serial.println(sensor.getTemperature(), 1);
        Serial.print("Humidity (%RH):  ");
        Serial.println(sensor.getHumidity(), 1);
    }
    else
    {
        Serial.print(".");
    }

    delay(500);
}
```

<FunctionDocumentation
  functionName="sensor.readMeasurement()"
  description="Checks whether a fresh measurement is available from the SCD43 and, if so, reads and caches the CO2, temperature, and humidity values."
  returnDescription="Returns true if new data was available and successfully read, false if the sensor is still processing."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.getCO2()"
  description="Returns the CO2 concentration from the most recent measurement."
  returnDescription="CO2 concentration in parts per million (ppm) as a uint16_t."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.getTemperature()"
  description="Returns the temperature from the most recent measurement."
  returnDescription="Temperature in degrees Celsius as a float."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.getHumidity()"
  description="Returns the relative humidity from the most recent measurement."
  returnDescription="Relative humidity in %RH as a float."
  parameters={[]}
/>

---

## Serial Monitor output

<CenteredImage src="/img/scd43/reading.png" alt="SCD43 Serial Monitor output" caption="SCD43 Serial Monitor output showing CO2, temperature, and humidity readings" width="1000px" />

---

## Full example

```cpp
/**
 **************************************************
 *
 * @file        BasicReadings.ino
 * @brief       Read CO2 concentration, temperature, and relative humidity
 *              from the SCD43 sensor using periodic measurements.
 *
 *              The SCD43 outputs a new measurement every 5 seconds.
 *              This example polls for fresh data and prints it to Serial.
 *
 * Hardware connections:
 *   - Connect the SCD43 breakout to your board via the Qwiic / I2C connector.
 *   - Open Serial Monitor at 115200 baud.
 *
 * @copyright   GNU General Public License v3.0
 * @authors     Soldered <soldered@soldered.com>
 *
 * @see         solde.red/333414
 ***************************************************/

#include "SCD43-SOLDERED.h"

SCD43 sensor;

void setup()
{
    Serial.begin(115200);
    Serial.println("SCD43 - Basic Readings");

    Wire.begin();

    if (!sensor.begin())
    {
        Serial.println("Sensor not found. Check wiring. Halting.");
        while (1)
            ;
    }

    // The SCD43 produces a new reading every 5 seconds.
}

void loop()
{
    if (sensor.readMeasurement()) // returns true when fresh data is available
    {
        Serial.println();
        Serial.print("CO2 (ppm):       ");
        Serial.println(sensor.getCO2());
        Serial.print("Temperature (C): ");
        Serial.println(sensor.getTemperature(), 1);
        Serial.print("Humidity (%RH):  ");
        Serial.println(sensor.getHumidity(), 1);
    }
    else
    {
        Serial.print(".");
    }

    delay(500);
}
```

<QuickLink
  title="BasicReadings.ino"
  description="Full example sketch for reading CO2, temperature, and humidity from the SCD43 sensor."
  url="https://github.com/SolderedElectronics/Soldered-SCD43-Arduino-Library/blob/main/examples/BasicReadings/BasicReadings.ino"
/>
