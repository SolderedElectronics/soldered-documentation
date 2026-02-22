---
slug: /bmv080/arduino/setup
title: BMV080 Particulate Matter Sensor - Setup
sidebar_label: Setup
id: bmv080-arduino-2 
hide_title: False
---

<SectionTitle title="Setup" backgroundImage="/img/faq.webp" />

This Arduino library provides an easy-to-use interface for the BMV080 sensor, allowing you to read air quality data, configure sensor parameters, and monitor sensor status with just a few simple function calls.

<InfoBox> **Important Note!** This library relies on the Bosch BMV080 SDK, which isn't included in the library. To properly use this library follow the steps below. </InfoBox>

### 1. Download the Bosch SDK

First, download the latest SDK version from **[this page](https://www.bosch-sensortec.com/software-tools/software/previous-sdk-bmv-080-versions/)**. After downloading, extract the files.

### 2. Copy the required header files

After extracting the files, you need to manually place the necessary files in your BMV080 Arduino library folder. Follow the table below on where to copy the files:

|     Bosch SDK File    | Soldered BMV080 Arduino Library folder |
| --------------------- | -------------------------------------- |
|  api/inc/bmv080.h     | src/BMV080Wrapper/bmv080.h             |
| api/inc/bmv080_defs.h | src/BMV080Wrapper/bmv080_defs.h        |

### 3. Initialization

After completing the steps above, now we can start using our sensor to read air quality data. First, lets initialize the sensor using I2C communication.

```cpp
#include "BMV080-SOLDERED.h"

BMV080 bmv080;             // Create an instance of the BMV080 class
#define BMV080_ADDR 0x57   // BMV080 default address

void setup()
{
    Serial.begin(115200);

    while (!Serial)
        delay(10); // Wait for Serial to become available.

    // Initialize the Wire library and set the device as controller
    Wire.begin();
 
    // Attempt to initialize the sensor via I2C
    if (bmv080.begin(BMV080_ADDR, Wire) == false) 
    {
        Serial.println("BMV080 not detected");
        while (1)
        ;
    }
    Serial.println("BMV080 found!");

    // Initialize the sensor
    if (bmv080.init())
    {
        Serial.println("BMV sensor initialized");
    }
    else
    {
        Serial.println("BMV initialization failed");
        while (1)
        ;
    }

    // Set the sensor mode to continuous mode
    if (bmv080.setMode(BMV080_MODE_CONTINUOUS) == true)
    {
        Serial.println("BMV080 set to continuous mode");
    }
    else
    {
        Serial.println("Error setting BMV080 mode");
    }
 }
```

<FunctionDocumentation
  functionName="bmv080.begin()"
  description="Begins the BMV080 with I2C as the communication bus"
  returnDescription="True if successful, false otherwise"
  returnType="bool"
  parameters={[
    { type: 'uint8_t', name: 'address', description: 'Sensor I2C address to use for communication' },
    { tyep: 'TwoWire', name: 'wirePort', description: 'Wire port to use for I2C communication'}
  ]}
/>

<FunctionDocumentation
  functionName="bmv080.init()"
  description="Initializes the BMV080 sensor"
  returnDescription="True if successful, false otherwise"
  returnType="bool"
/>

### 4. Getting readings

```cpp
void loop()
{
    // Attempt to read new measurement data from the sensor
    if (bmv080.readSensor())
    {
        // Get the PM10, PM2.5 and PM1 particulate matter concentrations and store them in variables
        // These values are updated when readSensor() method is called
        float pm10 = bmv080.PM10();
        float pm25 = bmv080.PM25();
        float pm1 = bmv080.PM1();

        // Print the values
        Serial.print("PM10: ");
        Serial.print(pm10);
        Serial.print("\t");
        Serial.print("PM2.5: ");
        Serial.print(pm25);
        Serial.print("\t");
        Serial.print("PM1: ");
        Serial.print(pm1);

        // Check if sensor is obstructed, value updates only when readSensor() is called
        if (bmv080.isObstructed() == true)
        {
            Serial.print("\tObstructed");
        }

        Serial.println();
    }
    delay(100);
}
```

<FunctionDocumentation
  functionName="bmv080.readSensor()"
  description="Triggers a sensor reading and updates the internal data cache with latest sensor values"
  returnDescription="True if data was successfully read from the senso, false if reading failed or no new data"
  returnType="bool"
  parameters={[
    { type: 'bmv080_output_t', name: 'bmv080_output', description: '(Optional) Pointer to a bmv080_output_t struct to store the sensor readings' }
  ]}
/>

<FunctionDocumentation
  functionName="bmv080.isObstructed()"
  description="This method returns the obstruction status from the latest sensor reading. Obstruction can be caused by dust, debris, or other particles blocking the sensor's optical path."
  returnDescription="true if the sensor is obstructed, false otherwise"
  returnType="bool"
/>

<FunctionDocumentation
  functionName="bmv080.PM1()"
  description="Function that returns the latest PM1 reading from the sensor's internal cache"
  returnDescription="PM1 concentration in micrograms per cubic meter (µg/m³)"
  returnType="float"
/>

<FunctionDocumentation
  functionName="bmv080.PM25()"
  description="Function that returns the latest PM2.5 reading from the sensor's internal cache"
  returnDescription="PM2.5 concentration in micrograms per cubic meter (µg/m³)"
  returnType="float"
/>

<FunctionDocumentation
  functionName="bmv080.PM10()"
  description="Function that returns the latest PM10 reading from the sensor's internal cache"
  returnDescription="PM10 concentration in micrograms per cubic meter (µg/m³)"
  returnType="float"
/>