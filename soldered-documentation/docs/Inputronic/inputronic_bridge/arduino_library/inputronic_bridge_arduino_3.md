---
slug: /inputronic_bridge/arduino/interrupt-events 
title: Inputronic BRIDGE - Interrupt-driven reading
sidebar_label: Interrupt-driven reading
id: inputronic_bridge-arduino-3 
hide_title: False
---

This page walks through the `interruptEvents` example: reading keyboard, mouse, and MIDI events without polling on a fixed interval.

---

## Connections for this example

<ErrorBox>The connection diagram for this example hasn't been generated yet! We're working on it!</ErrorBox>

Wire the BRIDGE's **INT** pin to a digital input on your microcontroller, in addition to the usual Qwiic or I²C header connection from the Getting Started guide.

---

## Interrupt-driven reading

Instead of calling `pollEvents()` on a fixed interval, you can wire the BRIDGE's **INT** pin to your microcontroller and have it tell you exactly when new data has arrived. Pass the interrupt pin to `begin()` and, optionally, register a callback that fires the moment data is ready.

```cpp
#include "Inputronic-BRIDGE.h"

InputronicParser parser;

// Pin on the receiving MCU connected to the BRIDGE interrupt output.
static const int8_t INTERRUPT_PIN = 5;
volatile bool newDataFlag = false;

void onBridgeDataReady()
{
    newDataFlag = true;
}

void setup()
{
    Serial.begin(115200);

    Wire.begin(8, 9);
    parser.configureI2c(0x50);
    if (!parser.begin(InputronicParser::PROTOCOL_I2C, Wire,
                      true, INTERRUPT_PIN, false)) // interrupt on FALLING edge
    {
        Serial.println("Could not connect to BRIDGE over I2C!");
        while (true);
    }

    parser.onDataReady(onBridgeDataReady);
    Serial.println("BRIDGE connected, interrupt mode active.");
}

void loop()
{
    auto events = parser.pollEvents();

    if (events.keyboard.valid)
    {
        Serial.print("Keyboard: ");
        for (uint8_t i = 0; i < events.keyboard.keyCount; i++)
        {
            Serial.print(events.keyboard.keys[i]);
        }
        Serial.println();
    }

    if (events.mouse.valid)
    {
        Serial.printf("Mouse X:%d Y:%d L:%d R:%d M:%d Scroll:%d\n",
                      events.mouse.x, events.mouse.y,
                      events.mouse.btnLeft, events.mouse.btnRight,
                      events.mouse.btnMiddle, events.mouse.scroll);
    }

    if (newDataFlag)
    {
        newDataFlag = false;
        // events above already contain the latest data; this flag
        // can be used to trigger additional work on data arrival.
    }
}
```

<FunctionDocumentation
  functionName="parser.onDataReady()"
  description="Registers a callback that runs from interrupt context the moment the BRIDGE signals new data on the INT pin. Keep the callback short: no Serial prints or blocking calls, just set a flag and handle it in loop()."
  returnDescription="None"
  parameters={[
    { type: 'void (*)()', name: 'callback', description: 'Function pointer to call when new data arrives' },
  ]}
/>

<InfoBox>
`pollEvents()` still works the same way in interrupt mode. It just returns immediately without touching the bus unless the interrupt flag has actually been set, so calling it on every loop iteration is still the normal pattern.
</InfoBox>

---

## Full example

<QuickLink
    title="interruptEvents"
    description="Same as pollingEvents, but reads are triggered by the BRIDGE's interrupt pin instead of continuous polling."
    url="https://github.com/SolderedElectronics/Soldered-Inputronic-BRIDGE-Library/tree/main/examples/interruptEvents"
/>
