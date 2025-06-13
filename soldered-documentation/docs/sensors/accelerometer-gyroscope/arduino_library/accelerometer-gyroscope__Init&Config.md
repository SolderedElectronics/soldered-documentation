---
slug: /accelerometer-gyroscope/arduino/Initilization & Configuration
title: LSM6DS – Initialization & Configuration
id: accelerometer-gyroscope-arduino-6
hide_title: False
---

This page outlines some of the **most important initializations and configurations** available for the **LSM6DS Accelerometer & Gyroscope sensor** and its in-depth configuration ability.

---

## Initialization 

To start using the LSM6DS3 Accelerometer & Gyroscope sensor, we need to include the required library `#include "LSM6DS3-SOLDERED.h"` and then initialize the sensor `myIMU.begin();` by configuring its communication protocol (I2C or SPI) and setting up its registers for operation. This process ensures proper data acquisition for motion tracking, temperature monitoring, and interrupt-driven events.

Any reference to `LSM6DS3` is made due to it being the base for Arduino code. The code itself still works on all devices this documentation is for, and this naming should not worry the user.

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

    // Call .begin() to configure the IMU
    myIMU.begin();
}
//...
```

---

## Configuration

The **LSM6DS Accelerometer & Gyroscope sensor** is configured by writing **specific values to its control registers**, which set the operating modes, full-scale ranges, and output data rates for both the accelerometer and gyroscope. This configuration process typically involves selecting **low-power** or **high-performance** modes and **fine-tuning filtering** and calibration settings to match the application's requirements. **Communication** with the sensor is handled via **I2C** or **SPI**, ensuring that the initialization sequence properly sets up the sensor for accurate motion detection and orientation tracking. **Some configuration options are shown below**.

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
    delay(1000); 

    // Call .begin() to configure the IMU
    myIMU.begin();

    // Configure accelerometer
    lsm6ds3trc.setAccelRange(LSM6DS_ACCEL_RANGE_2_G);
    lsm6ds3trc.setAccelDataRate(LSM6DS_RATE_104_HZ);

    // Configure gyroscope
    lsm6ds3trc.setGyroRange(LSM6DS_GYRO_RANGE_250_DPS);
    lsm6ds3trc.setGyroDataRate(LSM6DS_RATE_104_HZ);

    // Enable data ready interrupts
    lsm6ds3trc.configInt1(false, false, true);  // accelerometer DRDY on INT1
    lsm6ds3trc.configInt2(false, true, false);  // gyro DRDY on INT2

}
//...
```

---

## Different Setting Options

### Initialize the LSM6DS3 sensor with default or user-defined settings

```cpp
status_t begin(SensorSettings* pSettingsYouWanted = NULL);
//Initializes the LSM6DS3 sensor with default or user-defined settings for accelerometer, gyroscope, and communication mode.
```

### Adjust accelerometer bandwidth

```cpp
dataToWrite = LSM6DS3_ACC_GYRO_BW_XL_400Hz ;
```

<FunctionDocumentation
  functionName="LSM6DS3_ACC_GYRO_BW_XL_400Hz"
  description="Sets the accelerometer bandwidth to 400 Hz, allowing high-frequency signals to pass through for fast-moving applications."
  returnDescription="No direct return value; this value is used to configure the sensor's CTRL1_XL register."
  parameters={[]}
/>

| Bandwidth Setting                  | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| `LSM6DS3_ACC_GYRO_BW_XL_400Hz`     | Sets the accelerometer bandwidth to **400 Hz**, allowing high-frequency signals to pass through. Ideal for fast-moving applications like drone stabilization. |
| `LSM6DS3_ACC_GYRO_BW_XL_200Hz`     | Sets the accelerometer bandwidth to **200 Hz**, filtering out higher frequencies while maintaining responsiveness for medium-speed movements. |
| `LSM6DS3_ACC_GYRO_BW_XL_100Hz`     | Sets the accelerometer bandwidth to **100 Hz**, filtering noise effectively for slower movements or applications requiring smoother data. |
| `LSM6DS3_ACC_GYRO_BW_XL_50Hz`      | Sets the accelerometer bandwidth to **50 Hz**, heavily filtering high-frequency noise. Suitable for applications with very slow-moving objects or static measurements. |

### Monitor data input number

```cpp
LSM6DS3_ACC_GYRO_INT1_FTH_DISABLED = 0x00,
```

<FunctionDocumentation
  functionName="LSM6DS3_ACC_GYRO_INT1_FTH_t"
  description="Configures the FIFO threshold interrupt on the INT1 pin of the LSM6DS3 sensor."
  returnDescription="No direct return value; this setting is used to enable or disable the FIFO threshold interrupt."
  parameters={[]}
/>

| Command                                | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| `LSM6DS3_ACC_GYRO_INT1_FTH_DISABLED`   | Disables the FIFO threshold interrupt on the INT1 pin.                      |
| `LSM6DS3_ACC_GYRO_INT1_FTH_ENABLED`    | Enables the FIFO threshold interrupt on the INT1 pin.                       |

### Define data update rate

```cpp
LSM6DS3_ACC_GYRO_ODR_XL_13Hz = 0x10,
```

<FunctionDocumentation
  functionName="LSM6DS3_ACC_GYRO_ODR_XL_t"
  description="Configures the output data rate (ODR) of the accelerometer in the LSM6DS3 sensor."
  returnDescription="No direct return value; this setting is used to configure the sensor's CTRL1_XL register."
  parameters={[]}
/>

| Command                                | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| `LSM6DS3_ACC_GYRO_ODR_XL_POWER_DOWN`   | Disables the accelerometer.                                                 |
| `LSM6DS3_ACC_GYRO_ODR_XL_13Hz`         | Sets the accelerometer output data rate (ODR) to **13 Hz** for slow measurements. |
| `LSM6DS3_ACC_GYRO_ODR_XL_26Hz`         | Sets the accelerometer output data rate (ODR) to **26 Hz** for moderate-speed measurements. |
| `LSM6DS3_ACC_GYRO_ODR_XL_52Hz`         | Sets the accelerometer output data rate (ODR) to **52 Hz** for faster measurements. |
| `LSM6DS3_ACC_GYRO_ODR_XL_104Hz`        | Sets the accelerometer output data rate (ODR) to **104 Hz** for real-time applications. |
| `LSM6DS3_ACC_GYRO_ODR_XL_208Hz`        | Sets the accelerometer output data rate (ODR) to **208 Hz** for high-speed applications. |
| `LSM6DS3_ACC_GYRO_ODR_XL_416Hz`        | Sets the accelerometer output data rate (ODR) to **416 Hz** for very fast measurements. |
| `LSM6DS3_ACC_GYRO_ODR_XL_833Hz`        | Sets the accelerometer output data rate (ODR) to **833 Hz** for extremely fast measurements. |
| `LSM6DS3_ACC_GYRO_ODR_XL_1660Hz`       | Sets the accelerometer output data rate (ODR) to **1660 Hz** for ultra-high-speed applications. |
| `LSM6DS3_ACC_GYRO_ODR_XL_3330Hz`       | Sets the accelerometer output data rate (ODR) to **3330 Hz** for specialized high-speed applications. |
| `LSM6DS3_ACC_GYRO_ODR_XL_6660Hz`       | Sets the accelerometer output data rate (ODR) to **6660 Hz** for extreme high-speed applications. |
| `LSM6DS3_ACC_GYRO_ODR_XL_13330Hz`      | Sets the accelerometer output data rate (ODR) to **13330 Hz** for maximum speed applications. |

### Wake-up detection status (example specifically for the Y-axis of the accelerometer)

```cpp
LSM6DS3_ACC_GYRO_Y_WU_NOT_DETECTED = 0x00,
```

<FunctionDocumentation
  functionName="LSM6DS3_ACC_GYRO_Y_WU_t"
  description="Represents the wake-up detection status for the Y-axis in the LSM6DS3 sensor."
  returnDescription="No direct return value; this enum is used to interpret the sensor's wake-up detection status."
  parameters={[]}
/>

| Command                              | Description                                                           |
|--------------------------------------|-----------------------------------------------------------------------|
| `LSM6DS3_ACC_GYRO_Y_WU_NOT_DETECTED` | Indicates that no wake-up event has been detected on the Y-axis.      |
| `LSM6DS3_ACC_GYRO_Y_WU_DETECTED`     | Indicates that a wake-up event has been detected on the Y-axis.       |

### Define 6D orientation detection angle

```cpp
LSM6DS3_ACC_GYRO_SIXD_THS_80_degree = 0x00, 
```

<FunctionDocumentation
  functionName="LSM6DS3_ACC_GYRO_SIXD_THS_t"
  description="Configures the threshold angle for the 6D (six directions) orientation detection feature in the LSM6DS3 sensor."
  returnDescription="No direct return value; this enum is used to set the threshold in the sensor's configuration registers."
  parameters={[]}
/>

| Command                                | Description                                                   |
|----------------------------------------|---------------------------------------------------------------|
| `LSM6DS3_ACC_GYRO_SIXD_THS_80_degree`  | Sets the 6D orientation detection threshold to **80 degrees** |
| `LSM6DS3_ACC_GYRO_SIXD_THS_70_degree`  | Sets the 6D orientation detection threshold to **70 degrees** |
| `LSM6DS3_ACC_GYRO_SIXD_THS_60_degree`  | Sets the 6D orientation detection threshold to **60 degrees** |
| `LSM6DS3_ACC_GYRO_SIXD_THS_50_degree`  | Sets the 6D orientation detection threshold to **50 degrees** |

---

## Full Setup (default settings)

This section outlines the default settings when initializing the sensor. It can be helpful to refer to these if you wish to modify some of the settings during your project.

```cpp
// Include libraries
#include "LSM6DS3-SOLDERED.h"
#include "Wire.h"

uint16_t errorsAndWarnings = 0;

// Create object from LSM library
Soldered_LSM6DS3 myIMU; // Default address is 0x6B

void setup()
{
    // Put your setup code here, to run once:

    // Init serial communication
    Serial.begin(115200);
    delay(1000); // Relax...
    Serial.print("The sketch started - ");

    // Call .beginCore() to configure the IMU
    if (myIMU.beginCore() != 0)
    {
        Serial.println("Error at beginCore().");
    }
    else
    {
        Serial.println("beginCore() passed.");
    }

    uint8_t dataToWrite = 0; // Temporary variable

    // Setup the accelerometer******************************
    dataToWrite = 0; // Start Fresh!
    dataToWrite |= LSM6DS3_ACC_GYRO_BW_XL_100Hz;
    dataToWrite |= LSM6DS3_ACC_GYRO_FS_XL_8g;
    dataToWrite |= LSM6DS3_ACC_GYRO_ODR_XL_104Hz;

    // Now, write the patched together data
    errorsAndWarnings += myIMU.writeRegister(LSM6DS3_ACC_GYRO_CTRL1_XL, dataToWrite);

    // Set the ODR bit
    errorsAndWarnings += myIMU.readRegister(&dataToWrite, LSM6DS3_ACC_GYRO_CTRL4_C);
    dataToWrite &= ~((uint8_t)LSM6DS3_ACC_GYRO_BW_SCAL_ODR_ENABLED);
}

void loop()
{
    int16_t temp;
    // Get all parameters
    Serial.print("\nAccelerometer Counts:\n");
    Serial.print(" X = ");

    // Read a register into the temp variable.
    if (myIMU.readRegisterInt16(&temp, LSM6DS3_ACC_GYRO_OUTX_L_XL) != 0)
    {
        errorsAndWarnings++;
    }
    Serial.println(temp);
    Serial.print(" Y = ");

    // Read a register into the temp variable.
    if (myIMU.readRegisterInt16(&temp, LSM6DS3_ACC_GYRO_OUTY_L_XL) != 0)
    {
        errorsAndWarnings++;
    }
    Serial.println(temp);
    Serial.print(" Z = ");

    // Read a register into the temp variable.
    if (myIMU.readRegisterInt16(&temp, LSM6DS3_ACC_GYRO_OUTZ_L_XL) != 0)
    {
        errorsAndWarnings++;
    }
    Serial.println(temp);

    Serial.println();
    Serial.print("Total reported Errors and Warnings: ");
    Serial.println(errorsAndWarnings);

    delay(1000);
}
```

<QuickLink 
  title="lowLevelExample.ino" 
  description="Example using the LSM6DS3 with ONLY read and write methods."
  url="https://github.com/SolderedElectronics/Soldered-LSM6DS3-Arduino-Library/blob/main/examples/LowLevelExample/LowLevelExample.ino" 
/>

--- 

## In-depth Initialization & Configuration list

For an in-depth look at all available commands, refer to the code given below.  

<QuickLink  
  title="SparkFunLSM6DS3.h"  
  description="Detailed list of various commands for initialization and configuration of the LSM6DS3 6-DOF"  
  url="https://github.com/SolderedElectronics/Soldered-LSM6DS3-Arduino-Library/blob/main/src/libs/SparkFun_LSM6DS3_Arduino_Library/src/SparkFunLSM6DS3.h"  
/>