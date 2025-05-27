---
slug: /pcf85063a/arduino/troubleshooting
title: "PCF85063A RTC \u2013 Arduino troubleshooting"
id: pcf85063a-arduino-3
hide_title: false
pagination_next: null
---
This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My RTC won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The PCF85063A uses the **fixed I2C address 0x51**, so verify that no other device is using this address.

#### Try reinitializing
If the RTC fails to initialize on the first attempt, try calling `rtc.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>