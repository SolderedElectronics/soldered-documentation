---
slug: /pcal6416a/arduino/digital-write
title: PCAL6416A - Digital Write
sidebar_label: Digital Write
id: pcal6416a-arduino-3
hide_title: false
---

This page covers driving a digital output pin on the PCAL6416A GPIO expander.

---

## Writing a pin

Connect an LED with a current-limiting resistor between **A0** and GND.

```cpp
#include "PCAL6416A-SOLDERED.h"

PCAL6416A expander;

void setup()
{
    Serial.begin(115200);
    expander.begin();

    expander.pinModePCAL(PCAL6416A_A0, OUTPUT);
}

void loop()
{
    expander.digitalWritePCAL(PCAL6416A_A0, HIGH);
    delay(1000);
    expander.digitalWritePCAL(PCAL6416A_A0, LOW);
    delay(1000);
}
```

<FunctionDocumentation
  functionName="expander.pinModePCAL()"
  description="Configures a GPIO pin on the PCAL6416A expander as an input or output."
  returnDescription="None."
  parameters={[
    {
      name: "pin",
      type: "uint8_t",
      description: "The GPIO pin to configure. Use a constant such as PCAL6416A_A0-PCAL6416A_A7 or PCAL6416A_B0-PCAL6416A_B7."
    },
    {
      name: "mode",
      type: "uint8_t",
      description: "Pin mode: INPUT, OUTPUT, INPUT_PULLUP, or INPUT_PULLDOWN."
    }
  ]}
/>

<FunctionDocumentation
  functionName="expander.digitalWritePCAL()"
  description="Sets the output state of a selected GPIO pin on the PCAL6416A expander."
  returnDescription="None."
  parameters={[
    {
      name: "pin",
      type: "uint8_t",
      description: "The GPIO pin to write. Use a constant such as PCAL6416A_A0-PCAL6416A_A7 or PCAL6416A_B0-PCAL6416A_B7."
    },
    {
      name: "value",
      type: "uint8_t",
      description: "Output level: HIGH or LOW."
    }
  ]}
/>

The LED should blink on and off once per second.

{/* TODO: A picture of the example is needed here. */}

<QuickLink
  title="digitalWrite.ino"
  description="Full digital write example for the PCAL6416A GPIO expander"
  url="https://github.com/SolderedElectronics/Soldered-PCAL6416A-IO-Expander-Arduino-Library/blob/main/examples/digitalWrite/digitalWrite.ino"
/>
