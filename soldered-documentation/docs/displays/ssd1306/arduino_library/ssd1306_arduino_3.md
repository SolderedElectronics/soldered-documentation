---
slug: /ssd1306/arduino/troubleshooting
title: "SSD1306 \u2013 Arduino troubleshooting"
id: ssd1306-arduino-3
hide_title: false
pagination_next: null
---
This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My Display won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. The SSD1306 uses the **fixed I2C address 0x3C**, so verify that no other device is using this address.

#### Try reinitializing
If the display fails to initialize on the first attempt, try calling `display.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My Display is displaying static">

#### Call the display() function
If the function is called **before drawing anything**, you should see the soldered logo on the screen.

#### Check connection
The I2C connection may be loose, so that it is giving power to the display but not establishing a stable communication channel to send data. Troubleshoot using the **My Display won't initialize!** section.

</ExpandableSection>

<ExpandableSection title="My Display has ghosting or burn-in">

#### Refresh the screen frequently
OLED displays can experience ghosting or burn-in if a static image remains on the screen for too long. Periodically refresh the screen or implement a screen saver function.

#### Reduce display brightness
Running the OLED display at full brightness for extended periods can accelerate ghosting. Lower the brightness using `display.dim(bool dim)` where setting `dim` to 1 dims the display so that it's almost turned off.

#### Clear the buffer before updating
Make sure to clear the display buffer using `display.clearDisplay();` before drawing new content to prevent unwanted artifacts.

#### Power cycle the display
If ghosting persists, try turning the display off for a few hours to allow residual charge to dissipate.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>