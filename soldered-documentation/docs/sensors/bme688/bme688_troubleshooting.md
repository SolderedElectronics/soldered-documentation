---
slug: /bme688/arduino/troubleshooting 
title: BME688 Environmental Sensor - Troubleshooting
sidebar_label: Troubleshooting
id: bme688-troubleshooting
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments. Test

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The BME680 uses the **fixed I2C address 0x76**, so verify that no other device is using this address.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `bme688.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="The temperature readings aren't accurate!">

#### Add an offset
Because the sensor by itself generates heat, a temperature offset may be needed. You must find an independent temperature reading and apply the offset to the temperature value if needed

</ExpandableSection>

<ExpandableSection title="The gas readings are all over the place!">

#### Take "Dummy" sensor readings
Because of the way the gas sensor works, taking infrequent readings may make them inaccurate. To combat this, take readings more frequently, even if you don't plan on using the values

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>