---
slug: /slider-potentiometer/troubleshooting
title: "Slider Potentiometer \u2013 Troubleshooting"
id: slider-potentiometer-arduino-4
hide_title: false
pagination_next: null
---
This page contains some tips if you are having problems using this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller’s I2C bus.

</ExpandableSection>

<InfoBox>If you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>