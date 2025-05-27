---
slug: /electrochemical-gas-sensor/arduino/troubleshooting 
title: Troubleshooting
id: electrochemical-gas-sensor-arduino-3 
hide_title: False
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

#### Check for conflicting sensors
If you have multiple sensors connected, you must ensure that each ADS1115 has a different I2C address. You also have to connect the LMPEN pin to the GPIO pins on the board to be able to differentiate between them. You can find a detailed description in [**this example**](/electrochemical-gas-sensor/arduino/reading-from-multiple-sensors/).

</ExpandableSection>

<ExpandableSection title="The readings from the sensor are off!">

#### Create a custom configuration
Depending on your environment, you may need a different configuration than the predefined one. Check out the [**How it works**](/documentation/electrochemical-gas-sensor/how-it-works/) section as well as the [**Custom configuration example**](/documentation/electrochemical-gas-sensor/arduino/custom-config-example/).

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>