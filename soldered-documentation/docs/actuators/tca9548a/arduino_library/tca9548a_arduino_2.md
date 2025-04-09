---
slug: /tca9548a/arduino/examples 
title: Arduino example
id: tca9548a-arduino-2 
hide_title: False
---

This page contains an example for setting up the LSM6DS3 and SHTC3 sensors with I2C multiplexer TCA9548A.

---

## Connections for this example

take image!!
<!-- <CenteredImage src="/img/tca9548a/led_connection.png" width="100%" /> -->

---

## Full example

In this example, we first include the necessary libraries for the **TCA9548A I2C multiplexer**, **SHTC3 sensor**, and **LSM6DS3TR sensor**. We then create instances of the multiplexer and sensors. In the `setup()` function, we initialize the I2C communication with the multiplexer and sensors, ensuring all channels are properly configured. Finally, in the `loop()` function, we read data from each sensor on its respective channel and print the results to the Serial Monitor.


```cpp
#include "TCA9548A-SOLDERED.h"
#include "SHTC3-SOLDERED.h"
#include "LSM6DS3-SOLDERED.h"
#include <Arduino.h>

// Create objects for the multiplexer, SHTC3, and LSM6DS3 sensors
TCA9548A I2CMux; // Default address is 0x70
SHTC3 shtcSensor;
Soldered_LSM6DS3 myIMU; // Default address is 0x6B

void setup()
{
    Serial.begin(115200); // Start serial communication with PC
    delay(1000);          // Relax...

    // Initialize the I2C multiplexer
    I2CMux.begin();       // Initialize multiplexer
    I2CMux.closeAll();    // Ensure all channels are closed initially

    // Initialize SHTC3 sensor on channel 0
    I2CMux.openChannel(0);
    if (!shtcSensor.begin())
    {
        Serial.println("Failed to initialize SHTC3 sensor!");
    }
    else
    {
        Serial.println("SHTC3 sensor initialized successfully.");
    }
    I2CMux.closeChannel(0);

    // Initialize LSM6DS3TR sensor on channel 1
    I2CMux.openChannel(1);
    if (!myIMU.begin())
    {
        Serial.println("Failed to initialize LSM6DS3TR sensor!");
    }
    else
    {
        Serial.println("LSM6DS3TR sensor initialized successfully.");
    }
    I2CMux.closeChannel(1);
}

void loop()
{
    // Read data from SHTC3 sensor on channel 0
    I2CMux.openChannel(0);
    shtcSensor.sample();
    Serial.print("Temp (°C): ");
    Serial.println(shtcSensor.readTempC(), 2);
    Serial.print("Humidity (%): ");
    Serial.println(shtcSensor.readHumidity(), 2);
    I2CMux.closeChannel(0);

    delay(1000); // Wait before switching to the next channel

    // Read data from LSM6DS3TR sensor on channel 1
    I2CMux.openChannel(1);
    
    // Read acceleration data
    Serial.print("ACCX: ");
    Serial.print(myIMU.readFloatAccelX(), 4);
    Serial.print(", ACCY: ");
    Serial.print(myIMU.readFloatAccelY(), 4);
    Serial.print(", ACCZ: ");
    Serial.println(myIMU.readFloatAccelZ(), 4);

    // Read gyroscope data
    Serial.print("GYROX: ");
    Serial.print(myIMU.readFloatGyroX(), 4);
    Serial.print(", GYROY: ");
    Serial.print(myIMU.readFloatGyroY(), 4);
    Serial.print(", GYROZ: ");
    Serial.println(myIMU.readFloatGyroZ(), 4);

    // Read temperature data from LSM6DS3TR
    Serial.print("Temp (°C): ");
    Serial.println(myIMU.readTempC(), 4);

    I2CMux.closeChannel(1);

    delay(2000); // Wait before the next loop iteration
}
```
