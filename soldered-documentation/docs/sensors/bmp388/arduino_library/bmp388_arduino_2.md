---
slug: /bmp388/arduino/basic-continuous-measurements
title: BMP388 Pressure & Temperature Sensor - Basic continuous measurements
id: bmp388-arduino-2 
sidebar_label: Basic continuous measurements
hide_title: False
---

This page contains a simple example showing how to take continuous measurements with the BMP388 and print them to the Serial monitor.

---

## Connections for this example

<CenteredImage src="/img/bmp388/connections.jpg" alt="Connections"  />

---

## Initialization

To use the BMP388 sensor, first include the required library, create the sensor object, and initialize the sensor in the `setup()` function, along with setting its calibration parameters
```cpp
// Include Soldered BMP388 library.
#include <BMP388-SOLDERED.h>

// Create BMP388 sensor object.
Soldered_BMP388 bmp388;

// Initialize serial communication at 115200 bauds.
    Serial.begin(115200);

    // Initialize sensor (check for sensor). Notify if init failed.
    // Also, this will set BMP388 sensor into sleep mode.
    if (!bmp388.begin())
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
    bmp388.setSeaLevelPressure(1025.0);

    // Set the standby time of each sample to be roughly 1.3 seconds.
    bmp388.setTimeStandby(TIME_STANDBY_1280MS);

    // Start BMP388 continuous conversion in normal mode.
    bmp388.startNormalConversion();
```

<FunctionDocumentation
  functionName="bmp388.begin()"
  description="Initializes the BMP388 sensor, setting up communication over I2C"
  returnDescription="uint8_t value, 1 if initialization was successfull, 0 if not"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="bmp388.setSeaLevelPressure(float pressure)"
  description="Sets the sea level value of pressure, used in calculating altitude"
  returnDescription="None"
  parameters={[
  { type: 'float', name: 'pressure', description: "Pressure value in hPa" },
  ]}
/>

<FunctionDocumentation
  functionName="bmp388.setTimeStandby(enum TimeStandby standby)"
  description="Set the standby time of each sample"
  returnDescription="None"
  parameters={[
  { type: 'enum TimeStandby', name: 'standby', description: "Time the sensor will be asleep between each measurement" },
  ]}
/>

<FunctionDocumentation
  functionName="bmp388.startNormalConversion()"
  description="Start BMP388 continuous conversion in normal mode."
  returnDescription="None"
  parameters={[]}
/>

## Getting all readings

In the `loop()` function, we forward the variables in which we want to store the calculated measurements and print them to the serial monitor:

```cpp
void loop()
{
    // Variables for storing measurement data.
    float temperature, pressure, altitude;

    // Check if the data is ready.
    if (bmp388.getMeasurements(temperature, pressure, altitude))
    {
        // Print the results.
        Serial.print(temperature);
        Serial.print(F("*C   "));
        Serial.print(pressure);
        Serial.print(F("hPa   "));
        Serial.print(altitude);
        Serial.println(F("m"));
    }
}
```

<FunctionDocumentation
  functionName="bmp388.getMeasurements(volatile float &temperature, volatile float &pressure, volatile float &altitude);"
  description="Gets measurements from the sensor if the sensor is ready to do so"
  returnDescription="uint8_t value, 1 if the data is ready to be read, 0 if not"
  parameters={[
  { type: 'volatile float&', name: 'temperature', description: "Variable in which the temperature value will be stored" },
  { type: 'volatile float&', name: 'pressure', description: "Variable in which the pressure value will be stored" },
  { type: 'volatile float&', name: 'altitude', description: "Variable in which the altitude value will be stored" },
  ]}
/>

<CenteredImage src="/img/bmp388/serial_monitor.png" alt="Serial monitor readings" caption="Serial monitor" width="100%" />

---

## Full Example
You can find the full example below:

```cpp
// Include Soldered BMP388 library.
#include <BMP388-SOLDERED.h>

// Create BMP388 sensor object.
Soldered_BMP388 bmp388;

void setup()
{
    // Initialize serial communication at 115200 bauds.
    Serial.begin(115200);

    // Initialize sensor (check for sensor). Notify if init failed.
    // Also, this will set BMP388 sensor into sleep mode.
    if (!bmp388.begin())
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
    bmp388.setSeaLevelPressure(1025.0);

    // Set the standby time of each sample to be roughly 1.3 seconds.
    bmp388.setTimeStandby(TIME_STANDBY_1280MS);

    // Start BMP388 continuous conversion in normal mode.
    bmp388.startNormalConversion();
}

void loop()
{
    // Variables for storing measurement data.
    float temperature, pressure, altitude;

    // Check if the data is ready.
    if (bmp388.getMeasurements(temperature, pressure, altitude))
    {
        // Print the results.
        Serial.print(temperature);
        Serial.print(F("*C   "));
        Serial.print(pressure);
        Serial.print(F("hPa   "));
        Serial.print(altitude);
        Serial.println(F("m"));
    }
}
```