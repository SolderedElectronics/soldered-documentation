---
slug: /apds-9960/arduino/troubleshooting
title: Apds 9960 - Troubleshooting
id: apds-9960-arduino-6
hide_title: false
pagination_next: null
---

This page contains some tips if you are experiencing problems with this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The APDS-9960 uses the **fixed I2C address 0x39,** so verify that no other device is using this address.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `APDS.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My sensor is not detecting properly!">

#### Check sensor placement
Ensure that your APDS-9960 sensor is positioned correctly with a clear line of sight for proximity and gesture detection. Obstructions or a poor angle can interfere with the sensor's ability to detect motion or proximity.

<InfoBox> If you're using glass over your sensor, make sure you [leave an adequate gap of 1mm](/apds-9960/hardware#window-air-gap/)! </InfoBox>

#### Adjust sensitivity settings
If the sensor is not detecting gestures or proximity accurately, try adjusting the sensitivity settings. The default settings might be too low or too high depending on your environment. Experiment with different configurations to find the optimal setting for your application.

#### Verify proper I2C connection
Double-check your I2C wiring and ensure the sensor is properly connected. If you're using an I2C interface, verify that the SDA and SCL pins are correctly connected to your microcontroller. A common issue can be incorrect wiring, so double-check each pin assignment.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Test the sensor in a different environment
The APDS-9960 sensor's performance can be affected by ambient lighting conditions. If you’re in a very bright or very dark room, try moving to an area with more moderate lighting. The sensor is designed for indoor use and might struggle in extreme lighting conditions.

#### Reinitialize the sensor
If the sensor is still not working after your initial setup, try reinitializing it by calling `APDS.begin()`. Sometimes the sensor may fail to initialize properly on the first attempt, and a second try can resolve the issue.

</ExpandableSection>

<ExpandableSection title="Other common issues">

#### My sensor is not detecting all gesture types (e.g., up, down, left, right)
Check Gesture Mode  
Ensure that the gesture mode is properly enabled in your code. The APDS-9960 supports multiple modes, including gesture detection. If gesture recognition is not activated, the sensor may not detect gestures properly.

#### Adjust Gesture Sensitivity
Gesture detection relies on proper sensitivity settings. If gestures aren’t being detected, try adjusting the gesture sensitivity to a higher or lower value depending on your environment.

#### Test Gestures in a Controlled Space
Make sure you are performing gestures within the correct range and angle that the sensor can effectively detect. Too much ambient light or small, quick movements might affect detection accuracy.

#### Sensor data is inaccurate or fluctuating
Verify Power Supply  
Inconsistent or fluctuating power supply can lead to unreliable readings. Make sure the sensor is receiving a stable voltage and that your microcontroller is providing sufficient power to the sensor.

#### Sensor doesn't respond after firmware update
Revert to Previous Version  
If you recently updated the firmware of your microcontroller or sensor and the issue arose afterward, it might be worth trying to revert to an earlier firmware version to see if the problem persists.

#### Check for Compatibility Issues
Ensure that any libraries you are using are compatible with the version of the APDS-9960 you have. Sometimes, a new version of a library might have bugs or may not be fully compatible with all hardware revisions.

#### Sensor response time is slow
Adjust Integration Time  
The APDS-9960 sensor uses an integration time for ambient light and proximity detection. If the response time seems slow, you might want to reduce the integration time, though this might come at the expense of sensor accuracy.

#### Optimize Your Code
If the sensor works but the response time is slow, consider optimizing your code. For example, ensure you’re not performing unnecessary operations within your loop and that you're reading sensor data efficiently.

#### APDS-9960 sensor is getting hot
Check Power and Usage  
If the sensor is getting unusually warm, this could indicate a power supply issue or excessive current draw. Ensure that your microcontroller is providing the correct voltage (typically 3.3V or 5V, depending on the variant of the APDS-9960) and that the power supply is stable.

#### No color detection
Proper Light Conditions  
If the color sensing feature is not working as expected, make sure the environment has proper lighting. The APDS-9960 works best under standard indoor lighting and might struggle in dim or overly bright conditions.

#### Verify the LED Functionality
If the color sensor is not detecting properly, check if the sensor’s LED is functioning. The LED helps the sensor determine color, and if it's not emitting light correctly, the sensor won't be able to detect color.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>