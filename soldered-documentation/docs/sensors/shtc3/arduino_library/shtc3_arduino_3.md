---
slug: /shtc3/arduino/troubleshooting 
title: Troubleshooting
id: shtc3-arduino-3 
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments. Test

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The SHTC3 uses the **fixed I2C address 0x70**, so verify that no other device is using this address.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `shtcSensor.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My sensor is not detecting properly!">

### Check sensor placement
Ensure that your APDS9960 sensor is positioned correctly with a clear line of sight for proximity and gesture detection. Obstructions or a poor angle can interfere with the sensor's ability to detect motion or proximity.

### Adjust sensitivity settings
If the sensor is not detecting gestures or proximity accurately, try adjusting the sensitivity settings. The default settings might be too low or high depending on your environment. Experiment with different configurations to find the optimal setting for your application.

### Verify proper I2C connection
Double-check your I2C wiring and ensure the sensor is properly connected. If you're using an I2C interface, verify that the SDA and SCL pins are correctly connected to your microcontroller. A common issue can be incorrect wiring, so double-check each pin assignment.

### Scan for I2C devices
Run an I2C scanner sketch to ensure the sensor is detected on the I2C bus. If the scanner cannot detect the sensor, verify the wiring, check for pull-up resistors, and make sure the correct I2C address (usually 0x39) is being used in your code.

### Test the sensor in a different environment
The APDS9960 sensor's performance can be affected by ambient lighting conditions. If you’re in a very bright or very dark room, try moving to an area with more moderate lighting. The sensor is designed for indoor use and might struggle in extreme lighting conditions.

### Reinitialize the sensor
If the sensor is still not working after your initial setup, try reinitializing it by calling the appropriate initialization function in your code (e.g., sensor.begin()). Sometimes the sensor may fail to initialize properly on the first attempt, and a second try can resolve the issue.

</ExpandableSection>


<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>