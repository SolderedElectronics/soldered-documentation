---
slug: /pir-sensor/arduino/troubleshooting
title: Pir Sensor - Troubleshooting
sidebar_label: Troubleshooting
id: pir-sensor-arduino-3
hide_title: false
pagination_next: null
---

This page contains some tips in case you are experiencing problems using this product.

<ExpandableSection title="My sensor won't initialize! (Qwiic)">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `PIR.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My sketch won't upload! (Regular)">

The sensor might be drawing too much power when uploading a sketch.

#### Disconnect the wires connected to the sensor
Before uploading the sketch, disconnect the wires connected to the sensor.

#### Connect an external battery
Connect an external battery so that the board receives enough power.

</ExpandableSection>