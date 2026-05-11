---
slug: /inputronic-keyboard/troubleshooting 
title: Inputronic Keyboard - Troubleshooting
sidebar_label: Troubleshooting
id: inputronic-keyboard-troubleshooting
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My keyboard won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I²C pins
If you are connecting the keyboard using standard I²C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I²C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I²C devices
Run an [**I²C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the keyboard is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller's I²C bus. The keyboard should appear at address **0x34**.

#### Check power supply
The keyboard requires a **3.3V power supply**. Verify that your microcontroller is providing the correct voltage on the VCC/3V3 pin. Insufficient voltage can cause initialization failures.

#### Try reinitializing
If the keyboard fails to initialize on the first attempt, try calling `kbd.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="No key events are being detected!">

#### Check FIFO polling
Make sure you're regularly checking for events using `kbd.eventsAvailable()` and reading them with `kbd.readMappedEvent()`. The keyboard stores events in a 10-event FIFO buffer, but if you don't read them frequently enough, the buffer may overflow and lose data.

#### Verify key matrix configuration
Ensure the keyboard is properly configured for the 8×10 matrix. The library should handle this automatically during initialization, but you can verify by checking that `kbd.configureMatrix(8, 10)` was called successfully.

#### Test with polling example
Try running the basic polling example (`KeyboardPoll.ino` for Arduino or `keyboard-poll.py` for MicroPython) to verify that the keyboard hardware is working correctly. This will help isolate whether the issue is with your code or the hardware.

#### Clear stale events
If you suspect old events are clogging the FIFO, call `kbd.clearEvents()` to flush the buffer and start fresh.

</ExpandableSection>

<ExpandableSection title="SHIFT or CAPS isn't working correctly!">

#### Check labelToChar usage
Make sure you're using `kbd.labelToChar(label, true)` with the `applyShift` parameter set to `true` (Arduino) or `applyShift=True` (MicroPython). Without this parameter, SHIFT and CAPS transformations won't be applied.

#### Verify keymap configuration
The keyboard uses two keymaps: UPPER and LOWER. Pressing CAPS toggles between them internally. If case behavior seems inverted, you may need to check which keymap is currently active using `kbd.getActiveKeymap()`.

#### Understand CAPS XOR SHIFT behavior
For letters, the keyboard uses CAPS XOR SHIFT logic:
- CAPS ON + No SHIFT = Uppercase letters
- CAPS ON + SHIFT = Lowercase letters (inverted)
- CAPS OFF + No SHIFT = Lowercase letters  
- CAPS OFF + SHIFT = Uppercase letters

This is standard keyboard behavior and matches physical keyboards.

</ExpandableSection>

<ExpandableSection title="Some keys return wrong characters!">

#### Check the keymap files
The keyboard uses customizable keymaps defined in `Inputronic-Keymap.h` (Arduino) or within the module (MicroPython). If certain keys are returning unexpected characters, verify that the keymap matches your physical keyboard layout.

#### Verify shift map
For numbers and symbols with SHIFT, the keyboard uses `Inputronic-Shiftmap.h` (Arduino) to define transformations. If shifted characters are wrong (e.g., SHIFT+7 gives the wrong symbol), you may need to customize this file to match your regional keyboard layout.

#### Check for ghosting
If multiple keys are pressed simultaneously and you're getting unexpected key events, this may be due to ghosting. The keyboard supports N-key rollover, but certain key combinations can cause ghosting if the keys share rows and columns in specific patterns. Try pressing keys one at a time to verify this is the issue.

</ExpandableSection>

<ExpandableSection title="The keyboard stops responding after some time!">

#### Check I²C bus stability
If the keyboard stops responding during operation, there may be I²C communication errors. Try adding external pull-up resistors (4.7kΩ to 10kΩ) on the SDA and SCL lines if they're not already present.

#### Verify power stability
Ensure your power supply can provide sufficient current. If using USB power, try a different USB cable or power source. Voltage drops can cause the TCA8418 chip to malfunction.

#### Check for FIFO overflow
The keyboard has a 10-event buffer. If you're not reading events fast enough, the buffer can overflow. Check if the `OVR_FLOW_INT` bit is set in the interrupt status register, or simply ensure you're polling frequently enough (every 1-10ms is recommended).

#### Reset the device
As a last resort, you can perform a hardware reset by briefly pulling the RESET pin low, or simply power cycle the keyboard by disconnecting and reconnecting power.

</ExpandableSection>

<ExpandableSection title="Characters appear multiple times when I press a key once!">

#### Check debouncing settings
The keyboard has built-in hardware debouncing (50µs), but mechanical switches can still produce multiple events if they're worn or of poor quality. This is usually not a software issue but rather a hardware limitation of the switches themselves.

#### Verify event processing logic
Make sure you're only processing key **press** events and not both press and release. Check that your code filters out release events:

```cpp
// Arduino
if (!isRelease && label) {
    // Process only press events
}
```

```python
# MicroPython
if not isRelease and label:
    # Process only press events
```

#### Check for rapid re-reads
Ensure you're not reading the same event multiple times from the FIFO. Each call to `readMappedEvent()` should consume one event from the buffer.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>