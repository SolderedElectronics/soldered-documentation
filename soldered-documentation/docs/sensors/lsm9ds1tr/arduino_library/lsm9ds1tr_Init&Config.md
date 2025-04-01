---
slug: /lsm9ds1tr/arduino/init-and-configuration
title: Initialization & Configuration
id: lsm9ds1tr-arduino-init-config
hide_title: False
---

This page outlines some of the **most important initializations and configurations** available for the **LSM9DS1 Accelerometer & Gyroscope sensor** and its in-depth configuration ability.

---

## Initialization

To start using the **LSM9DS1 Accelerometer, Gyroscope & Magnetometer sensor**, include the required library `#include "LSM9DS1TR-SOLDERED.h"` and initialize the sensor using `imu.begin();`. This process ensures proper communication (**I2C** or **SPI**) and configures the registers for operation. Below is an example of basic initialization:

```cpp
// Include libraries
#include "LSM9DS1TR-SOLDERED.h"
#include "Wire.h"

// Create an LSM9DS1TR object
LSM9DS1TR imu; // Default I2C addresses: 0x6B (AG) and 0x1E (M)

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);
    delay(1000); // Relax...

    // Initialize sensor
    if (!imu.begin())
    {
        Serial.println("Can't initialize LSM9DS1!");
        Serial.println("Check connection!");
        while (true)
            ;
    }

    Serial.println("LSM9DS1 initialized successfully.");
}
//...
```
---

## Configuration

The **LSM9DS1** offers extensive configuration options for its accelerometer, gyroscope, magnetometer, and temperature sensors. These configurations allow you to set full-scale ranges, output data rates (ODR), bandwidths, and enable/disable specific features. Below are examples of common configurations:

### Configure Accelerometer

```cpp
void setupAccel()
{
    imu.settings.accel.enabled = true;       // Enable accelerometer
    imu.settings.accel.scale = 8;           // Set scale to ±8g
    imu.settings.accel.sampleRate = 3;      // Set ODR to 119 Hz
    imu.settings.accel.bandwidth = 0;       // Set bandwidth to max (408 Hz)
}
//...
```
---

### Configure Temperature Sensor

```cpp
void setupTemperature()
{
    imu.settings.temp.enabled = true;            // Enable temperature sensor
}
//...
```
---

### Configure Gyroscope

```cpp
void setupGyro()
{
    imu.settings.gyro.enabled = true;       // Enable gyroscope
    imu.settings.gyro.scale = 245;         // Set scale to ±245 dps
    imu.settings.gyro.sampleRate = 3;      // Set ODR to 119 Hz
    imu.settings.gyro.bandwidth = 0;       // Set bandwidth to max
}
//...
```
---

### Configure Magnetometer

```cpp
void setupMag()
{
    imu.settings.mag.enabled = true;             // Enable magnetometer
    imu.settings.mag.scale = 12;                 // Set scale to ±12 Gauss
    imu.settings.mag.sampleRate = 5;             // Set ODR to 20 Hz
    imu.settings.mag.XYPerformance = 3;          // Ultra-high performance for X/Y axes
    imu.settings.mag.ZPerformance = 3;           // Ultra-high performance for Z axis
}
//...
```
---

## Different Advanced Settings 

| **Sensor**         | **Parameter**            | **Description**                                                                 |
|---------------------|--------------------------|---------------------------------------------------------------------------------|
| **Accelerometer**   | `enabled`               | Enables or disables the accelerometer.                                         |
|                     | `enableX/Y/Z`           | Enables or disables individual axes (X, Y, Z).                                 |
|                     | `scale`                 | Full-scale range: ±2g, ±4g, ±8g, ±16g.                                         |
|                     | `sampleRate`            | Output data rate (ODR): 10 Hz to 952 Hz.                                       |
|                     | `bandwidth`             | Anti-aliasing filter bandwidth: Max (408 Hz) or reduced (50–211 Hz).           |
|                     | `highResEnable`         | Enables high-resolution mode for smoother data.                                |
|                     | `highResBandwidth`      | Low-pass cutoff frequency in high-res mode: ODR/50 to ODR/400.                 |
| **Gyroscope**       | `enabled`               | Enables or disables the gyroscope.                                             |
|                     | `scale`                 | Full-scale range: ±245 dps, ±500 dps, ±2000 dps.                               |
|                     | `sampleRate`            | Output data rate (ODR): 14.9 Hz to 952 Hz.                                     |
|                     | `bandwidth`             | Cutoff frequency based on sample rate.                                         |
|                     | `lowPowerEnable`        | Enables low-power mode for reduced energy consumption.                         |
|                     | `HPFEnable`             | Enables or disables the high-pass filter (HPF).                                |
|                     | `HPFCutoff`             | Sets HPF cutoff frequency: 0–9 (depends on ODR).                               |
|                     | `flipX/Y/Z`             | Flips the orientation of X, Y, or Z axes.                                      |
| **Magnetometer**    | `enabled`               | Enables or disables the magnetometer.                                          |
|                     | `scale`                 | Full-scale range: ±4 Gauss, ±8 Gauss, ±12 Gauss, ±16 Gauss.                    |
|                     | `sampleRate`            | Output data rate (ODR): 0.625 Hz to 80 Hz.                                     |
|                     | `tempCompensationEnable`| Enables temperature compensation for better accuracy.                          |
|                     | `XYPerformance/ZPerformance` | Performance modes: Low power to ultra-high performance.                        |
|                     | `lowPowerEnable`        | Enables low-power mode for reduced energy consumption.                         |
|                     | `operatingMode`         | Operating modes: Continuous conversion, single-conversion, power down.         |
| **Temperature**     | `enabled`               | Enables or disables the temperature sensor.                                    |

---

## Full Setup (default settings)

This section outlines the default settings when initializing the sensor. It can be helpful to refer to these if you wish to modify some of the settings during your project.

```cpp
#include "LSM9DS1TR-SOLDERED.h"
#include "Wire.h"

LSM9DS1TR imu;

void setup()
{
    Serial.begin(115200);
    Wire.begin();

    if (!imu.begin())
    {
        Serial.println("Failed to initialize LSM9DS1!");
        while (true)
            ;
    }

    setupAccel();
    setupGyro();
    setupMag();
    setupTemperature();

    Serial.println("LSM9DS1 configured successfully.");
}

void loop()
{
    if (imu.accelAvailable())
        imu.readAccel();

    if (imu.gyroAvailable())
        imu.readGyro();

    if (imu.magAvailable())
        imu.readMag();

    if (imu.tempAvailable())
        imu.readTemp();

    Serial.print("Accelerometer: ");
    Serial.print(imu.calcAccel(imu.ax), 4);
    Serial.print(", ");
    Serial.print(imu.calcAccel(imu.ay), 4);
    Serial.print(", ");
    Serial.println(imu.calcAccel(imu.az), 4);

    Serial.print("Gyroscope: ");
    Serial.print(imu.calcGyro(imu.gx), 4);
    Serial.print(", ");
    Serial.print(imu.calcGyro(imu.gy), 4);
    Serial.print(", ");
    Serial.println(imu.calcGyro(imu.gz), 4);

    Serial.print("Magnetometer: ");
    Serial.print(imu.calcMag(imu.mx), 4);
    Serial.print(", ");
    Serial.print(imu.calcMag(imu.my), 4);
    Serial.print(", ");
    Serial.println(imu.calcMag(imu.mz), 4);

    Serial.print("Temperature: ");
    Serial.println(imu.temperature);

    delay(500);
}

```

---

## In-depth Initialization & Configuration List

For an in-depth look at all available commands, refer to the code given below.  

<QuickLink  
  title="LSM9DS1_Settings.ino"  
  description="Detailed list of various commands for initialization and configuration of the LSM9DS1TR 9-DOF"  
  url="https://github.com/SolderedElectronics/Soldered-LSM9DS1TR-Arduino-Library/blob/main/examples/LSM9DS1_Settings/LSM9DS1_Settings.ino"  
/>