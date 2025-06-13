---
slug: /accelerometer-gyroscope/arduino/troubleshooting 
title: LSM6DS – Troubleshooting
id: accelerometer-gyroscope-arduino-5
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
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The LSM6DS3 6-DOF uses the **fixed I2C address 0x6A**, so verify that no other device is using this address.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `lsm6ds3.begin_I2C()` again in your code or resetting your microcontroller with `NVIC_SystemReset();`. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My sensor won't read or display data!">

#### Adjust Output Data Rate
Set an appropriate Output Data Rate (ODR) for the accelerometer and gyroscope. Low ODRs (e.g., 13Hz) are suitable for slow applications, while high ODRs (e.g., 104Hz or above) are better for real-time motion tracking.

##### Example:
```cpp
uint8_t dataToWrite = LSM6DS3_ACC_GYRO_ODR_XL_104Hz; // Set accelerometer ODR to 104Hz
```

#### Configure Full-Scale Range
Set the full-scale range for the accelerometer and gyroscope based on application requirements. **Accelerometer** ranges: ±2g, ±4g, ±8g, ±16g, while **Gyroscope** ranges: ±125dps, ±250dps, ±500dps, ±1000dps, ±2000dps.

##### Example:
```cpp
uint8_t dataToWrite = LSM6DS3_ACC_GYRO_FS_XL_8g; // Set accelerometer range to ±8g
dataToWrite = LSM6DS3_ACC_GYRO_FS_G_500dps; // Set gyroscope range to ±500dps
```

#### Enable Embedded Functions
Activate embedded functions such as pedometer, tilt detection, or interrupts to allow the device to return the wanted data.

##### Example:
```cpp
myIMU.writeRegister(LSM6DS3_ACC_GYRO_CTRL10_C, 0x3E); // Enable embedded functions
```

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>