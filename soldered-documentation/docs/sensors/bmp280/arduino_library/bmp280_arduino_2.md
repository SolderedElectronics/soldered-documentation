---
slug: /bmp280/arduino/initialization 
title: Bmp280 - Initialization
sidebar_label: Initialization
id: bmp280-arduino-2 
hide_title: False
---

This page contains simple examples with function documentation on how to take measurements using the BMP280 temperature and pressure sensor.

---

## Connections for this example

[IMAGE PLACEHOLDER - Connections]

---

## Initialization

To use the BMP280 sensor, first include the required library, create the sensor object and initialize the sensor in the `setup()` function. For accurate altitude readings, set the current pressure at sea level with ``bmp280.setSeaLevelPressure()``


```cpp
// Include Soldered BMP280 library
#include <BMP280-SOLDERED.h>

// Create BMP280 sensor object.
Soldered_BMP280 bmp280;

void setup()
{
    // Initialize serial communication at 115200 bauds.
    Serial.begin(115200);

    // Initialize sensor (check for sensor). Notify if init failed.
    // Also, this will set BMP280 sensor into sleep mode.
    if (!bmp280.begin())
    {
        // Print error message.
        Serial.println("Sensor not found! Check your wiring!");

        // Stop the code!
        while (1)
        {
            // Delay for ESP8266.
            delay(10);
        }
    }

    // Set current pressure at sea level to get accurate altitude readings.
    bmp280.setSeaLevelPressure(1020.6);

    // Set the pressure oversampling to X4
    // bmp280.setPresOversampling(OVERSAMPLING_X4);

    // Set the temperature oversampling to X1
    // bmp280.setTempOversampling(OVERSAMPLING_X1);

    // Set the IIR filter to setting 4
    // bmp280.setIIRFilter(IIR_FILTER_4);
}

```

<FunctionDocumentation
    functionName="bmp280.begin()"
    description="Initializes the BMP280 sensor, setting up communication over I2C and retrieving calibration data from device"
    returnDescription="Boolean value, returns 1 if sensor was properly initialized, 0 if not."
    parameters={[]}
/>

<FunctionDocumentation
    functionName="setSeaLevelPressure()"
    description="Modifies the internal sea_level_pressure valiable for more precise readings."
    parameters={[
    { type: 'double', name: 'pressure', description: "Variable that changes the internal sea_level_pressure variable." },
    ]}
/>