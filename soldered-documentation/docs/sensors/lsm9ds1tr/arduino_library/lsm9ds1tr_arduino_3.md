---
slug: /lsm9ds1tr/arduino/examples-gyroscope
title: LSM9DS1TR – Measuring rotational velocity with LSM9DS1TR Gyroscope (example)
sidebar_label: Measuring rotational velocity with LSM9DS1TR Gyroscope (example)
id: lsm9ds1tr-arduino-3
hide_title: False
---

This page contains some simple examples and function documentation on measuring gyroscope readings using the **LSM9DS1 Accelerometer, Gyroscope & Magnetometer**.

---

## Initialization

To start working with the **Gyroscope** on the **LSM9DS1 Breakout**, you need to set up your Arduino environment. First, include the required libraries, create the sensor object, and initialize the sensor in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly:

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
description="Initializes the LSM9DS1 Gyroscope sensor, setting up communication over I2C or SPI and configuring the sensor for operation. This function also verifies the presence of the sensor on the specified I2C address or SPI bus."
returnDescription="Returns true: If initialization is successful, indicating that the sensor is properly connected and configured.Returns false: If initialization fails, indicating a connection issue or incorrect configuration."
parameters={[]}
/>
---

## Measuring rotational velocity

To measure rotational velocity, we first need to read all three directional vectors (**x, y, z**) and display them as shown below.

```cpp
// Read rotational velocity and print it on serial
// Note: for precise results, you have to calibrate the gyro
Serial.print("GYROX:");
Serial.print(imu.calcGyro(imu.gx), 4);
Serial.print(",");
Serial.print("GYROY:");
Serial.print(imu.calcGyro(imu.gy), 4);
Serial.print(",");
Serial.print("GYROZ:");
Serial.print(imu.calcGyro(imu.gz), 4);
Serial.println(",");
```

<FunctionDocumentation functionName="imu.calcGyro()" description="Reads and calculates the rotational velocity along the given axis (X, Y, or Z) from the LSM9DS1 gyroscope." returnDescription="Returns a floating-point number in units of degrees per second (dps)." parameters={[]} />

---

## Full example

Try all of the functions mentioned above in this full example, which prints the measured gyroscope data over **Serial at 115200 baud**:

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
    // Update gyroscope values whenever new data is available
    if (imu.gyroAvailable())
    {
        imu.readGyro(); // Update gx, gy, gz variables with current data

        // Print gyroscope data on Serial Monitor
        Serial.print("GYROX:");
        Serial.print(imu.calcGyro(imu.gx), 4);
        Serial.print(",");
        Serial.print("GYROY:");
        Serial.print(imu.calcGyro(imu.gy), 4);
        Serial.print(",");
        Serial.print("GYROZ:");
        Serial.print(imu.calcGyro(imu.gz), 4);
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