---
slug: /inputronic_bridge/how-it-works 
title: Inputronic BRIDGE - How it works
sidebar_label: How it works
id: inputronic_bridge-how-it-works 
hide_title: False
---  

The Inputronic BRIDGE is built around [**Espressif**](https://www.espressif.com/en/products/socs/esp32-s3)'s **ESP32-S3**, wired here to a female USB-A port through its native USB peripheral. When you plug in a keyboard, mouse, or MIDI device, the ESP32-S3 acts as a USB host: it enumerates the device, reads its HID report descriptor, and figures out how to interpret the raw bytes it sends. From there, the firmware translates those bytes into the event structures the Arduino library hands back to your own microcontroller.

<CenteredImage src="/img/inputronic_bridge/chip.png" alt="ESP32-S3FH4R2 on the board" caption="ESP32-S3FH4R2 on the board" width="400px" />

---

## Datasheet

For the full electrical characteristics and pin descriptions of the microcontroller driving this board, see the official datasheet.

<QuickLink
    title="ESP32-S3 Series Datasheet"
    description="Espressif's datasheet covering the ESP32-S3 dual-core SoC used on this board"
    url="https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf"
/>

---

## How the bridge works

A USB HID device doesn't send "key A was pressed" over the wire. It sends a fixed-size report, a short array of bytes whose meaning is defined by a descriptor the device provides during enumeration. A keyboard's report might mark which of 8 simultaneous keys are held down; a mouse's report carries X/Y movement deltas, a scroll value, and button states packed into a few bytes. The ESP32-S3 reads these raw reports from the USB port and, based on the device class it detected, decodes them into one of five event types: keyboard, mouse, MIDI, HID descriptor, or raw HID.

<InfoBox>
If the BRIDGE doesn't recognize a connected device as a standard keyboard, mouse, or MIDI controller, you can still read its data. Raw HID polling passes the undecoded report bytes straight through as a hex string, so you can parse a custom or unusual HID device yourself.
</InfoBox>

Keyboard events track up to 8 keys held down at once, matching typical USB keyboard rollover. Mouse events carry signed X/Y deltas, a scroll value, and the state of five buttons, including left, right, middle, and the two side buttons found on many mice. MIDI events pass through the three raw status/data bytes of a MIDI message untouched, leaving the interpretation up to your project.

---

## Protocol communication

Once an event is decoded, the BRIDGE needs to hand it to your microcontroller, and this is where the selectable protocol comes in. In the default I²C mode, the BRIDGE acts as a slave device at address **0x50**, and your microcontroller reads out the latest event data by calling the library's `pollEvents()` function. UART and SPI modes work the same way from the sketch's point of view. Only the transport underneath changes, selected by which of JP3 or JP4 you bridge on the board and which protocol constant you pass to `begin()`.

<CenteredImage src="/img/inputronic_bridge/i2c_data_transfer.svg" alt="I2C SDA and SCL signal timing during a data transfer" caption="SDA and SCL signal timing during an I2C data transfer, the same protocol the BRIDGE uses by default" width="600px" />

For time-sensitive applications, the BRIDGE can also signal your microcontroller the moment new data is available through its **INT** pin, instead of making you poll continuously. This is configured through the same `begin()` call and is entirely optional.

<InfoBox>
The library handles all of the USB report decoding, event framing, and protocol-specific message formatting internally. Your sketch only ever deals with `KeyboardEvent`, `MouseEvent`, and `MIDIEvent` structures returned by `pollEvents()`, never the underlying byte stream.
</InfoBox>