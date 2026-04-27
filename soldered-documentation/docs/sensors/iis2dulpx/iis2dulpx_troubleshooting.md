---
slug: /iis2dulpx/troubleshooting
title: Troubleshooting
sidebar_label: Troubleshooting
id: iis2dulpx-troubleshooting
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My sensor won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the sensor using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected. The IIS2DULPX uses the fixed I2C address **0x18**, so verify the scanner finds a device at that address.

#### Check for conflicting devices
If you have multiple I2C devices on the same bus, ensure none of them share the address **0x18**. If there is a conflict, remove the conflicting device or use a separate I2C bus.

#### Make sure `Wire.begin()` is called first (Arduino)
`sensor.begin()` assumes the I2C bus is already initialized. Always call `Wire.begin()` before `sensor.begin()` in your `setup()` function.

</ExpandableSection>

<ExpandableSection title="Acceleration readings are zero or not changing!">

#### Enable the accelerometer
Calling `sensor.begin()` alone is not enough — you must also call `sensor.Enable_X()` before reading data. Without it, the accelerometer stays in power-down mode and outputs zeros.

#### Check the full scale and ODR settings
If you manually configured the full scale or ODR, make sure the values are valid. Accepted full-scale values are **2, 4, 8, 16** (in g). If an invalid value is passed, the sensor may not configure correctly.

#### Don't read faster than the ODR
If you are polling `Get_X_Axes()` faster than the configured output data rate, you may read the same value multiple times. Add an appropriate delay, or poll the data-ready flag with `Get_X_DRDY_Status()` before each read.

</ExpandableSection>

<ExpandableSection title="My interrupt isn't triggering!">

#### Check the INT pin wiring
Make sure the **INT1** (or **INT2**) pin of the breakout is connected to a digital input pin on your microcontroller that supports interrupts.

#### Use the correct interrupt attachment
- **Arduino:** use `attachInterrupt(digitalPinToInterrupt(pin), callback, RISING)`
- **MicroPython:** use `pin.irq(trigger=Pin.IRQ_RISING, handler=callback)`

On ESP32-based boards (like Dasduino CONNECTPLUS), pass the GPIO number directly to `attachInterrupt`.

#### Check the wake-up threshold
If the threshold is set too high, normal movement won't trigger the interrupt. Use `Set_Wake_Up_Threshold()` to lower it and test with a smaller value first.

#### Verify the interrupt pin routing
Make sure the event is routed to the correct physical pin. `Enable_Wake_Up_Detection(IIS2DULPX_INT1_PIN)` routes the event to **INT1** — if you wired to **INT2**, use `IIS2DULPX_INT2_PIN` instead.

</ExpandableSection>

<ExpandableSection title="Arduino library not found!">

#### Install via Library Manager
In the Arduino IDE, open **Sketch → Include Library → Manage Libraries**, search for **Soldered IIS2DULPXTR Accelerometer**, and install it.

#### Manual installation
Download the library from the [GitHub repository](https://github.com/SolderedElectronics/Soldered-IIS2DULPXTR-Accelerometer-Arduino-Library) and install it via **Sketch → Include Library → Add .ZIP Library**.

</ExpandableSection>

<ExpandableSection title="MicroPython module not found!">

#### Copy the module to your board
The `iis2dulpx.py` file must be present in the root of your board's filesystem. Use a tool like **mpremote**, **Thonny**, or **rshell** to upload the file before running your script.

#### Check the import statement
Make sure you are importing from the correct module name: `from iis2dulpx import IIS2DULPX`

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
