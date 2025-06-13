---
slug: /lsm9ds1tr/arduino/examples-magnetometer
title: LSM9DS1TR – Measuring magnetic field strength with LSM9DS1TR Magnetometer (example)
sidebar_label: Measuring magnetic field strength with LSM9DS1TR Magnetometer (example)
id: lsm9ds1tr-arduino-4
hide_title: False
---

This page contains some simple examples with function documentation on how to take **magnetometer** measurements using the **LSM9DS1 Accelerometer, Gyroscope & Magnetometer**.

---

### Initialization
To start working with the **Magnetometer** in **LSM9DS1 Breakout**, you need to set up your Arduino environment. First, include the required library, create the sensor object, and initialize the sensor in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly:

```cpp
// Include libraries
#include "LSM9DS1TR-SOLDERED.h"
#include "Wire.h"

// Create an LSM9DS1TR object
LSM9DS1TR imu; // Default address for magnetometer is 0x1E.

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
returnDescription="Returns true: If initialization is successful, indicating that the sensor is properly connected and configured. Returns false: If initialization fails, indicating a connection issue or incorrect configuration."
parameters={[]}
/>

---

### Measuring Magnetic Field Strength
To start measuring magnetic field data, you first need to read all three directional vectors (**x, y, z**) and display them as shown below:

```cpp
// Read magnetic field strength and print it on serial
Serial.print("MAGX:");
Serial.print(imu.calcMag(imu.mx), 4);
Serial.print(",");
Serial.print("MAGY:");
Serial.print(imu.calcMag(imu.my), 4);
Serial.print(",");
Serial.print("MAGZ:");
Serial.print(imu.calcMag(imu.mz), 4);
Serial.println(",");
```

<FunctionDocumentation 
  functionName="imu.calcMag()" 
  description="Reads and calculates the magnetic field strength along the given axis (X, Y, or Z) from the LSM9DS1 magnetometer." 
  returnDescription="Returns a floating-point number in units of gauss." 
  parameters={[]} 
/>

---

### Full Example
Try all of the above-mentioned functions in this full example, which prints out measured magnetic field data over **Serial at 115200 baud**:

```cpp
// Include libraries
#include "LSM9DS1TR-SOLDERED.h"
#include "Wire.h"

// Create object from LSM library
LSM9DS1TR imu; // Default address for magnetometer is 0x1E

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
    // Update magnetometer values whenever new data is available
    if (imu.magAvailable())
    {
        imu.readMag(); // Update mx, my, mz variables with current data

        // Print magnetometer data on Serial Monitor
        Serial.print("MAGX:");
        Serial.print(imu.calcMag(imu.mx), 4);
        Serial.print(",");
        Serial.print("MAGY:");
        Serial.print(imu.calcMag(imu.my), 4);
        Serial.print(",");
        Serial.print("MAGZ:");
        Serial.print(imu.calcMag(imu.mz), 4);
        Serial.println(",");
    }

    delay(150); // Adjust delay for desired refresh rate
}
```

<QuickLink 
  title="LSM9DS1_Basic_I2C.ino" 
  description="Most basic example of use. Example using the LSM9DS1 with basic settings"
  url="https://github.com/SolderedElectronics/Soldered-LSM9DS1TR-Arduino-Library/blob/main/examples/LSM9DS1_Basic_I2C/LSM9DS1_Basic_I2C.ino" 
/>