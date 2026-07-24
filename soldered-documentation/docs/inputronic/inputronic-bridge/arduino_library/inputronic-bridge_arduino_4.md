---
slug: /inputronic-bridge/arduino/raw-hid
title: Inputronic BRIDGE - Reading raw HID reports
sidebar_label: Reading raw HID reports
id: inputronic-bridge-arduino-4
hide_title: False
---

The library parses standard keyboards and mice into ready-to-use structures. For USB devices that are not standard HID keyboards or mice, or when you want to process the report bytes yourself, you can read the unparsed HID report directly. Call `setHidRawPolling(true)` so the BRIDGE sends the raw report on every poll, then read the bytes from `events.hidRaw.hex` as a hex string.

---

## Connections for this example

This example uses the same I2C connection as the basic example. Connect the board to the **Nula DeepSleep** over the Qwiic (formerly easyC) system.

| **Nula DeepSleep** | **Inputronic BRIDGE** |
| ------------------ | --------------------- |
| Qwiic              | Qwiic                 |

---

## Enabling raw HID polling

```cpp
#include "Inputronic-BRIDGE.h"

InputronicParser parser;

void setup()
{
    Serial.begin(115200);

    Wire.begin();
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

<CenteredImage src="/img/inputronic-bridge/raw-HID-serial-monitor.png" alt="Raw HID example output from Serial Monitor" caption="Raw HID example output from Serial Monitor" width="500px"/>

<InfoBox>

**Reading the raw HID data**

The raw report is delivered through the `events.hidRaw` sub-structure of the `EventBundle`:

* **`valid`** (bool) - Check this first. It returns `true` when a new raw HID report has been received.
* **`hex`** (String) - The unparsed HID report bytes as a hexadecimal string, ready for you to process on the host.

</InfoBox>

If you only need a single raw report instead of a continuous stream, call `requestHidRawOnce()` before polling instead of `setHidRawPolling(true)`. The BRIDGE then returns one raw HID report on the next poll.

<FunctionDocumentation
functionName="parser.setHidRawPolling()"
description="Enables or disables continuous raw HID polling. When enabled, the BRIDGE sends the unparsed HID report on every call to pollEvents()."
returnDescription="None"
parameters={[
{ type: 'bool', name: 'enabled', description: "Set to true to request the raw HID report on every poll, false to stop." }
]}
/>

<FunctionDocumentation
functionName="parser.requestHidRawOnce()"
description="Requests a single raw HID report on the next poll, instead of the continuous stream enabled by setHidRawPolling()."
returnDescription="None"
parameters={[]}
/>
