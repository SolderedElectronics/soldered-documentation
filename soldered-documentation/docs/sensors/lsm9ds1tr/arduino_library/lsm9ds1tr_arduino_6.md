---
slug: /lsm9ds1tr/arduino/troubleshooting 
title: Troubleshooting
id: lsm9ds1tr-arduino-6 
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The LSM6DS3 6-DOF uses **0x6A** or **0x6B** for its Accelerometer and Gyroscope and **0x1C** or **0x1E** for the Magnetometer, so verify that no other device is using these addresses.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `lsm6ds3trc.begin_I2C()` again in your code or resetting your microcontroller with `NVIC_SystemReset();`. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My sensor won't read or display data!">

#### Adjust Output Data Rate
Set an appropriate **Output Data Rate (ODR)** for the accelerometer, gyroscope, and magnetometer. Low ODRs (e.g., 10 Hz) are suitable for slow applications, while higher ODRs (e.g., 119 Hz or above) are better for real-time motion tracking.
##### Example:
```cpp
uint8_t dataToWrite = LSM9DS1_ODR_XL_119Hz; // Set accelerometer ODR to 119Hz
dataToWrite = LSM9DS1_ODR_G_59_5Hz;        // Set gyroscope ODR to 59.5Hz
dataToWrite = LSM9DS1_ODR_M_20Hz;          // Set magnetometer ODR to 20Hz
```

#### Configure Full-Scale Range
Set the full-scale range for the **accelerometer**, **gyroscope**, and **magnetometer** based on application requirements.

*   **Accelerometer** ranges: ±2g, ±4g, ±8g, ±16g.
*   **Gyroscope** ranges: ±245dps, ±500dps, ±2000dps.    
*   **Magnetometer** ranges: ±4 gauss, ±8 gauss, ±12 gauss, ±16 gauss.
##### Example:
```cpp
uint8_t dataToWrite = LSM9DS1_FS_XL_8g;    // Set accelerometer range to ±8g
dataToWrite = LSM9DS1_FS_G_500dps;        // Set gyroscope range to ±500dps
dataToWrite = LSM9DS1_FS_M_12Gs;          // Set magnetometer range to ±12 gauss
```

#### Enable Embedded Functions
Activate **embedded functions** such as **interrupts** or **temperature compensation** for enhanced functionality. These features allow the device to return the desired data efficiently and improve performance in specific applications.
##### Example:
```cpp
imu.writeRegister(LSM9DS1_CTRL_REG1_M, 0x7C); // Enable magnetometer high-performance mode
imu.writeRegister(LSM9DS1_CTRL_REG6_XL, 0x70); // Configure accelerometer settings
imu.writeRegister(LSM9DS1_CTRL_REG4, 0x38);   // Enable interrupt-driven data ready signals
```
</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>