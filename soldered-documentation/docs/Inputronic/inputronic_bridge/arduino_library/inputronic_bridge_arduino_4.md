---
slug: /inputronic_bridge/arduino/raw-hid-readings 
title: Inputronic BRIDGE - Reading raw HID data
sidebar_label: Reading raw HID data
id: inputronic_bridge-arduino-4 
hide_title: False
---

This page walks through the `rawHIDReadings` example: reading undecoded HID report bytes for devices the BRIDGE doesn't recognize as a keyboard, mouse, or MIDI controller.

---

## Connections for this example

<ErrorBox>The connection diagram for this example hasn't been generated yet! We're working on it!</ErrorBox>

Connect the BRIDGE to your microcontroller via Qwiic or the I²C header pins as shown in the Getting Started guide, then plug in the USB HID device you want to inspect.

---

## Reading raw HID data

If you plug in a device the BRIDGE doesn't recognize as a keyboard, mouse, or MIDI controller, or you just want the unprocessed report bytes, switch on raw HID polling. Every call to `pollEvents()` will then also return the latest report as a hex string.

```cpp
#include "Inputronic-BRIDGE.h"

InputronicParser parser;

void setup()
{
    Serial.begin(115200);

    Wire.begin(21, 22);
    parser.configureI2c(0x50);
    if (!parser.begin(InputronicParser::PROTOCOL_I2C, Wire))
    {
        Serial.println("Could not connect to BRIDGE over I2C!");
        while (true);
    }

    Serial.println("BRIDGE connected.");

    // Push raw HID bytes on every poll.
    parser.setHidRawPolling(true);
}

void loop()
{
    auto events = parser.pollEvents();

    if (events.hidRaw.valid)
    {
        Serial.print("HID RAW HEX: ");
        Serial.println(events.hidRaw.hex);
    }

    delay(30);
}
```

<FunctionDocumentation
  functionName="parser.setHidRawPolling()"
  description="Turns raw HID report polling on or off. While enabled, pollEvents() also fills in the hidRaw event with the latest report as a hex string, regardless of whether it was decoded as a keyboard, mouse, or MIDI event."
  returnDescription="None"
  parameters={[
    { type: 'bool', name: 'enabled', description: 'True to start including raw HID reports in pollEvents(), false to stop' },
  ]}
/>

<InfoBox>
Raw HID polling runs alongside normal event decoding. If the connected device is a recognized keyboard, mouse, or MIDI controller, `pollEvents()` still fills in those events too, the raw report is just extra data on top.
</InfoBox>

---

## Full example

<QuickLink
    title="rawHIDReadings"
    description="Shows how to read raw, undecoded HID reports for devices the BRIDGE doesn't recognize."
    url="https://github.com/SolderedElectronics/Soldered-Inputronic-BRIDGE-Library/tree/main/examples/rawHIDReadings"
/>
