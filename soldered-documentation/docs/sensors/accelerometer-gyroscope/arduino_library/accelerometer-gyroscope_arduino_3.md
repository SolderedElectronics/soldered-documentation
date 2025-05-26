---
slug: /accelerometer-gyroscope/arduino/examples-gyroscope 
title: Measuring linear acceleration with LSM6DS3 Gyroscope (example)
id: accelerometer-gyroscope-arduino-3 
hide_title: False
---

This page contains some simple examples with function documentation on how to take gyroscope measurements using the LSM6DS Accelerometer & Gyroscope.

---

## Initialization

To start working with the **Gyroscope in LSM6DS 6-DOF Breakout**, you need to set up your Arduino environment. Firstly, include the required library, create the sensor object, and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly.

```cpp
// Include libraries
#include "LSM6DS3-SOLDERED.h"
#include "Wire.h"

// Create an LSM6DS3 object
Soldered_LSM6DS3 myIMU; // Default address is 0x6B

void setup()
{
// Initialize serial communication
Serial.begin(115200);
delay(1000);
//...

// Initialize sensor
if (!myIMU.begin())
{
    // 'begin' returned false, there is an error
    Serial.println("Can't initialize LSM6DS!");
    Serial.println("Check connection!");
    while (true)
        ;
}

Serial.println("LSM6DS3 initialized successfully.");
}
//...
```

<FunctionDocumentation
  functionName="myIMU.begin()"
  description="Initializes the **LSM6DS Accelerometer & Gyroscope sensor**, setting up communication over I2C or SPI and configuring the sensor for operation. This function also verifies the presence of the sensor on the specified I2C address or SPI bus."
  returnDescription="**Returns `true`**: If initialization is successful, indicating that the sensor is properly connected and configured.
- **Returns `false`**: If initialization fails, indicating a connection issue or incorrect configuration."
  parameters={[]}
/>

---

## Measuring rotational velocity

To start measuring rotational velocity information, we first need to read all three (x, y, z) directional vectors and display them as shown below.

```cpp
// Read rotational velocity and print it on serial
// Note: for precise results, you have to calibrate the gyro
Serial.print("GYROX:");
Serial.print(myIMU.readFloatGyroX(), 4);
Serial.print(",");
Serial.print("GYROY:");
Serial.print(myIMU.readFloatGyroY(), 4);
Serial.print(",");
Serial.print("GYROZ:");
Serial.print(myIMU.readFloatGyroZ(), 4);
Serial.print(",");

```

<FunctionDocumentation
  functionName="myIMU.readFloatGyro*()"
  description="Reads the rotational velocity along the given axis (X, Y, or Z) from the LSM6DS gyroscope."
  returnDescription="Returns a floating-point number in units of degrees per second (dps)."
  parameters={[]}
/>

---

<!-- <CenteredImage src="/img/accelerometer-gyroscope/AGposition3.gif" alt="LSM6DS in position 1" caption="LSM6DS in position 1" width="750px" /> -->
<CenteredImage src="/img/accelerometer-gyroscope/serialMonitor3.png" alt="Serial Monitor for LSM6DS Gyroscope measurement" caption="Serial Monitor for LSM6DS Gyroscope measurement" width="1000px" />

---

## Full example

Try all of the above-mentioned functions in this full example, which prints out the measured gyroscope data over Serial at 115200 baud:

```cpp

// Include libraries
#include "LSM6DS3-SOLDERED.h"
#include "Wire.h"

// Create object from LSM library
Soldered_LSM6DS3 myIMU; // Default address is 0x6B

void setup()
{
    // Init serial communication
    Serial.begin(115200);
    delay(1000); // Relax...

    // Call .begin() to configure the IMU
    myIMU.begin();
}

void loop()
{
    // Read rotational velocity and print it on serial
    // Note: for precise results, you have to calibrate the gyro
    Serial.print("GYROX:");
    Serial.print(myIMU.readFloatGyroX(), 4);
    Serial.print(",");
    Serial.print("GYROY:");
    Serial.print(myIMU.readFloatGyroY(), 4);
    Serial.print(",");
    Serial.print("GYROZ:");
    Serial.print(myIMU.readFloatGyroZ(), 4);
    Serial.print(",");    

    delay(150);

}
```
<QuickLink 
  title="minimalistExample.ino" 
  description=" Most basic example of use. Example using the LSM6DS3 with basic settings"
  url="https://github.com/SolderedElectronics/Soldered-LSM6DS3-Arduino-Library/blob/main/examples/MinimalistExample/MinimalistExample.ino" 
/>