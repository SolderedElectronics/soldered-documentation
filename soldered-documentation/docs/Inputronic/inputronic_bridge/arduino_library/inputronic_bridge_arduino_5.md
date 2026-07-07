---
slug: /inputronic_bridge/arduino/change-i2c-address 
title: Inputronic BRIDGE - Changing the I²C address
sidebar_label: Changing the I²C address
id: inputronic_bridge-arduino-5 
hide_title: False
---

This page walks through the `changeI2CAddress` example: changing the BRIDGE's I²C address and verifying it took effect.

---

## Connections for this example

<ErrorBox>The connection diagram for this example hasn't been generated yet! We're working on it!</ErrorBox>

Connect the BRIDGE to your microcontroller via Qwiic or the I²C header pins as shown in the Getting Started guide.

---

## Changing the I²C address

The default address of **0x50** can be changed to anything in the **0x08–0x77** range with `changeI2CAddress()`. The library writes the new address to the BRIDGE's non-volatile storage immediately. You don't need to power cycle the board, and the address survives reboots.

```cpp
#include "Inputronic-BRIDGE.h"

// Current address the device is responding on.
#define CURRENT_I2C_ADDR 0x50

// Address to change to. Modify this to your desired address (0x08–0x77).
#define NEW_I2C_ADDR 0x30

InputronicParser parser;

void setup()
{
    Serial.begin(115200);
    delay(500);

    Wire.begin(21, 22); // Adjust SDA/SCL pins for your board.

    // --- Connect at the current address ---
    parser.configureI2c(CURRENT_I2C_ADDR);
    if (!parser.begin(InputronicParser::PROTOCOL_I2C, Wire))
    {
        Serial.println("Could not connect to BRIDGE at address 0x" + String(CURRENT_I2C_ADDR, HEX));
        Serial.println("Check wiring and that CURRENT_I2C_ADDR matches the device.");
        while (true);
    }
    Serial.println("Connected at address 0x" + String(CURRENT_I2C_ADDR, HEX));

    // --- Send the address change command ---
    Serial.println("Changing address to 0x" + String(NEW_I2C_ADDR, HEX) + "...");
    if (!parser.changeI2CAddress(NEW_I2C_ADDR))
    {
        Serial.println("changeI2CAddress() failed — check protocol.");
        while (true);
    }

    // --- Reconnect at the new address to verify ---
    if (!parser.begin(InputronicParser::PROTOCOL_I2C, Wire))
    {
        Serial.println("Could not reconnect at new address 0x" + String(NEW_I2C_ADDR, HEX));
        Serial.println("Address change may have failed.");
        while (true);
    }
    Serial.println("Success! BRIDGE now responds at address 0x" + String(NEW_I2C_ADDR, HEX));
}

void loop()
{
    // Normal event polling works as usual after the address change.
    auto events = parser.pollEvents();

    if (events.keyboard.valid)
    {
        for (uint8_t i = 0; i < events.keyboard.keyCount; i++)
        {
            Serial.print(events.keyboard.keys[i]);
        }
        Serial.println();
    }
}
```

<FunctionDocumentation
  functionName="parser.changeI2CAddress()"
  description="Sends a command that tells the BRIDGE to store a new I2C address in its non-volatile memory and reinitialize its I2C slave driver immediately. Also updates the address the library itself uses for subsequent calls."
  returnDescription="True if the command was sent successfully, false if the protocol wasn't initialized as I2C or the port is unavailable"
  parameters={[
    { type: 'uint8_t', name: 'newAddr', description: 'New 7-bit I2C address, valid range 0x08–0x77' },
  ]}
/>

<InfoBox>
If you forget which address you changed the BRIDGE to, run an [**I²C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) to find it, or check the [troubleshooting](/inputronic_bridge/arduino/troubleshooting) page.
</InfoBox>

---

## Full example

<QuickLink
    title="changeI2CAddress"
    description="Shows how to change and verify the BRIDGE's I2C address."
    url="https://github.com/SolderedElectronics/Soldered-Inputronic-BRIDGE-Library/tree/main/examples/changeI2CAddress"
/>
