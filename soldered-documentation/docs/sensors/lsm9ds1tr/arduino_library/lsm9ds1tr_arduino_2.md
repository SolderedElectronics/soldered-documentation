---
slug: /lsm9ds1tr/arduino/examples-accelerometer
title: Measuring linear acceleration with LSM9DS1TR Accelerometer (example)
id: lsm9ds1tr-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take accelerometer measurements using the **LSM9DS1 Accelerometer, Gyroscope & Magnetometer**.

---

## Initialization

To start working with the **Accelerometer, Gyroscope & Magnetometer LSM9DS1 Breakout**, you need to set up your Arduino environment. Firstly, include the **required library**, create the sensor object, and **initialize** the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:

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
description="Initializes the LSM9DS1 Accelerometer sensor, setting up communication over I2C or SPI and configuring the sensor for operation. This function also verifies the presence of the sensor on the specified I2C address or SPI bus."
returnDescription="Returns true: If initialization is successful, indicating that the sensor is properly connected and configured.Returns false: If initialization fails, indicating a connection issue or incorrect configuration."
parameters={[]}
/>

---

## Measuring acceleration 

To start measuring acceleration, we first need to read all three **(x,y,z)** directional vectors and display them as shown below.

```cpp
// Read acceleration and print it on serial
Serial.print("ACCX:");
Serial.print(imu.calcAccel(imu.ax), 4);
Serial.print(",");
Serial.print("ACCY:");
Serial.print(imu.calcAccel(imu.ay), 4);
Serial.print(",");
Serial.print("ACCZ:");
Serial.print(imu.calcAccel(imu.az), 4);
Serial.println(",");
```

<FunctionDocumentation functionName="imu.calcAccel()" description="Reads and calculates the acceleration value along the given axis from the LSM9DS1 sensor." returnDescription="Returns a floating-point number in units of g (gravitational force)." parameters={[]} />

---

## Full example

Try all of the above-mentioned functions in this full example, which prints out the measured acceleration data over **Serial at 115200 baud**:

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
    // Update accelerometer values whenever new data is available
    if (imu.accelAvailable())
    {
        imu.readAccel(); // Update ax, ay, az variables with current data

        // Print acceleration data on Serial Monitor
        Serial.print("ACCX:");
        Serial.print(imu.calcAccel(imu.ax), 4);
        Serial.print(",");
        Serial.print("ACCY:");
        Serial.print(imu.calcAccel(imu.ay), 4);
        Serial.print(",");
        Serial.print("ACCZ:");
        Serial.print(imu.calcAccel(imu.az), 4);
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