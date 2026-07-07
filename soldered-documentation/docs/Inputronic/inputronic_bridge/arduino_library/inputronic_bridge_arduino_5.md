---
slug: /inputronic_bridge/arduino/troubleshooting 
title: Inputronic BRIDGE - Troubleshooting
sidebar_label: Troubleshooting
id: inputronic_bridge-arduino-5
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="begin() keeps returning false!">

#### Check that a USB device is actually plugged in
`begin()` works by pinging the BRIDGE and waiting for a response. On UART, the BRIDGE won't answer if no USB device has been attached yet, so plug in your keyboard, mouse, or MIDI device before calling `begin()`.

#### Check the protocol jumpers match your begin() call
The BRIDGE only listens on one protocol at a time, whichever JP3/JP4 state it's in. If you call `begin(InputronicParser::PROTOCOL_SPI, ...)` while the board is still in its default I²C mode, it will never respond. Bridge JP3 for UART or JP4 for SPI, and leave both open for I²C.

#### Verify the bus was started first
`Wire.begin()`, `Serial1.begin()`, or `SPI.begin()` all need to run before you call the parser's `begin()`. Double-check the pins you passed match how the BRIDGE is actually wired.

#### Scan for the I²C device
If you're using I²C, run an [**I²C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) to confirm the BRIDGE shows up. It should appear at **0x50** unless you've changed the address.

</ExpandableSection>

<ExpandableSection title="No keyboard, mouse, or MIDI events show up!">

#### Confirm the device class
The BRIDGE recognizes standard USB keyboards, mice, and MIDI controllers. Composite or vendor-specific devices may not map cleanly to any of the three event types. Try `setHidRawPolling(true)` and check `events.hidRaw.hex` to confirm the BRIDGE is receiving reports at all before assuming it's a wiring issue.

#### Make sure pollEvents() is called often enough
Events reflect only the latest report from the connected device. If `loop()` is blocked by a long `delay()` or another slow operation, you can miss short key presses or fast mouse movement.

#### Try a different USB device
Some USB HID devices, especially ones with unusual power requirements or nonstandard descriptors, may not enumerate correctly. Testing with a simple wired USB keyboard is a good way to confirm the BRIDGE itself is working.

</ExpandableSection>

<ExpandableSection title="The FAULT LED is on and my USB device won't power up!">

#### Check the device's current draw
The onboard USB-A port is current-limited to **260 mA**. Devices that draw more, such as RGB keyboards or ones with backlighting, will trip the overcurrent protection and light the red FAULT LED. Try the device on a powered USB hub instead of drawing power directly from the BRIDGE.

#### Power cycle the board
Once the overcurrent condition clears, unplug and reconnect the BRIDGE's power to reset the FAULT state.

#### Read the FAULT pin in your own code
If you want your microcontroller to detect this condition too, wire the header's **FAULT** pin to a digital input. It mirrors the same overcurrent signal driving the onboard LED.

</ExpandableSection>

<ExpandableSection title="I forgot the I²C address I changed it to!">

#### Run an I²C scanner
`changeI2CAddress()` stores the new address in non-volatile memory, so it survives power cycles. If you didn't note it down, run an [**I²C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) to find whatever address the BRIDGE is currently answering on.

#### Try the default address first
If the BRIDGE is a fresh, unmodified board, it will still be on **0x50**.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
