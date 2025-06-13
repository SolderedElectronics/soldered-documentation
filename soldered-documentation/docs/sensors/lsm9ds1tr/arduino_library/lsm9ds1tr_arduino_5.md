---
slug: /lsm9ds1tr/arduino/examples-temperature
title: LSM9DS1TR – Measuring temperature with LSM9DS1TR (example)
sidebar_label: Measuring temperature with LSM9DS1TR (example)
id: lsm9ds1tr-arduino-5
hide_title: False
---

This page contains a few simple examples with function documentation on how to measure **temperature** using the **LSM9DS1 Accelerometer, Gyroscope & Magnetometer sensor**.

---

### Initialization
To start working with the temperature sensor on the LSM9DS1 Breakout, you must set up your Arduino environment. First, include the required library, create the sensor object, and initialize the sensor in the `setup()` function. You can use the return value of `begin()` to verify that everything is connected correctly:

```cpp
// Include libraries
#include "LSM9DS1TR-SOLDERED.h"
#include "Wire.h"

// Create an LSM9DS1TR object
LSM9DS1TR imu; // Default address for accelerometer/gyroscope is 0x6B, and magnetometer is 0x1E.

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);
    delay(1000); // Relax...

    // Initialize sensor
    if (!imu.begin())
    {
        // 'begin' returned false, there is an error
        Serial.println("Can't initialize LSM9DS1!");
        Serial.println("Check connection!");
        while (true)
            ;
    }

    Serial.println("LSM9DS1 initialized successfully.");
}

//...
```

<FunctionDocumentation
functionName="imu.begin()"
description="Initializes the LSM9DS1 Magnetometer sensor, setting up communication over I2C or SPI and configuring the sensor for operation. This function also verifies the presence of the sensor on the specified I2C address or SPI bus."
returnDescription="Returns true: If initialization is successful, indicating that the sensor is properly connected and configured.Returns false: If initialization fails, indicating a connection issue or incorrect configuration."
parameters={[]}
/>

---

### Measuring Temperature
To start measuring temperature data, you can use the following functions to read values in **Celsius** and **Fahrenheit**, as shown below:

```cpp
// Read the temperature and print it on serial
Serial.print("DEGC:");
Serial.print(imu.readTempC(), 4);
Serial.print(",");
Serial.print("DEGF:");
Serial.println(imu.readTempF(), 4);
```

<FunctionDocumentation functionName="imu.readTemp*()" description="Reads the temperature value from the LSM9DS1 sensor in Celsius (`readTempC`) or Fahrenheit (`readTempF`)." returnDescription="Returns a floating-point number representing the temperature in degrees Celsius or Fahrenheit." parameters={[]} />

---

### Full Example
Try all of the above-mentioned functions in this full example, which prints out the measured temperature data over **Serial at 115200 baud**:


```cpp
// Include libraries
#include "LSM9DS1TR-SOLDERED.h"
#include "Wire.h"

// Create object from LSM library
LSM9DS1TR imu; // Default address for accelerometer/gyroscope is 0x6B

void setup()
{
    // Init serial communication
    Serial.begin(115200);
    delay(1000); // Relax...

    // Call .begin() to configure the IMU
    if (!imu.begin())
    {
        Serial.println("Failed to initialize LSM9DS1!");
        while (true)
            ;
    }
}

void loop()
{
    // Get all parameters and print them to the Serial Monitor

    // Read the temperature and print it on serial
    Serial.print("DEGC:");
    Serial.print(imu.readTempC(), 4);
    Serial.print(",");
    Serial.print("DEGF:");
    Serial.println(imu.readTempF(), 4);

    delay(150); // Adjust delay for desired refresh rate
}

```
<QuickLink 
  title="LSM9DS1_Basic_I2C.ino" 
  description="Most basic example of use. Example using the LSM9DS1 with basic settings"
  url="https://github.com/SolderedElectronics/Soldered-LSM9DS1TR-Arduino-Library/blob/main/examples/LSM9DS1_Basic_I2C/LSM9DS1_Basic_I2C.ino" 
/>