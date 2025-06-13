---
slug: /bmp180/arduino/troubleshooting
title: Bmp180 - Troubleshooting
sidebar_label: Troubleshooting
id: bmp180-arduino-3
hide_title: false
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The SHTC3 uses the **fixed I2C address 0x77**, so verify that no other device is using this address.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `bmp180.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="The temperature readings aren't accurate!">

#### Add an offset
Because the sensor by itself generates heat, a temperature offset may be needed. You must find an independent temperature reading and apply the offset to the temperature value if needed.

#### Get the measurement right after reading it
Taking too long to call `getTemperature()` after calling `startTemperature()` may result in inaccurate readings, it is best to get the values right after the small reading delay.

</ExpandableSection>

<ExpandableSection title="The pressure readings aren't accurate!">

#### Calculate relative pressure
Depending on your altitude, the pressure may be different than expected, with an altitude above 50m, it is recommended to get the relative pressure by calling the `sealevel()` function.

#### Get the measurement right after reading it
Taking too long to call `getTemperature()` after calling `startTemperature()` may result in inaccurate readings, it is best to get the values right after the small reading delay.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>