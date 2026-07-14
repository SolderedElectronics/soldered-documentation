---
slug: /ads1219/arduino/troubleshooting 
title: ADS1219 24-bit ADC - Troubleshooting
sidebar_label: Troubleshooting
id: ads1219-arduino-6 
hide_title: False
pagination_next: null
---

This page contains some tips if you are having problems using this product.

<ExpandableSection title="My ADS1219 won't initialize!">

#### Check wiring
Make sure your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic (formerly easyC)-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Check your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the ADS1219 is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller's I2C bus.

#### Check for conflicting I2C addresses
If you have multiple I2C devices on the same bus, make sure none share the same address. The ADS1219 default address is **0x40** - verify no other device is using this address, or reconfigure the address via the onboard jumpers.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `adc.begin()` again or resetting your microcontroller. Some initialization issues are resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="My readings are always 0 or incorrect!">

#### Check the input wiring
Verify that your signal source is correctly connected to the AIN pins. For single-ended measurements, make sure the signal is connected to the correct channel (AIN0-AIN3) and that GND is shared between the signal source and the board.

#### Check the gain setting
If the input signal is larger than the selected gain range allows, the ADC will saturate and return the maximum or minimum value. For example, with `ADS1219_GAIN_1` and the internal 2.048 V reference, the input must stay within ±2.048 V. Reduce the gain or use a lower reference voltage accordingly.

#### Make sure you call start()
In both single-shot and continuous modes, `adc.startSync()` must be called to begin conversions. Without it, `readConversion()` will return stale or zero data.

#### Wait for data to be ready
Always check `adc.dataReady()` before calling `adc.readConversion()`. Reading before a conversion completes will return the previous result or invalid data.

#### Check the voltage reference
If you are using an external voltage reference (`ADS1219_VREF_EXTERNAL`), make sure a valid reference voltage is applied to the REFP and REFN pins. An unconnected or incorrect reference will produce inaccurate results.

</ExpandableSection>

<ExpandableSection title="My continuous mode stops producing new results!">

#### Check the data rate and polling speed
In continuous mode, new results are produced at the configured data rate (e.g. 90 SPS = one result every ~11 ms). If your loop is faster than the data rate, `dataReady()` will return false until the next sample is ready - this is normal behaviour.

#### Verify the DRDY pin connection
If you are using the DRDY interrupt pin instead of polling, make sure it is connected to a valid digital input on your microcontroller and that the pin is configured as `INPUT` or `INPUT_PULLUP` in your code.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>












