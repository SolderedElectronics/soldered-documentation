---
slug: /accelerometer-gyroscope/arduino/examples-temperature 
title: LSM6DS – Measuring temperature with LSM6DS3 (example)
sidebar_label: Measuring temperature with LSM6DS3 (example)
id: accelerometer-gyroscope-arduino-4 
hide_title: False
---

This page contains some simple examples with function documentation on how to measure temperature using the **LSM6DS Accelerometer & Gyroscope sensor**.

---

## Initialization

To start working with the **Temperature Sensor in LSM6DS 6-DOF Breakout**, you need to set up your Arduino environment. First, include the required library, create the sensor object, and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:

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
}
void loop()
{
    // Initialize sensor
    if (!myIMU.begin())
    {
        // 'begin' returned false, there is an error
        Serial.println("Can't initialize LSM6DS3!");
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
  description="Initializes the **LSM6DS3 Accelerometer & Gyroscope sensor**, setting up communication over I2C or SPI and configuring the sensor for operation. This function also verifies the presence of the sensor on the specified I2C address or SPI bus."
  returnDescription="**Returns `true`**: If initialization is successful, indicating that the sensor is properly connected and configured.
- **Returns `false`**: If initialization fails, indicating a connection issue or incorrect configuration."
  parameters={[]}
/>

---

## Measuring temperature

To start measuring temperature data, you can use the following functions to read values in Celsius and Fahrenheit and display them as shown below:

```cpp
// Read the temperature and print it on serial
Serial.print("DEGC:");
Serial.print(myIMU.readTempC(), 4);
Serial.print(",");
Serial.print("DEGF:");
Serial.println(myIMU.readTempF(), 4);
```

<FunctionDocumentation
  functionName="myIMU.readTemp*()"
  description="Reads the temperature value from the LSM6DS3 sensor in Celsius (`readTempC`) or Fahrenheit (`readTempF`)."
  returnDescription="Returns a floating-point number representing the temperature in degrees Celsius or Fahrenheit."
  parameters={[]}
/>

---

## Full example

Try all of the above-mentioned functions in this full example, which prints out the measured temperature data over Serial at 115200 baud:

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
    // Get all parameters and print it on the Serial Monitor

    // Read the temperature and print it on serial
    Serial.print("DEGC:");
    Serial.print(myIMU.readTempC(), 4);
    Serial.print(",");
    Serial.print("DEGF:");
    Serial.println(myIMU.readTempF(), 4);

    delay(150);
}
```
<QuickLink 
  title="minimalistExample.ino" 
  description="Most basic example of use. Example using the LSM6DS3 with basic settings"
  url="https://github.com/SolderedElectronics/Soldered-LSM6DS3-Arduino-Library/blob/main/examples/MinimalistExample/MinimalistExample.ino" 
/>