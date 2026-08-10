---
slug: /ads1219/arduino/troubleshooting 
title: ADS1219 24-bit ADC - Troubleshooting
sidebar_label: Troubleshooting
id: ads1219-arduino-5 
hide_title: False
pagination_next: null
---

This page contains some tips if you are having problems using this product.

<ExpandableSection title="My ADS1219 won't initialize!">

#### Check wiring
Make sure your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Check your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the ADS1219 is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller's I2C bus.

#### Check for conflicting I2C addresses
If you have multiple I2C devices on the same bus, make sure none share the same address. The ADS1219 default address is **0x40** - verify no other device is using this address, or reconfigure the address via the onboard jumpers.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `adc.begin()` again or resetting your microcontroller. Some initialization issues are resolved by a simple reboot.

If the ADC's configuration ends up in an unexpected state after some experimentation (wrong mux, gain, or data rate still set from earlier in your sketch), call `adc.reset()` first. This is a lighter touch than a full re-`begin()` or reboot, it just returns the configuration register to its defaults without re-checking the I2C connection.

</ExpandableSection>

<ExpandableSection title="My readings are always 0 or incorrect!">

#### Check the input wiring
Verify that your signal source is correctly connected to the AIN pins. For single-ended measurements, make sure the signal is connected to the correct channel (AIN0-AIN3) and that GND is shared between the signal source and the board.

#### Check the gain setting
If the input signal is larger than the selected gain range allows, the ADC will saturate and return the maximum or minimum value. For example, with `ADS1219_GAIN_1` and the internal 2.048 V reference, the input must stay within ±2.048 V. Reduce the gain or use a lower reference voltage accordingly.

The tell-tale sign is that the printed millivolt value equals your reference voltage **exactly** - `2500.000` when you passed `2500.0f`, for instance. That's `getConversionMillivolts()` reporting a raw code pinned at full scale (8388607), which means the input is at or above the top of the range rather than being measured. Printing `adc.getConversionRaw()` alongside makes it unmistakable.

<CenteredImage src="/img/ads1219/first_reading.png" alt="Serial Monitor showing a clipped reading" caption="A clipped channel: every sample reports exactly the reference voltage, with no variation at all" width="100%" />

#### Check that the input is actually connected
The board ships with unpopulated headers. A wire pushed into a plated hole without solder often makes no connection at all, and a floating analog input settles at a small steady value near 0 mV - so it looks like a working measurement of nothing. If a channel reads a stable near-zero figure that ignores your signal source, measure directly between that AIN hole and a GND hole before suspecting the code.

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

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link, or ask on the [**Soldered community**](https://community.soldered.com), a great place to browse existing questions or post your own.</InfoBox>












