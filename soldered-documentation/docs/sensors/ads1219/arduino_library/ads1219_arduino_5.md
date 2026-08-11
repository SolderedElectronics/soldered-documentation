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

<ExpandableSection title="My readings are noisy or drifting!">

#### Give a bench supply a load and time to warm up
A bench supply feeding the ADS1219 is running almost unloaded, because the reference input draws about 10 nA and the analog inputs are buffered. With nothing to regulate against, the supply's output wanders. Fitting a resistor between 470 Ω and 2.2 kΩ across the supply's output terminals took our noise from 150 mV of wander down to 0.112 mV. Give it a few minutes to settle too: straight after switch-on ours climbed about 5 mV in 10 seconds. A reading that moves steadily in one direction is warm-up drift rather than noise.

#### Measure the converter's own noise floor
Tie a channel directly to GND and read it with the matching `ADS1219_MUX_SINGLE_x` setting. That measures the ADC against itself, with your signal source out of the picture. Expect a few tens of microvolts: ours held within 22 µV of zero, against the datasheet figure of 19.71 µV peak-to-peak at 20 SPS and gain 1. If a grounded channel is far worse than that, the problem is upstream of the chip in the grounding, the lead dress or a marginal solder joint, and no amount of averaging in software will recover it.

#### Use a lower data rate
Noise rises with data rate because there is less time to average between conversions. At 20 SPS and gain 1 the effective resolution is about 19.6 bits; at 1000 SPS it drops to roughly 16.8 bits. If you don't need the speed, `ADS1219_DR_20SPS` is the quietest setting and the default.

#### Keep the leads short
At 24 bits, half a metre of unshielded wire is an antenna. Twist each signal wire together with its ground return and keep both as short as practical.

</ExpandableSection>

<ExpandableSection title="My external reference doesn't seem to be used!">

#### Read the configuration register back
`adc.getConfigReg()` returns the register the chip is actually running on. The `vref` bit must read 1 for an external reference. If it reads 0 the device is still on the internal 2.048 V reference and nothing downstream will be correct.

```cpp
ads1219_config_reg_t cfg;
if (adc.getConfigReg(cfg))
{
    Serial.print("vref bit = ");
    Serial.println(cfg.vref); // 1 = external, 0 = internal
}
```

#### Check REFN is grounded and the voltage is in range
The ADS1219 measures REFP and REFN against its own internal ground, so an external source left floating has no defined level relative to the chip. Tie REFN to the board's GND. The reference itself has to sit between 0.75 V and AVDD.

#### Compare the same input against two references
Read one unchanged signal twice, once with `ADS1219_VREF_INTERNAL` and `getConversionMillivolts(2048.0f)`, then again with your external reference and its measured value. The raw code must change by the ratio of the two references while the reported millivolts stay put. If the raw code doesn't move at all, the external reference is not being applied.

</ExpandableSection>

<ExpandableSection title="My continuous mode stops producing new results!">

#### Check the data rate and polling speed
In continuous mode, new results are produced at the configured data rate (e.g. 90 SPS = one result every ~11 ms). If your loop is faster than the data rate, `dataReady()` will return false until the next sample is ready - this is normal behaviour.

#### Verify the DRDY pin connection
If you are using the DRDY interrupt pin instead of polling, make sure it is connected to a valid digital input on your microcontroller and that the pin is configured as `INPUT` or `INPUT_PULLUP` in your code.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link, or ask on the [**Soldered community**](https://community.soldered.com), a great place to browse existing questions or post your own.</InfoBox>












