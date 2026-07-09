---
slug: /scd43/arduino/troubleshooting
title: SCD43 - Troubleshooting
sidebar_label: Troubleshooting
id: scd43-arduino-7
hide_title: false
pagination_next: null
---

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Make sure your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify it works. If the issue persists, swap it out for a different cable to rule out damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Check your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. The SCD43 uses the **fixed I2C address 0x62** - if the scanner does not find it, there is likely a wiring issue or a problem with the I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices on the same bus, make sure none of them share the address **0x62**. The SCD43's address is fixed and cannot be changed.

#### Try reinitializing
If the sensor fails to initialize on the first attempt, try calling `sensor.begin()` again or resetting your microcontroller. Some initialization issues can be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="readMeasurement() always returns false!">

#### Wait for the first measurement
The SCD43 needs up to **5 seconds** after `begin()` before it produces its first measurement. Make sure your code is not expecting data immediately after initialization.

#### Don't block with long delays
If you are using `delay()` values longer than the sensor's measurement interval (5 seconds), you may miss the data-ready window. Use short polling delays (500 ms or less) and check `readMeasurement()` frequently, as shown in the example.

#### Check that periodic measurement mode started
`sensor.begin()` starts periodic measurement mode automatically. If `begin()` returned `false`, the sensor did not initialize correctly and will never produce readings - fix the initialization issue first.

</ExpandableSection>

<ExpandableSection title="CO2 readings seem inaccurate or unstable!">

#### Allow warmup time
The SCD43 requires a **warmup period** of at least one minute after power-on before CO2 readings stabilize. Discard the first few readings after startup.

#### Allow ASC to calibrate
The Automatic Self-Calibration (ASC) algorithm needs the sensor to be exposed to **fresh outdoor air** regularly, matching its calibration target (**400 ppm** by default) - typically over several days of operation - to establish an accurate baseline. Indoor-only use without any ventilation will slow down calibration.

#### Check sensor placement
Keep the sensor away from direct breath, vents, or CO2 sources that would give artificially high readings. Also avoid enclosing the sensor in an airtight case - it needs free airflow to measure the surrounding environment accurately.

#### Avoid rapid temperature changes
Sudden temperature changes can temporarily affect CO2 readings due to the photoacoustic sensing principle. Allow the sensor to settle in its operating environment before relying on measurements.

</ExpandableSection>

<ExpandableSection title="Temperature or humidity readings seem wrong!">

#### Account for self-heating
The SCD43 generates a small amount of heat during operation, which can cause the reported temperature to read slightly higher than the actual ambient temperature. This is normal behavior - Sensirion provides a temperature offset compensation feature in the library if more accurate temperature readings are needed.

#### Check sensor placement
Do not mount the sensor directly against a heat source (e.g. a voltage regulator or processor). Give the board adequate airflow so the sensor measures ambient air rather than heat trapped around the PCB.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
